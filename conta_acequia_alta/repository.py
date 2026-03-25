from __future__ import annotations

import json
from json import JSONDecodeError
from pathlib import Path
from tempfile import NamedTemporaryFile

from conta_acequia_alta.models import Movimiento


class StorageError(Exception):
    pass


class MovimientoRepository:
    def __init__(self, data_file: Path) -> None:
        self._data_file = data_file
        self._data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self._data_file.exists():
            self._data_file.write_text("[]\n", encoding="utf-8")

    def list_all(self) -> list[Movimiento]:
        try:
            raw_items = json.loads(self._data_file.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise StorageError("No se ha encontrado el fichero de datos de movimientos.") from exc
        except JSONDecodeError as exc:
            raise StorageError("El fichero de movimientos no tiene un formato JSON valido.") from exc
        except OSError as exc:
            raise StorageError("No se ha podido leer el fichero de movimientos.") from exc
        return [Movimiento.from_dict(item) for item in raw_items]

    def add(self, movimiento: Movimiento) -> None:
        movimientos = self.list_all()
        movimientos.append(movimiento)
        serialized = [item.to_dict() for item in movimientos]
        payload = json.dumps(serialized, ensure_ascii=True, indent=2) + "\n"
        try:
            with NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=self._data_file.parent,
                delete=False,
            ) as temp_file:
                temp_file.write(payload)
                temp_path = Path(temp_file.name)
            temp_path.replace(self._data_file)
        except OSError as exc:
            raise StorageError("No se ha podido guardar el movimiento en el fichero de datos.") from exc
