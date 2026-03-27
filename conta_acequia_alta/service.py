from __future__ import annotations

from dataclasses import replace
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from uuid import uuid4

from conta_acequia_alta.models import Movimiento
from conta_acequia_alta.repository import MovimientoRepository

TIPOS_MOVIMIENTO = {"gasto", "ingreso"}


@dataclass(frozen=True)
class ValidationError:
    field: str
    message: str


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
