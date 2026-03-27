from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Movimiento:
    identificador: str
    fecha: str
    concepto: str
    categoria: str
    tipo: str
    importe: Decimal
    numero_asiento: int | None = None

    def to_dict(self) -> dict[str, str]:
        return {
            "identificador": self.identificador,
            "fecha": self.fecha,
            "concepto": self.concepto,
            "categoria": self.categoria,
            "tipo": self.tipo,
            "importe": format(self.importe, ".2f"),
        }

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Movimiento":
        return cls(
            identificador=data["identificador"],
            fecha=data["fecha"],
            concepto=data["concepto"],
            categoria=data["categoria"],
            tipo=data["tipo"],
            importe=Decimal(data["importe"]),
        )
