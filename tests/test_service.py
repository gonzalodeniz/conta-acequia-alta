from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from conta_acequia_alta.repository import MovimientoRepository
from conta_acequia_alta.service import MovimientoService


class MovimientoServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        data_file = Path(self.temp_dir.name) / "movimientos.json"
        repository = MovimientoRepository(data_file)
        self.service = MovimientoService(repository)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_crea_un_gasto_valido_con_identificador_unico(self) -> None:
        movimiento, errors = self.service.crear_movimiento(
            {
                "fecha": "2026-03-21",
                "concepto": "Reparacion bomba",
                "categoria": "Mantenimiento",
                "tipo": "gasto",
                "importe": "125.50",
            }
        )

        self.assertEqual(errors, [])
        self.assertIsNotNone(movimiento)
        assert movimiento is not None
        self.assertTrue(movimiento.identificador.startswith("MOV-"))
        self.assertEqual(movimiento.importe, Decimal("125.50"))
        self.assertEqual(len(self.service.listar_movimientos()), 1)

    def test_rechaza_campos_obligatorios_vacios(self) -> None:
        movimiento, errors = self.service.crear_movimiento(
            {
                "fecha": "",
                "concepto": "",
                "categoria": "",
                "tipo": "",
                "importe": "",
            }
        )

        self.assertIsNone(movimiento)
        self.assertEqual({error.field for error in errors}, {"fecha", "concepto", "categoria", "tipo", "importe"})

    def test_rechaza_tipo_no_permitido_e_importe_negativo(self) -> None:
        movimiento, errors = self.service.crear_movimiento(
            {
                "fecha": "2026-03-21",
                "concepto": "Cuota extraordinaria",
                "categoria": "Derramas",
                "tipo": "transferencia",
                "importe": "-10",
            }
        )

        self.assertIsNone(movimiento)
        self.assertEqual({error.field for error in errors}, {"tipo", "importe"})


if __name__ == "__main__":
    unittest.main()
