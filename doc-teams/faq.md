# Preguntas frecuentes

## Por donde empiezo a leer el repositorio?
Empieza por `README.md`, luego revisa `product-manager/vision-product.md` y `product-manager/product-backlog.md`. A partir de ahi, entra en los manuales de `doc-teams/` segun si buscas informacion de usuario, tecnica o administracion.

## Esta listo el producto para usuarios finales?
No aun. Existe una primera entrega ejecutable para registrar movimientos, pero el producto completo sigue incompleto y con varias capacidades en backlog.

## Donde esta la fuente de verdad funcional?
En `product-manager/`, especialmente en `vision-product.md`, `product-backlog.md`, `historias-de-usuario.md` y `casos-de-uso.md`.

## El backlog esta vacio?
No. `product-manager/product-backlog.md` contiene PB-001, PB-002, PB-003, PB-004, PB-005, PB-006, PB-007 y PB-008.

## Que hace la aplicacion actual?
Permite registrar y actualizar movimientos de gasto o ingreso directamente en el libro de asientos de una unica pagina. Hay filtro por rango de fechas, numeracion anual visible y persistencia local, pero no hay resumen financiero, autenticacion ni perfiles de acceso separados.

## Como cambio el puerto de ejecucion?
Define `HOST`, `PORT` o `BASE_PATH` en el entorno o en un fichero `.env` en la raiz. Si no lo haces, la aplicacion usa `127.0.0.1`, `8000` y la raiz del sitio.

## Como filtro el libro de asientos?
Usa los campos `Desde` y `Hasta` del formulario de consulta. Ambos aceptan fechas en formato `AAAA-MM-DD`.

## Que pasa si el fichero de datos falla?
La aplicacion responde con `503 Service Unavailable` si `data/movimientos.json` esta corrupto o no puede escribirse. En ese caso conviene revisar el fichero o restaurar una copia valida.

## Que tipo de contenido mantiene `doc-teams`?
Manual de usuario, manual tecnico, manual de administracion y guias operativas como instalacion o despliegue cuando existan bases verificables para hacerlo.

## Puedo asumir que hay una app desplegable?
Si hay una aplicacion WSGI minima para uso local con `python3 app.py` o `make run`, pero no un despliegue de produccion verificado.

## Puedo servirla bajo una subruta?
Si, la base actual interpreta `BASE_PATH` y tambien respeta `SCRIPT_NAME` cuando no se ha configurado una subruta fija. Sigue siendo una capacidad de ejecucion local, no una guia de produccion.

## Como se usan los scripts `*_rol-*.sh`?
Cada script lanza el prompt del rol correspondiente mediante `run-codex.sh`. Son utilidades de coordinacion, no la aplicacion del dominio de negocio.

## Que falta para una documentacion funcional mas completa?
- Validar PB-003 para que el resumen financiero pase de vision a funcionalidad documentada.
- Definir el alcance real de vecinos en solo lectura.
- Confirmar el formato de importacion, el cierre anual y las notificaciones antes de documentarlos como operativos.
- Definir una guia de despliegue de produccion cuando exista una base tecnica para ello.
- Alinear cualquier futura guia de administracion con el alcance real integrado en `main` antes de describirlo como vigente.

## Si una issue esta validada, por que el manual sigue sin describirla como vigente?
Porque `doc-teams` documenta el comportamiento integrado en `main`. Si la validacion existe pero la rama tecnica todavia no se ha fusionado, la documentacion debe seguir describiendo el estado vigente y dejar esa entrega como dependencia abierta.

## Hay contradicciones en la documentacion?
Si. La principal contradiccion que se ha corregido aqui era entre una lectura antigua del repositorio como solo documental y la presencia real de una aplicacion minima en Python junto con su suite de tests.
