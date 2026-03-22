from __future__ import annotations

import json
from pathlib import Path

from conta_acequia_alta.models import Movimiento


class MovimientoRepository:
    def __init__(self, data_file: Path) -> None:
        self._data_file = data_file
        self._data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self._data_file.exists():
            self._data_file.write_text("[]\n", encoding="utf-8")

    def list_all(self) -> list[Movimiento]:
        raw_items = json.loads(self._data_file.read_text(encoding="utf-8"))
        return [Movimiento.from_dict(item) for item in raw_items]

    def add(self, movimiento: Movimiento) -> None:
        movimientos = self.list_all()
        movimientos.append(movimiento)
        serialized = [item.to_dict() for item in movimientos]
        self._data_file.write_text(
            json.dumps(serialized, ensure_ascii=True, indent=2) + "\n",
            encoding="utf-8",
        )
