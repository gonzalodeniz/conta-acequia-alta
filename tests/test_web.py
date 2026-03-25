from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from wsgiref.util import setup_testing_defaults
import unittest

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
        self.assertIn("Libro de asientos contables", body)

    def test_registra_un_ingreso_y_lo_hace_visible_en_la_respuesta(self) -> None:
        status, body = self._call_app(
            "POST",
            "fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )

        self.assertEqual(status, "200 OK")
        self.assertIn("Movimiento registrado correctamente con identificador MOV-", body)
        self.assertIn("Cuota mensual", body)
        self.assertIn("Tipo: Ingreso", body)

    def test_muestra_errores_de_validacion_en_el_formulario(self) -> None:
        _, body = self._call_app("POST", "fecha=&concepto=&categoria=&tipo=&importe=")

        self.assertIn("Este campo es obligatorio.", body)

    def test_usa_base_path_configurado_en_la_accion_del_formulario(self) -> None:
        app = create_app(self.data_file, base_path="/contabilidad")

        status, body = self._call_app("GET", app=app, path="/contabilidad")

        self.assertEqual(status, "200 OK")
        self.assertIn('<form method="post" action="/contabilidad">', body)

    def test_devuelve_404_si_la_ruta_no_coincide_con_el_base_path(self) -> None:
        app = create_app(self.data_file, base_path="/contabilidad")

        status, body = self._call_app("GET", app=app, path="/")

        self.assertEqual(status, "404 Not Found")
        self.assertIn("Ruta no encontrada", body)

    def test_usa_script_name_como_ruta_publica_si_no_hay_base_path_configurado(self) -> None:
        status, body = self._call_app("GET", script_name="/portal")

        self.assertEqual(status, "200 OK")
        self.assertIn('<form method="post" action="/portal">', body)
        self.assertIn('href="/portal"', body)

    def test_filtra_el_libro_de_asientos_por_rango_de_fechas(self) -> None:
        self._call_app(
            "POST",
            "fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )
        self._call_app(
            "POST",
            "fecha=2026-03-25&concepto=Factura+agua&categoria=Suministros&tipo=gasto&importe=12.50",
        )

        status, body = self._call_app("GET", query_string="fecha_desde=2026-03-22&fecha_hasta=2026-03-26")

        self.assertEqual(status, "200 OK")
        self.assertNotIn("Cuota mensual", body)
        self.assertIn("Factura agua", body)

    def test_muestra_estado_vacio_claro_si_el_filtro_no_devuelve_resultados(self) -> None:
        self._call_app(
            "POST",
            "fecha=2026-03-21&concepto=Cuota+mensual&categoria=Recibos&tipo=ingreso&importe=35.25",
        )

        _, body = self._call_app("GET", query_string="fecha_desde=2026-03-22&fecha_hasta=2026-03-26")

        self.assertIn("No hay movimientos en el rango indicado.", body)

    def test_muestra_error_si_el_rango_de_fechas_no_es_coherente(self) -> None:
        _, body = self._call_app("GET", query_string="fecha_desde=2026-03-26&fecha_hasta=2026-03-22")

        self.assertIn("La fecha final debe ser igual o posterior a la fecha inicial.", body)

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


if __name__ == "__main__":
    unittest.main()
