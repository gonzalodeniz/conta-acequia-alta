from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Callable
from urllib.parse import parse_qs

from conta_acequia_alta.repository import MovimientoRepository, StorageError
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
            filter_data = _parse_filter_data(_parse_form_data(environ.get("QUERY_STRING", "")))
            try:
                return _render_page(
                    start_response,
                    service,
                    filter_data=filter_data,
                    public_base_path=public_base_path,
                )
            except StorageError as error:
                return _render_storage_error_page(start_response, public_base_path, str(error))

        if method == "POST":
            size = int(environ.get("CONTENT_LENGTH") or "0")
            raw_body = environ["wsgi.input"].read(size).decode("utf-8")
            form_data = _parse_form_data(raw_body)
            filter_data = _parse_filter_data(form_data)
            action = form_data.get("action", "create").strip()
            try:
                if action == "update":
                    movimiento, errors = service.actualizar_movimiento(form_data)
                    active_form = f"edit:{form_data.get('identificador', '').strip()}"
                    success_message = (
                        f"Asiento actualizado correctamente para el movimiento {movimiento.identificador}."
                        if movimiento
                        else None
                    )
                else:
                    movimiento, errors = service.crear_movimiento(form_data)
                    active_form = "create"
                    success_message = (
                        f"Asiento registrado correctamente para el movimiento {movimiento.identificador}."
                        if movimiento
                        else None
                    )

                return _render_page(
                    start_response,
                    service,
                    form_data=form_data,
                    filter_data=filter_data,
                    errors=errors,
                    active_form=active_form,
                    public_base_path=public_base_path,
                    success_message=success_message,
                )
            except StorageError as error:
                return _render_storage_error_page(
                    start_response,
                    public_base_path,
                    str(error),
                    form_data=form_data,
                    filter_data=filter_data,
                    active_form=f"edit:{form_data.get('identificador', '').strip()}" if action == "update" else "create",
                )

        start_response("405 Method Not Allowed", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Metodo no permitido"]

    return app


def _render_page(
    start_response: Callable,
    service: MovimientoService,
    form_data: dict[str, str] | None = None,
    filter_data: dict[str, str] | None = None,
    errors: list[ValidationError] | None = None,
    success_message: str | None = None,
    public_base_path: str = "",
    status: str = "200 OK",
    storage_error: str | None = None,
    active_form: str = "create",
) -> list[bytes]:
    form_data = form_data or {}
    filter_data = filter_data or {}
    page_errors = errors or []
    movimientos, filter_errors = service.listar_movimientos(
        filter_data.get("fecha_desde", "").strip(),
        filter_data.get("fecha_hasta", "").strip(),
    )
    error_map = {error.field: error.message for error in page_errors + filter_errors}
    start_response(status, [("Content-Type", "text/html; charset=utf-8")])
    html = f"""<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Conta Acequia Alta</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #efe7da;
        --panel: #fffdf8;
        --panel-alt: #f7f1e7;
        --ink: #231b16;
        --muted: #6d5c4d;
        --accent: #0d5d56;
        --accent-soft: #d8ece8;
        --danger: #9d2d20;
        --danger-soft: #f6e1dc;
        --line: #d7c8b6;
        --expense: #7e2a1d;
        --income: #1d6b38;
      }}
      * {{
        box-sizing: border-box;
      }}
      body {{
        margin: 0;
        font-family: Georgia, serif;
        background:
          radial-gradient(circle at top left, rgba(255, 255, 255, 0.65), transparent 30%),
          linear-gradient(180deg, #e6dbc9 0%, var(--bg) 100%);
        color: var(--ink);
      }}
      .workspace {{
        min-height: 100vh;
        display: grid;
        grid-template-columns: 104px minmax(0, 1fr);
      }}
      .sidebar {{
        background: #1c342f;
        color: #f7f2ea;
        padding: 28px 16px;
        display: grid;
        align-content: start;
        gap: 18px;
      }}
      .brand {{
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: rgba(247, 242, 234, 0.78);
      }}
      .nav-item {{
        display: grid;
        justify-items: center;
        gap: 8px;
        text-decoration: none;
        color: inherit;
        font-size: 0.78rem;
      }}
      .nav-icon {{
        width: 48px;
        height: 48px;
        border-radius: 14px;
        display: grid;
        place-items: center;
        border: 1px solid rgba(255, 255, 255, 0.16);
        background: rgba(255, 255, 255, 0.06);
        font-weight: 700;
      }}
      .nav-item.active .nav-icon {{
        background: var(--accent-soft);
        color: var(--accent);
        border-color: transparent;
      }}
      .content {{
        padding: 32px 24px 48px;
      }}
      .hero {{
        max-width: 1200px;
        margin: 0 auto 24px;
      }}
      .eyebrow {{
        margin: 0 0 12px;
        color: var(--accent);
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
      }}
      h1 {{
        margin: 0 0 12px;
        font-size: clamp(2rem, 3vw, 3rem);
      }}
      .lead {{
        margin: 0;
        max-width: 70ch;
        color: var(--muted);
      }}
      .panel {{
        max-width: 1200px;
        margin: 0 auto;
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 16px 40px rgba(62, 47, 31, 0.08);
      }}
      .panel + .panel {{
        margin-top: 24px;
      }}
      .section-head {{
        display: flex;
        justify-content: space-between;
        gap: 16px;
        align-items: end;
        margin-bottom: 18px;
      }}
      .section-head h2 {{
        margin: 0 0 6px;
      }}
      .section-head p {{
        margin: 0;
        color: var(--muted);
      }}
      form.filters {{
        display: grid;
        gap: 16px;
        margin-bottom: 24px;
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
      }}
      input, select {{
        width: 100%;
        padding: 10px 12px;
        border-radius: 12px;
        border: 1px solid #c8baa8;
        background: #fff;
      }}
      .table-input {{
        min-width: 100%;
        padding: 9px 10px;
        border-radius: 10px;
      }}
      .table-actions {{
        display: flex;
        gap: 10px;
        align-items: center;
        flex-wrap: wrap;
      }}
      .table-actions .link {{
        color: var(--accent);
        font-weight: 700;
        text-decoration: none;
      }}
      button {{
        border: 0;
        border-radius: 999px;
        padding: 11px 18px;
        font-weight: 700;
        cursor: pointer;
        background: var(--accent);
        color: #fff;
      }}
      .button-secondary {{
        background: #e8ddd0;
        color: var(--ink);
      }}
      .message {{
        padding: 12px 14px;
        border-radius: 14px;
        margin-bottom: 16px;
      }}
      .success {{
        background: #e4f3e8;
        color: var(--income);
      }}
      .error-banner {{
        background: var(--danger-soft);
        color: var(--danger);
      }}
      .error {{
        display: block;
        color: var(--danger);
        font-size: 0.84rem;
        margin-top: 6px;
      }}
      .sheet {{
        overflow-x: auto;
        border: 1px solid var(--line);
        border-radius: 18px;
        background: var(--panel-alt);
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
        min-width: 960px;
      }}
      thead th {{
        text-align: left;
        padding: 14px 12px;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        background: rgba(255, 255, 255, 0.62);
      }}
      tbody td {{
        padding: 12px;
        border-top: 1px solid var(--line);
        vertical-align: top;
        background: rgba(255, 253, 248, 0.92);
      }}
      tbody tr.create-row td {{
        background: #f3ece1;
      }}
      tbody tr.row-active td {{
        background: #fff8ef;
      }}
      .entry-number {{
        display: inline-flex;
        min-width: 40px;
        justify-content: center;
        padding: 7px 10px;
        border-radius: 999px;
        font-weight: 700;
        background: #efe3d1;
      }}
      .tipo-gasto {{
        color: var(--expense);
      }}
      .tipo-ingreso {{
        color: var(--income);
      }}
      .empty {{
        padding: 16px 18px;
        border-top: 1px solid var(--line);
        color: var(--muted);
        background: rgba(255, 253, 248, 0.92);
      }}
      @media (max-width: 840px) {{
        .workspace {{
          grid-template-columns: 1fr;
        }}
        .sidebar {{
          grid-auto-flow: column;
          grid-auto-columns: 1fr;
          align-items: start;
          overflow-x: auto;
        }}
        .content {{
          padding: 20px 14px 32px;
        }}
        .panel {{
          padding: 18px;
          border-radius: 18px;
        }}
        .section-head {{
          flex-direction: column;
          align-items: start;
        }}
      }}
    </style>
  </head>
  <body>
    <div class="workspace">
      <aside class="sidebar" aria-label="Navegacion principal del administrador">
        <div class="brand">Conta Acequia</div>
        <a class="nav-item active" href="{public_base_path or '/'}">
          <span class="nav-icon" aria-hidden="true">LA</span>
          <span>Libro</span>
        </a>
        <a class="nav-item" href="{public_base_path or '/'}#resumen">
          <span class="nav-icon" aria-hidden="true">RS</span>
          <span>Resumen</span>
        </a>
        <a class="nav-item" href="{public_base_path or '/'}#recordatorios">
          <span class="nav-icon" aria-hidden="true">RM</span>
          <span>Record.</span>
        </a>
      </aside>
      <main class="content">
        <section class="hero">
          <p class="eyebrow">Operativa contable diaria</p>
          <h1>Libro de asientos editable</h1>
          <p class="lead">
            Registra y corrige movimientos directamente en una tabla tipo hoja de calculo.
            Cada asiento muestra su numero correlativo por ejercicio para mantener trazabilidad anual.
          </p>
        </section>
        <section class="panel" id="resumen">
          <div class="section-head">
            <div>
              <h2>Consulta del libro</h2>
              <p>Filtra por rango de fechas cuando necesites acotar la revision del ejercicio.</p>
            </div>
          </div>
          {_render_message(success_message, "success")}
          {_render_message(storage_error, "error-banner")}
          <form method="get" action="{public_base_path or '/'}" class="filters">
            <div class="grid">
              {_render_input("fecha_desde", "Desde", "date", filter_data, error_map)}
              {_render_input("fecha_hasta", "Hasta", "date", filter_data, error_map)}
            </div>
            <div class="table-actions">
              <button type="submit">Filtrar libro</button>
              <a class="link" href="{public_base_path or '/'}">Limpiar filtros</a>
            </div>
          </form>
          {_render_movimientos_sheet(
              movimientos,
              form_data,
              filter_data,
              error_map,
              active_form,
              public_base_path,
          )}
        </section>
      </main>
    </div>
  </body>
</html>"""
    return [html.encode("utf-8")]


def _render_message(message: str | None, css_class: str) -> str:
    if not message:
        return ""
    return f'<div class="message {css_class}">{escape(message)}</div>'


def _render_storage_error_page(
    start_response: Callable,
    public_base_path: str,
    storage_error: str,
    form_data: dict[str, str] | None = None,
    filter_data: dict[str, str] | None = None,
    active_form: str = "create",
) -> list[bytes]:
    return _render_page(
        start_response,
        service=_UnavailableMovimientoService(storage_error),
        form_data=form_data,
        filter_data=filter_data,
        active_form=active_form,
        public_base_path=public_base_path,
        status="503 Service Unavailable",
        storage_error=storage_error,
    )


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


def _render_movimientos_sheet(
    movimientos: list,
    form_data: dict[str, str],
    filter_data: dict[str, str],
    error_map: dict[str, str],
    active_form: str,
    public_base_path: str,
) -> str:
    create_form = _resolve_create_form_data(form_data, active_form)
    forms = [
        _render_table_form("create-form", public_base_path, "create", "", filter_data),
        '<div class="sheet"><table aria-label="Libro de asientos editable">',
        (
            "<thead><tr>"
            "<th>Asiento</th>"
            "<th>Fecha</th>"
            "<th>Concepto</th>"
            "<th>Categoria</th>"
            "<th>Tipo</th>"
            "<th>Importe</th>"
            "<th>Accion</th>"
            "</tr></thead><tbody>"
        ),
        _render_create_row(create_form, error_map if active_form == "create" else {}, filter_data),
    ]

    if not movimientos:
        empty_message = (
            "No hay movimientos en el rango indicado."
            if filter_data.get("fecha_desde") or filter_data.get("fecha_hasta")
            else "Todavia no hay movimientos registrados."
        )
        forms.append(
            f'<tr><td class="empty" colspan="7"><strong>{escape(empty_message)}</strong></td></tr>'
        )
    else:
        for movimiento in movimientos:
            row_form_id = f"edit-{movimiento.identificador}"
            row_errors = (
                error_map
                if active_form == f"edit:{movimiento.identificador}"
                else {}
            )
            row_data = _resolve_row_form_data(movimiento, form_data, active_form)
            forms.append(_render_table_form(row_form_id, public_base_path, "update", movimiento.identificador, filter_data))
            forms.append(
                _render_movimiento_row(
                    movimiento,
                    row_form_id,
                    row_data,
                    row_errors,
                    active_form == f"edit:{movimiento.identificador}",
                )
            )

    forms.append("</tbody></table></div>")
    return "".join(forms)


def _render_table_form(
    form_id: str,
    public_base_path: str,
    action: str,
    identificador: str,
    filter_data: dict[str, str],
) -> str:
    return (
        f'<form id="{escape(form_id)}" method="post" action="{public_base_path or "/"}">'
        f'<input type="hidden" name="action" value="{escape(action)}">'
        f'<input type="hidden" name="identificador" value="{escape(identificador)}">'
        f'<input type="hidden" name="fecha_desde" value="{escape(filter_data.get("fecha_desde", ""))}">'
        f'<input type="hidden" name="fecha_hasta" value="{escape(filter_data.get("fecha_hasta", ""))}">'
        "</form>"
    )


def _render_create_row(
    form_data: dict[str, str],
    error_map: dict[str, str],
    filter_data: dict[str, str],
) -> str:
    return (
        '<tr class="create-row">'
        '<td><span class="entry-number">Nuevo</span></td>'
        f'<td>{_render_table_input("fecha", "date", form_data, error_map, "create-form")}</td>'
        f'<td>{_render_table_input("concepto", "text", form_data, error_map, "create-form", placeholder="Nuevo asiento")}</td>'
        f'<td>{_render_table_input("categoria", "text", form_data, error_map, "create-form", placeholder="Categoria")}</td>'
        f'<td>{_render_table_select(form_data, error_map, "create-form")}</td>'
        f'<td>{_render_table_input("importe", "number", form_data, error_map, "create-form", step="0.01", min="0.01", placeholder="0.00")}</td>'
        f'<td><button type="submit" form="create-form">Anadir asiento</button>{_render_hidden_filter_hint(filter_data)}</td>'
        "</tr>"
    )


def _render_movimiento_row(
    movimiento,
    form_id: str,
    form_data: dict[str, str],
    error_map: dict[str, str],
    is_active: bool,
) -> str:
    row_class = "row-active" if is_active else ""
    tipo_css = f"tipo-{escape(form_data.get('tipo', movimiento.tipo))}"
    return (
        f'<tr class="{row_class}">'
        f'<td><span class="entry-number">{movimiento.numero_asiento}</span></td>'
        f'<td>{_render_table_input("fecha", "date", form_data, error_map, form_id)}</td>'
        f'<td>{_render_table_input("concepto", "text", form_data, error_map, form_id)}</td>'
        f'<td>{_render_table_input("categoria", "text", form_data, error_map, form_id)}</td>'
        f'<td><span class="{tipo_css}">{_render_table_select(form_data, error_map, form_id)}</span></td>'
        f'<td>{_render_table_input("importe", "number", form_data, error_map, form_id, step="0.01", min="0.01")}</td>'
        f'<td><button type="submit" form="{escape(form_id)}">Guardar</button></td>'
        "</tr>"
    )


def _render_table_input(
    field: str,
    input_type: str,
    form_data: dict[str, str],
    error_map: dict[str, str],
    form_id: str,
    **attrs: str,
) -> str:
    extra = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    error = error_map.get(field, "")
    return (
        f'<input class="table-input" type="{input_type}" name="{field}" value="{escape(form_data.get(field, ""))}" '
        f'form="{escape(form_id)}" {extra}>'
        f'<span class="error">{escape(error)}</span>'
    )


def _render_table_select(
    form_data: dict[str, str],
    error_map: dict[str, str],
    form_id: str,
) -> str:
    selected = form_data.get("tipo", "")
    options = []
    for value, label in (("", "Selecciona"), ("gasto", "Gasto"), ("ingreso", "Ingreso")):
        is_selected = ' selected="selected"' if value == selected else ""
        options.append(f'<option value="{value}"{is_selected}>{label}</option>')
    error = error_map.get("tipo", "")
    return (
        f'<select class="table-input" name="tipo" form="{escape(form_id)}">{"".join(options)}</select>'
        f'<span class="error">{escape(error)}</span>'
    )


def _render_hidden_filter_hint(filter_data: dict[str, str]) -> str:
    if not filter_data.get("fecha_desde") and not filter_data.get("fecha_hasta"):
        return ""
    return '<span class="error">La alta mantiene el filtro actual tras guardar.</span>'


def _resolve_create_form_data(form_data: dict[str, str], active_form: str) -> dict[str, str]:
    if active_form == "create":
        return {
            "fecha": form_data.get("fecha", ""),
            "concepto": form_data.get("concepto", ""),
            "categoria": form_data.get("categoria", ""),
            "tipo": form_data.get("tipo", ""),
            "importe": form_data.get("importe", ""),
        }
    return {"fecha": "", "concepto": "", "categoria": "", "tipo": "", "importe": ""}


def _resolve_row_form_data(movimiento, form_data: dict[str, str], active_form: str) -> dict[str, str]:
    if active_form == f"edit:{movimiento.identificador}":
        return {
            "fecha": form_data.get("fecha", movimiento.fecha),
            "concepto": form_data.get("concepto", movimiento.concepto),
            "categoria": form_data.get("categoria", movimiento.categoria),
            "tipo": form_data.get("tipo", movimiento.tipo),
            "importe": form_data.get("importe", format(movimiento.importe, ".2f")),
        }
    return {
        "fecha": movimiento.fecha,
        "concepto": movimiento.concepto,
        "categoria": movimiento.categoria,
        "tipo": movimiento.tipo,
        "importe": format(movimiento.importe, ".2f"),
    }


def _parse_filter_data(raw_data: dict[str, str]) -> dict[str, str]:
    return {
        "fecha_desde": raw_data.get("fecha_desde", "").strip(),
        "fecha_hasta": raw_data.get("fecha_hasta", "").strip(),
    }


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


def _parse_form_data(raw_data: str) -> dict[str, str]:
    return {key: values[0] for key, values in parse_qs(raw_data, keep_blank_values=True).items()}


class _UnavailableMovimientoService:
    def __init__(self, storage_error: str) -> None:
        self._storage_error = storage_error

    def listar_movimientos(
        self,
        fecha_desde: str = "",
        fecha_hasta: str = "",
    ) -> tuple[list, list[ValidationError]]:
        return [], []
