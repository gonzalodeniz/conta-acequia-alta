from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from app import DEFAULT_PORT, _load_env_file, _resolve_port


class AppConfigTests(unittest.TestCase):
    def test_carga_el_puerto_desde_el_fichero_env(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text('PORT="9090"\n', encoding="utf-8")

            file_env = _load_env_file(env_file)

            self.assertEqual(file_env["PORT"], "9090")
            self.assertEqual(_resolve_port({}, file_env), 9090)

    def test_usa_el_puerto_por_defecto_si_no_hay_configuracion(self) -> None:
        self.assertEqual(_resolve_port({}, {}), DEFAULT_PORT)

    def test_da_prioridad_a_la_variable_de_entorno_en_ejecucion(self) -> None:
        self.assertEqual(_resolve_port({"PORT": "6060"}, {"PORT": "9090"}), 6060)


if __name__ == "__main__":
    unittest.main()
