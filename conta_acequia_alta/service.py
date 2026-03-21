from __future__ import annotations

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
        errors = self._validate(payload)
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
        return movimiento, []

    def listar_movimientos(self) -> list[Movimiento]:
        return list(reversed(self._repository.list_all()))

    def _validate(self, payload: dict[str, str]) -> list[ValidationError]:
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
