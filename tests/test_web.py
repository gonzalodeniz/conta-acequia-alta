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

    def _call_app(self, method: str, body: str = "") -> tuple[str, str]:
        environ: dict[str, object] = {}
        setup_testing_defaults(environ)
        environ["REQUEST_METHOD"] = method
        encoded = body.encode("utf-8")
        environ["CONTENT_LENGTH"] = str(len(encoded))
        environ["wsgi.input"] = BytesIO(encoded)
        response_status: list[str] = []

        def start_response(status: str, _headers: list[tuple[str, str]]) -> None:
            response_status.append(status)

        chunks = self.app(environ, start_response)
        rendered = b"".join(chunks).decode("utf-8")
        return response_status[0], rendered


if __name__ == "__main__":
    unittest.main()
