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
        self.assertEqual(movimiento.numero_asiento, 1)
        movimientos, listing_errors = self.service.listar_movimientos()
        self.assertEqual(listing_errors, [])
        self.assertEqual(len(movimientos), 1)

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

    def test_lista_movimientos_en_orden_cronologico_y_filtra_por_rango(self) -> None:
        for payload in (
            {
                "fecha": "2026-03-25",
                "concepto": "Seguro",
                "categoria": "Servicios",
                "tipo": "gasto",
                "importe": "80.00",
            },
            {
                "fecha": "2026-03-21",
                "concepto": "Cuota ordinaria",
                "categoria": "Recibos",
                "tipo": "ingreso",
                "importe": "40.00",
            },
            {
                "fecha": "2026-03-23",
                "concepto": "Limpieza",
                "categoria": "Mantenimiento",
                "tipo": "gasto",
                "importe": "20.00",
            },
        ):
            _, errors = self.service.crear_movimiento(payload)
            self.assertEqual(errors, [])

        movimientos, errors = self.service.listar_movimientos("2026-03-22", "2026-03-25")

        self.assertEqual(errors, [])
        self.assertEqual([movimiento.fecha for movimiento in movimientos], ["2026-03-23", "2026-03-25"])
        self.assertEqual([movimiento.concepto for movimiento in movimientos], ["Limpieza", "Seguro"])

    def test_asigna_numero_correlativo_por_ejercicio(self) -> None:
        for payload in (
            {
                "fecha": "2025-12-31",
                "concepto": "Cierre previo",
                "categoria": "Tesoreria",
                "tipo": "gasto",
                "importe": "10.00",
            },
            {
                "fecha": "2026-01-02",
                "concepto": "Cuota enero",
                "categoria": "Recibos",
                "tipo": "ingreso",
                "importe": "40.00",
            },
            {
                "fecha": "2026-02-02",
                "concepto": "Seguro",
                "categoria": "Servicios",
                "tipo": "gasto",
                "importe": "80.00",
            },
        ):
            _, errors = self.service.crear_movimiento(payload)
            self.assertEqual(errors, [])

        movimientos, errors = self.service.listar_movimientos()

        self.assertEqual(errors, [])
        self.assertEqual(
            [(movimiento.fecha, movimiento.numero_asiento) for movimiento in movimientos],
            [("2025-12-31", 1), ("2026-01-02", 1), ("2026-02-02", 2)],
        )

    def test_actualiza_un_movimiento_y_recalcula_su_numero_en_otro_ejercicio(self) -> None:
        primero, errors = self.service.crear_movimiento(
            {
                "fecha": "2026-03-01",
                "concepto": "Cuota marzo",
                "categoria": "Recibos",
                "tipo": "ingreso",
                "importe": "40.00",
            }
        )
        self.assertEqual(errors, [])
        segundo, errors = self.service.crear_movimiento(
            {
                "fecha": "2026-03-15",
                "concepto": "Agua",
                "categoria": "Suministros",
                "tipo": "gasto",
                "importe": "12.50",
            }
        )
        self.assertEqual(errors, [])
        assert primero is not None
        assert segundo is not None

        movimiento, errors = self.service.actualizar_movimiento(
            {
                "identificador": segundo.identificador,
                "fecha": "2027-01-05",
                "concepto": "Agua actualizada",
                "categoria": "Suministros",
                "tipo": "gasto",
                "importe": "15.00",
            }
        )

        self.assertEqual(errors, [])
        assert movimiento is not None
        movimientos, listing_errors = self.service.listar_movimientos()
        self.assertEqual(listing_errors, [])
        self.assertEqual(
            [(item.identificador, item.fecha, item.numero_asiento) for item in movimientos],
            [
                (primero.identificador, "2026-03-01", 1),
                (segundo.identificador, "2027-01-05", 1),
            ],
        )

    def test_informa_error_si_el_rango_de_fechas_es_invalido(self) -> None:
        movimientos, errors = self.service.listar_movimientos("2026-03-30", "2026-03-01")

        self.assertEqual(movimientos, [])
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].field, "fecha_hasta")


if __name__ == "__main__":
    unittest.main()
