from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from app import DEFAULT_HOST, DEFAULT_PORT, _load_env_file, _resolve_base_path, _resolve_host, _resolve_port


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

    def test_usa_host_por_defecto_si_no_hay_configuracion(self) -> None:
        self.assertEqual(_resolve_host({}, {}), DEFAULT_HOST)

    def test_carga_host_desde_el_fichero_env(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text('HOST="0.0.0.0"\n', encoding="utf-8")

            file_env = _load_env_file(env_file)

            self.assertEqual(file_env["HOST"], "0.0.0.0")
            self.assertEqual(_resolve_host({}, file_env), "0.0.0.0")

    def test_da_prioridad_al_host_de_entorno_en_ejecucion(self) -> None:
        self.assertEqual(_resolve_host({"HOST": "0.0.0.0"}, {"HOST": "127.0.0.1"}), "0.0.0.0")

    def test_carga_base_path_desde_el_fichero_env(self) -> None:
        with TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text('BASE_PATH="/contabilidad"\n', encoding="utf-8")

            file_env = _load_env_file(env_file)

            self.assertEqual(file_env["BASE_PATH"], "/contabilidad")
            self.assertEqual(_resolve_base_path({}, file_env), "/contabilidad")

    def test_normaliza_base_path_raiz_como_vacio(self) -> None:
        self.assertEqual(_resolve_base_path({}, {"BASE_PATH": "/"}), "")

    def test_base_path_de_entorno_en_ejecucion_tiene_prioridad(self) -> None:
        self.assertEqual(
            _resolve_base_path({"BASE_PATH": "portal/comunidad"}, {"BASE_PATH": "/contabilidad"}),
            "/portal/comunidad",
        )


if __name__ == "__main__":
    unittest.main()
