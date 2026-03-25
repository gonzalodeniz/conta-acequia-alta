from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Callable
from urllib.parse import parse_qs

from conta_acequia_alta.repository import MovimientoRepository
from conta_acequia_alta.service import MovimientoService, ValidationError

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "movimientos.json"


def create_app(data_file: Path | None = None, base_path: str = "") -> Callable:
    repository = MovimientoRepository(data_file or DATA_FILE)
    service = MovimientoService(repository)
    normalized_base_path = _normalize_base_path(base_path)

    def app(environ: dict, start_response: Callable) -> list[bytes]:
        method = environ["REQUEST_METHOD"]
        path = _normalize_request_path(environ.get("PATH_INFO", "/"))
        public_base_path = _resolve_public_base_path(environ, normalized_base_path)

        if not _matches_path(path, normalized_base_path):
            start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
            return [b"Ruta no encontrada"]

        if method == "GET":
            return _render_page(start_response, service, public_base_path=public_base_path)

        if method == "POST":
            size = int(environ.get("CONTENT_LENGTH") or "0")
            raw_body = environ["wsgi.input"].read(size).decode("utf-8")
            form_data = {key: values[0] for key, values in parse_qs(raw_body).items()}
            movimiento, errors = service.crear_movimiento(form_data)
            return _render_page(
                start_response,
                service,
                form_data=form_data,
                errors=errors,
                public_base_path=public_base_path,
                success_message=(
                    f"Movimiento registrado correctamente con identificador {movimiento.identificador}."
                    if movimiento
                    else None
                ),
            )

        start_response("405 Method Not Allowed", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Metodo no permitido"]

    return app


def _render_page(
    start_response: Callable,
    service: MovimientoService,
    form_data: dict[str, str] | None = None,
    errors: list[ValidationError] | None = None,
    success_message: str | None = None,
    public_base_path: str = "",
) -> list[bytes]:
    form_data = form_data or {}
    errors = errors or []
    error_map = {error.field: error.message for error in errors}
    movimientos = service.listar_movimientos()
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    html = f"""<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Conta Acequia Alta</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #f3efe7;
        --panel: #fffdf9;
        --ink: #1e1e1e;
        --accent: #0c6c5a;
        --danger: #a12424;
        --expense: #6f1d1b;
        --income: #155d27;
        --line: #d9d0c3;
      }}
      body {{
        margin: 0;
        font-family: Georgia, serif;
        background: linear-gradient(180deg, #e7dfd2 0%, var(--bg) 100%);
        color: var(--ink);
      }}
      main {{
        max-width: 960px;
        margin: 0 auto;
        padding: 32px 20px 48px;
      }}
      .layout {{
        display: grid;
        gap: 24px;
      }}
      .panel {{
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(62, 47, 31, 0.08);
      }}
      h1, h2 {{
        margin-top: 0;
      }}
      form {{
        display: grid;
        gap: 16px;
      }}
      .grid {{
        display: grid;
        gap: 16px;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      }}
      label {{
        display: grid;
        gap: 6px;
        font-weight: 700;
      }}
      input, select, button {{
        font: inherit;
        padding: 10px 12px;
        border-radius: 10px;
        border: 1px solid #bfb3a2;
      }}
      button {{
        background: var(--accent);
        color: white;
        font-weight: 700;
        cursor: pointer;
      }}
      .message {{
        padding: 12px 14px;
        border-radius: 12px;
        margin-bottom: 16px;
      }}
      .success {{
        background: #e6f5ee;
        color: var(--income);
      }}
      .error {{
        color: var(--danger);
        font-size: 0.95rem;
      }}
      ul.movimientos {{
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 12px;
      }}
      li.movimiento {{
        border: 1px solid var(--line);
        border-left: 8px solid var(--accent);
        border-radius: 12px;
        padding: 14px 16px;
      }}
      li.movimiento.gasto {{
        border-left-color: var(--expense);
      }}
      li.movimiento.ingreso {{
        border-left-color: var(--income);
      }}
      .meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px 18px;
        font-size: 0.95rem;
      }}
      .empty {{
        padding: 16px;
        border: 1px dashed var(--line);
        border-radius: 12px;
      }}
    </style>
  </head>
  <body>
    <main>
      <section class="layout">
        <div class="panel">
          <h1>Registro de movimientos contables</h1>
          <p>Da de alta gastos e ingresos de la comunidad con la informacion minima obligatoria.</p>
          {_render_message(success_message, "success")}
          <form method="post" action="{public_base_path or '/'}">
            <div class="grid">
              {_render_input("fecha", "Fecha", "date", form_data, error_map)}
              {_render_select(form_data, error_map)}
              {_render_input("concepto", "Concepto", "text", form_data, error_map)}
              {_render_input("categoria", "Categoria", "text", form_data, error_map)}
              {_render_input("importe", "Importe", "number", form_data, error_map, step="0.01", min="0.01")}
            </div>
            <button type="submit">Guardar movimiento</button>
          </form>
        </div>
        <div class="panel">
          <h2>Ultimos movimientos registrados</h2>
          {_render_movimientos(movimientos)}
        </div>
      </section>
    </main>
  </body>
</html>"""
    return [html.encode("utf-8")]


def _render_message(message: str | None, css_class: str) -> str:
    if not message:
        return ""
    return f'<div class="message {css_class}">{escape(message)}</div>'


def _render_input(
    field: str,
    label: str,
    input_type: str,
    form_data: dict[str, str],
    error_map: dict[str, str],
    **attrs: str,
) -> str:
    extra = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    error = error_map.get(field, "")
    return (
        f'<label>{escape(label)}'
        f'<input type="{input_type}" name="{field}" value="{escape(form_data.get(field, ""))}" {extra}>'
        f'<span class="error">{escape(error)}</span>'
        f"</label>"
    )


def _render_select(form_data: dict[str, str], error_map: dict[str, str]) -> str:
    selected = form_data.get("tipo", "")
    options = []
    for value, label in (("", "Selecciona un tipo"), ("gasto", "Gasto"), ("ingreso", "Ingreso")):
        is_selected = ' selected="selected"' if value == selected else ""
        options.append(f'<option value="{value}"{is_selected}>{label}</option>')
    error = error_map.get("tipo", "")
    return (
        '<label>Tipo'
        f'<select name="tipo">{"".join(options)}</select>'
        f'<span class="error">{escape(error)}</span>'
        "</label>"
    )


def _render_movimientos(movimientos: list) -> str:
    if not movimientos:
        return '<div class="empty">Todavia no hay movimientos registrados.</div>'

    items = []
    for movimiento in movimientos:
        items.append(
            f'<li class="movimiento {escape(movimiento.tipo)}">'
            f"<strong>{escape(movimiento.concepto)}</strong>"
            f'<div class="meta">'
            f"<span>ID: {escape(movimiento.identificador)}</span>"
            f"<span>Fecha: {escape(movimiento.fecha)}</span>"
            f"<span>Categoria: {escape(movimiento.categoria)}</span>"
            f"<span>Tipo: {escape(movimiento.tipo.title())}</span>"
            f"<span>Importe: {escape(format(movimiento.importe, '.2f'))} EUR</span>"
            f"</div>"
            f"</li>"
        )
    return f'<ul class="movimientos">{"".join(items)}</ul>'


def _normalize_base_path(base_path: str) -> str:
    cleaned = base_path.strip()
    if not cleaned or cleaned == "/":
        return ""
    return "/" + cleaned.strip("/")


def _normalize_request_path(path: str) -> str:
    if not path:
        return "/"
    if path == "/":
        return path
    return "/" + path.strip("/")


def _resolve_public_base_path(environ: dict, configured_base_path: str) -> str:
    if configured_base_path:
        return configured_base_path
    script_name = _normalize_base_path(str(environ.get("SCRIPT_NAME", "")))
    return script_name


def _matches_path(path: str, base_path: str) -> bool:
    if not base_path:
        return path == "/"
    return path in {base_path, f"{base_path}/"}
