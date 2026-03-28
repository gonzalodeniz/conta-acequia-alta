from __future__ import annotations

from dataclasses import replace
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from uuid import uuid4

from conta_acequia_alta.models import Movimiento
from conta_acequia_alta.repository import MovimientoRepository

TIPOS_MOVIMIENTO = {"gasto", "ingreso"}
TIPOS_RESUMEN = {"mensual", "anual"}
MESES_ES = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}


@dataclass(frozen=True)
class ValidationError:
    field: str
    message: str


@dataclass(frozen=True)
class ResumenPeriodo:
    periodo_tipo: str
    periodo_referencia: str
    etiqueta: str
    total_ingresos: Decimal
    total_gastos: Decimal
    saldo: Decimal
    total_movimientos: int


class MovimientoService:
    def __init__(self, repository: MovimientoRepository) -> None:
        self._repository = repository

    def crear_movimiento(self, payload: dict[str, str]) -> tuple[Movimiento | None, list[ValidationError]]:
        errors = self._validate_payload(payload)
        if errors:
            return None, errors

        movimiento = Movimiento(
            identificador=f"MOV-{uuid4().hex[:8].upper()}",
            fecha=payload["fecha"].strip(),
            concepto=payload["concepto"].strip(),
            categoria=payload["categoria"].strip(),
            tipo=payload["tipo"].strip(),
            importe=Decimal(payload["importe"].strip()).quantize(Decimal("0.01")),
        )
        self._repository.add(movimiento)
        return self._assign_entry_numbers([movimiento])[0], []

    def actualizar_movimiento(self, payload: dict[str, str]) -> tuple[Movimiento | None, list[ValidationError]]:
        identificador = payload.get("identificador", "").strip()
        if not identificador:
            return None, [ValidationError("identificador", "No se ha indicado el movimiento a actualizar.")]

        errors = self._validate_payload(payload)
        if errors:
            return None, errors

        movimiento = Movimiento(
            identificador=identificador,
            fecha=payload["fecha"].strip(),
            concepto=payload["concepto"].strip(),
            categoria=payload["categoria"].strip(),
            tipo=payload["tipo"].strip(),
            importe=Decimal(payload["importe"].strip()).quantize(Decimal("0.01")),
        )
        self._repository.update(movimiento)
        return self._assign_entry_numbers([movimiento])[0], []

    def listar_movimientos(
        self,
        fecha_desde: str = "",
        fecha_hasta: str = "",
    ) -> tuple[list[Movimiento], list[ValidationError]]:
        errors = self._validate_range(fecha_desde, fecha_hasta)
        if errors:
            return [], errors

        movimientos = self._sort_movimientos(self._repository.list_all())
        if fecha_desde:
            movimientos = [movimiento for movimiento in movimientos if movimiento.fecha >= fecha_desde]
        if fecha_hasta:
            movimientos = [movimiento for movimiento in movimientos if movimiento.fecha <= fecha_hasta]
        return self._assign_entry_numbers(movimientos), []

    def resumir_movimientos(
        self,
        periodo_tipo: str = "",
        periodo_mes: str = "",
        periodo_ejercicio: str = "",
    ) -> tuple[ResumenPeriodo | None, list[ValidationError]]:
        normalized_tipo, normalized_mes, normalized_ejercicio = self._normalize_summary_input(
            periodo_tipo,
            periodo_mes,
            periodo_ejercicio,
        )
        errors = self._validate_summary_input(normalized_tipo, normalized_mes, normalized_ejercicio)
        if errors:
            return None, errors

        prefix = normalized_mes if normalized_tipo == "mensual" else normalized_ejercicio
        movimientos = [
            movimiento for movimiento in self._repository.list_all() if movimiento.fecha.startswith(prefix)
        ]
        total_ingresos = sum(
            (movimiento.importe for movimiento in movimientos if movimiento.tipo == "ingreso"),
            Decimal("0.00"),
        )
        total_gastos = sum(
            (movimiento.importe for movimiento in movimientos if movimiento.tipo == "gasto"),
            Decimal("0.00"),
        )
        return (
            ResumenPeriodo(
                periodo_tipo=normalized_tipo,
                periodo_referencia=prefix,
                etiqueta=self._build_summary_label(normalized_tipo, normalized_mes, normalized_ejercicio),
                total_ingresos=total_ingresos.quantize(Decimal("0.01")),
                total_gastos=total_gastos.quantize(Decimal("0.01")),
                saldo=(total_ingresos - total_gastos).quantize(Decimal("0.01")),
                total_movimientos=len(movimientos),
            ),
            [],
        )

    def _validate_payload(self, payload: dict[str, str]) -> list[ValidationError]:
        errors: list[ValidationError] = []

        for field in ("fecha", "concepto", "categoria", "tipo", "importe"):
            if not payload.get(field, "").strip():
                errors.append(ValidationError(field, "Este campo es obligatorio."))

        fecha = payload.get("fecha", "").strip()
        if fecha:
            try:
                date.fromisoformat(fecha)
            except ValueError:
                errors.append(ValidationError("fecha", "La fecha debe usar el formato AAAA-MM-DD."))

        tipo = payload.get("tipo", "").strip()
        if tipo and tipo not in TIPOS_MOVIMIENTO:
            errors.append(ValidationError("tipo", "El tipo debe ser gasto o ingreso."))

        importe = payload.get("importe", "").strip()
        if importe:
            try:
                amount = Decimal(importe)
                if amount <= 0:
                    errors.append(ValidationError("importe", "El importe debe ser mayor que cero."))
            except InvalidOperation:
                errors.append(ValidationError("importe", "El importe debe ser un numero valido."))

        return errors

    def _validate_range(self, fecha_desde: str, fecha_hasta: str) -> list[ValidationError]:
        errors: list[ValidationError] = []
        for field, value in (("fecha_desde", fecha_desde), ("fecha_hasta", fecha_hasta)):
            if not value:
                continue
            try:
                date.fromisoformat(value)
            except ValueError:
                errors.append(ValidationError(field, "La fecha debe usar el formato AAAA-MM-DD."))

        if not errors and fecha_desde and fecha_hasta and fecha_desde > fecha_hasta:
            errors.append(
                ValidationError("fecha_hasta", "La fecha final debe ser igual o posterior a la fecha inicial.")
            )
        return errors

    def _validate_summary_input(
        self,
        periodo_tipo: str,
        periodo_mes: str,
        periodo_ejercicio: str,
    ) -> list[ValidationError]:
        errors: list[ValidationError] = []
        if periodo_tipo not in TIPOS_RESUMEN:
            errors.append(ValidationError("periodo_tipo", "El periodo debe ser mensual o anual."))
            return errors

        if periodo_tipo == "mensual":
            if not periodo_mes:
                errors.append(ValidationError("periodo_mes", "Debes indicar un mes para consultar el resumen."))
                return errors
            try:
                date.fromisoformat(f"{periodo_mes}-01")
            except ValueError:
                errors.append(ValidationError("periodo_mes", "El mes debe usar el formato AAAA-MM."))
            return errors

        if not periodo_ejercicio:
            errors.append(ValidationError("periodo_ejercicio", "Debes indicar un ejercicio para el resumen anual."))
            return errors

        if not periodo_ejercicio.isdigit() or len(periodo_ejercicio) != 4:
            errors.append(ValidationError("periodo_ejercicio", "El ejercicio debe usar el formato AAAA."))
        return errors

    def _normalize_summary_input(
        self,
        periodo_tipo: str,
        periodo_mes: str,
        periodo_ejercicio: str,
    ) -> tuple[str, str, str]:
        today = date.today()
        normalized_tipo = periodo_tipo.strip() or "mensual"
        normalized_mes = periodo_mes.strip() or today.strftime("%Y-%m")
        normalized_ejercicio = periodo_ejercicio.strip() or str(today.year)
        return normalized_tipo, normalized_mes, normalized_ejercicio

    def _build_summary_label(self, periodo_tipo: str, periodo_mes: str, periodo_ejercicio: str) -> str:
        if periodo_tipo == "mensual":
            year, month = periodo_mes.split("-")
            return f"{MESES_ES[int(month)].capitalize()} {year}"
        return f"Ejercicio {periodo_ejercicio}"

    def _sort_movimientos(self, movimientos: list[Movimiento]) -> list[Movimiento]:
        return sorted(movimientos, key=lambda movimiento: (movimiento.fecha, movimiento.identificador))

    def _assign_entry_numbers(self, movimientos: list[Movimiento]) -> list[Movimiento]:
        counters_by_year: dict[str, int] = {}
        numbered_movimientos: list[Movimiento] = []
        for movimiento in self._sort_movimientos(movimientos):
            year = movimiento.fecha[:4]
            counters_by_year[year] = counters_by_year.get(year, 0) + 1
            numbered_movimientos.append(replace(movimiento, numero_asiento=counters_by_year[year]))
        return numbered_movimientos
