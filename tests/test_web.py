from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from wsgiref.util import setup_testing_defaults
import unittest
from unittest.mock import patch

from conta_acequia_alta.repository import StorageError
from conta_acequia_alta.web import create_app


class WebAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "movimientos.json"
        self.app = create_app(self.data_file)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_muestra_estado_vacio_cuando_no_hay_movimientos(self) -> None:
        status, body = self._call_app("GET")

        self.assertEqual(status, "200 OK")
        self.assertIn("Todavia no hay movimientos registrados.", body)
        self.assertIn("Libro de asientos editable", body)
        self.assertIn("Navegacion principal del administrador", body)
        self.assertIn("Anadir asiento", body)
        self.assertIn("Resumen financiero", body)
        self.assertIn("No hay movimientos registrados en el periodo seleccionado.", body)

    def test_registra_un_ingreso_desde_la_tabla_y_lo_hace_visible_en_la_respuesta(self) -> None:
        status, body = self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )

        self.assertEqual(status, "200 OK")
        self.assertIn("Asiento registrado correctamente para el movimiento MOV-", body)
        self.assertIn("Cuota mensual", body)
        self.assertIn(">1</span>", body)

    def test_muestra_errores_de_validacion_en_el_formulario(self) -> None:
        _, body = self._call_app("POST", "action=create&fecha=&concepto=&categoria=&tipo=&importe=")

        self.assertIn("Este campo es obligatorio.", body)

    def test_usa_base_path_configurado_en_la_accion_del_formulario(self) -> None:
        app = create_app(self.data_file, base_path="/contabilidad")

        status, body = self._call_app("GET", app=app, path="/contabilidad")

        self.assertEqual(status, "200 OK")
        self.assertIn('<form id="create-form" method="post" action="/contabilidad">', body)

    def test_devuelve_404_si_la_ruta_no_coincide_con_el_base_path(self) -> None:
        app = create_app(self.data_file, base_path="/contabilidad")

        status, body = self._call_app("GET", app=app, path="/")

        self.assertEqual(status, "404 Not Found")
        self.assertIn("Ruta no encontrada", body)

    def test_usa_script_name_como_ruta_publica_si_no_hay_base_path_configurado(self) -> None:
        status, body = self._call_app("GET", script_name="/portal")

        self.assertEqual(status, "200 OK")
        self.assertIn('<form id="create-form" method="post" action="/portal">', body)
        self.assertIn('href="/portal"', body)

    def test_filtra_el_libro_de_asientos_por_rango_de_fechas(self) -> None:
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-25&concepto=Factura+agua&categoria=Suministros&tipo=gasto&importe=12.50",
        )

        status, body = self._call_app("GET", query_string="fecha_desde=2026-03-22&fecha_hasta=2026-03-26")

        self.assertEqual(status, "200 OK")
        self.assertNotIn("Cuota mensual", body)
        self.assertIn("Factura agua", body)

    def test_muestra_estado_vacio_claro_si_el_filtro_no_devuelve_resultados(self) -> None:
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )

        _, body = self._call_app("GET", query_string="fecha_desde=2026-03-22&fecha_hasta=2026-03-26")

        self.assertIn("No hay movimientos en el rango indicado.", body)

    def test_permite_editar_un_asiento_directamente_desde_la_tabla(self) -> None:
        _, body = self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        identificador = self._extract_identificador(body)

        status, updated_body = self._call_app(
            "POST",
            (
                f"action=update&identificador={identificador}"
                "&fecha=2027-01-10&concepto=Cuota+anual&categoria=Recibos&tipo=ingreso&importe=45.00"
            ),
        )

        self.assertEqual(status, "200 OK")
        self.assertIn("Asiento actualizado correctamente", updated_body)
        self.assertIn("Cuota anual", updated_body)
        self.assertIn('value="2027-01-10"', updated_body)

    def test_muestra_numeracion_visible_y_reiniciada_por_ejercicio(self) -> None:
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-25&concepto=Factura+agua&categoria=Suministros&tipo=gasto&importe=12.50",
        )
        _, body = self._call_app(
            "POST",
            "action=create&fecha=2027-01-02&concepto=Cuota+enero&categoria=Recibos&tipo=ingreso&importe=35.25",
        )

        self.assertIn('<span class="entry-number">1</span>', body)
        self.assertIn('<span class="entry-number">2</span>', body)
        self.assertGreaterEqual(body.count('<span class="entry-number">1</span>'), 2)

    def test_reemplaza_el_formulario_principal_por_una_tabla_editable(self) -> None:
        _, body = self._call_app("GET")

        self.assertNotIn("Registro de movimientos contables", body)
        self.assertIn('<table aria-label="Libro de asientos editable">', body)
        self.assertNotIn("Guardar movimiento", body)

    def test_muestra_error_si_el_rango_de_fechas_no_es_coherente(self) -> None:
        _, body = self._call_app("GET", query_string="fecha_desde=2026-03-26&fecha_hasta=2026-03-22")

        self.assertIn("La fecha final debe ser igual o posterior a la fecha inicial.", body)

    def test_muestra_resumen_financiero_mensual_con_totales_del_periodo(self) -> None:
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-25&concepto=Factura+agua&categoria=Suministros&tipo=gasto&importe=12.50",
        )
        self._call_app(
            "POST",
            "action=create&fecha=2026-04-01&concepto=Cuota+abril&categoria=Recibos&tipo=ingreso&importe=40.00",
        )

        status, body = self._call_app(
            "GET",
            query_string="periodo_tipo=mensual&periodo_mes=2026-03&periodo_ejercicio=2026",
        )

        self.assertEqual(status, "200 OK")
        self.assertIn("Marzo 2026", body)
        self.assertIn("35.25 EUR", body)
        self.assertIn("12.50 EUR", body)
        self.assertIn("22.75 EUR", body)
        self.assertIn("Se han consolidado 2 movimientos del periodo.", body)

    def test_muestra_resumen_financiero_anual_y_conserva_contexto_en_formularios(self) -> None:
        self._call_app(
            "POST",
            "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        self._call_app(
            "POST",
            "action=create&fecha=2026-04-01&concepto=Cuota+abril&categoria=Recibos&tipo=ingreso&importe=40.00",
        )

        status, body = self._call_app(
            "GET",
            query_string="periodo_tipo=anual&periodo_mes=2026-03&periodo_ejercicio=2026&fecha_desde=2026-03-01",
        )

        self.assertEqual(status, "200 OK")
        self.assertIn("Ejercicio 2026", body)
        self.assertIn("75.25 EUR", body)
        self.assertIn('name="periodo_tipo" value="anual"', body)
        self.assertIn('name="periodo_ejercicio" value="2026"', body)
        self.assertIn('name="fecha_desde" value="2026-03-01"', body)

    def test_muestra_error_si_el_mes_del_resumen_es_invalido(self) -> None:
        _, body = self._call_app(
            "GET",
            query_string="periodo_tipo=mensual&periodo_mes=2026-13&periodo_ejercicio=2026",
        )

        self.assertIn("El mes debe usar el formato AAAA-MM.", body)

    def test_devuelve_503_y_mensaje_claro_si_el_json_esta_corrupto(self) -> None:
        self.data_file.write_text("{", encoding="utf-8")

        status, body = self._call_app("GET")

        self.assertEqual(status, "503 Service Unavailable")
        self.assertIn("El fichero de movimientos no tiene un formato JSON valido.", body)

    def test_devuelve_503_si_falla_el_guardado_del_movimiento(self) -> None:
        with patch(
            "conta_acequia_alta.web.MovimientoService.crear_movimiento",
            side_effect=StorageError("No se ha podido guardar el movimiento en el fichero de datos."),
        ):
            status, body = self._call_app(
                "POST",
                "action=create&fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
            )

        self.assertEqual(status, "503 Service Unavailable")
        self.assertIn("No se ha podido guardar el movimiento en el fichero de datos.", body)
        self.assertIn('value="Cuota mensual"', body)

    def _call_app(
        self,
        method: str,
        body: str = "",
        query_string: str = "",
        app=None,
        path: str = "/",
        script_name: str = "",
    ) -> tuple[str, str]:
        environ: dict[str, object] = {}
        setup_testing_defaults(environ)
        environ["REQUEST_METHOD"] = method
        environ["PATH_INFO"] = path
        environ["SCRIPT_NAME"] = script_name
        environ["QUERY_STRING"] = query_string
        encoded = body.encode("utf-8")
        environ["CONTENT_LENGTH"] = str(len(encoded))
        environ["wsgi.input"] = BytesIO(encoded)
        response_status: list[str] = []

        def start_response(status: str, _headers: list[tuple[str, str]]) -> None:
            response_status.append(status)

        chunks = (app or self.app)(environ, start_response)
        rendered = b"".join(chunks).decode("utf-8")
        return response_status[0], rendered

    def _extract_identificador(self, body: str) -> str:
        marker = "movimiento MOV-"
        start = body.index(marker) + len(marker)
        return f"MOV-{body[start:start + 8]}"


if __name__ == "__main__":
    unittest.main()
