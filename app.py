from os import environ
from pathlib import Path
from typing import Mapping
from wsgiref.simple_server import make_server

from conta_acequia_alta.web import create_app

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_BASE_PATH = ""
ENV_FILE = Path(__file__).resolve().parent / ".env"


def main() -> None:
    file_env = _load_env_file(ENV_FILE)
    host, port = _resolve_server_address(file_env, environ)
    base_path = _resolve_base_path(environ, file_env)
    app = create_app(base_path=base_path)
    with make_server(host, port, app) as httpd:
        print(f"Aplicacion disponible en http://{host}:{port}{base_path or '/'}")
        httpd.serve_forever()


def _resolve_server_address(file_env: Mapping[str, str], runtime_env: Mapping[str, str]) -> tuple[str, int]:
    host = _resolve_host(runtime_env, file_env)
    port = _resolve_port(runtime_env, file_env)
    return host, port


def _load_env_file(env_file: Path) -> dict[str, str]:
    if not env_file.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def _resolve_port(runtime_env: Mapping[str, str], file_env: Mapping[str, str]) -> int:
    raw_port = runtime_env.get("PORT") or file_env.get("PORT")
    if not raw_port:
        return DEFAULT_PORT

    try:
        port = int(raw_port)
    except ValueError as exc:  # pragma: no cover - defensive branch
        raise ValueError("PORT debe ser un numero entero valido.") from exc

    if port < 1 or port > 65535:
        raise ValueError("PORT debe estar entre 1 y 65535.")

    return port


def _resolve_host(runtime_env: Mapping[str, str], file_env: Mapping[str, str]) -> str:
    raw_host = runtime_env.get("HOST") or file_env.get("HOST") or DEFAULT_HOST
    host = raw_host.strip()
    if not host:
        raise ValueError("HOST no puede estar vacio.")
    return host


def _resolve_base_path(runtime_env: Mapping[str, str], file_env: Mapping[str, str]) -> str:
    raw_base_path = runtime_env.get("BASE_PATH") or file_env.get("BASE_PATH") or DEFAULT_BASE_PATH
    return _normalize_base_path(raw_base_path)


def _normalize_base_path(raw_base_path: str) -> str:
    base_path = raw_base_path.strip()
    if not base_path or base_path == "/":
        return ""

    normalized = "/" + base_path.strip("/")
    return normalized.rstrip("/")


if __name__ == "__main__":
    main()
