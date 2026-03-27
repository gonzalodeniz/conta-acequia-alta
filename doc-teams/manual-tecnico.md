# Manual tecnico

## Publico objetivo
Equipo tecnico, soporte interno y cualquier persona que necesite entender la estructura y las limitaciones verificables del repositorio.

## Alcance
Este manual documenta la base tecnica real visible en el arbol de trabajo.
No inventa arquitectura ni dependencias externas que no esten respaldadas por los ficheros del repositorio.

## Estado tecnico verificado
- Existe una aplicacion WSGI minima en Python en `app.py`.
- El paquete `conta_acequia_alta/` contiene modelos, repositorio, servicio y capa web.
- Los tests automaticos viven en `tests/test_app.py`, `tests/test_service.py` y `tests/test_web.py`.
- La persistencia de datos usa `data/movimientos.json`.
- `requirements.txt` existe, pero por ahora no declara dependencias externas.
- La aplicacion valida campos obligatorios, formato de fecha, tipo de movimiento e importe positivo.
- La vista web actual es unica y sirve para alta y actualizacion inline del libro persistido, con filtro opcional por rango de fechas.
- La numeracion de asientos se calcula por ejercicio anual y se muestra en la propia tabla.
- La entrega de `PB-010` ya esta integrada en `main`; este manual describe el comportamiento vigente y no una dependencia abierta.
- La configuracion de ejecucion se resuelve desde `HOST`, `PORT` y `BASE_PATH` leidos primero del entorno y despues de `.env`, con valores por defecto `127.0.0.1`, `8000` y raiz sin subruta.
- Si la ruta solicitada no coincide con el `BASE_PATH` configurado, la aplicacion responde `404 Not Found`.
- Si el fichero de datos no existe, se crea automaticamente como un array JSON vacio.
- Si el fichero de datos esta corrupto o no puede escribirse, la aplicacion responde con `503 Service Unavailable` y devuelve un mensaje explicito.

## Estructura relevante
- `app.py`: punto de entrada para levantar el servidor WSGI local.
- `conta_acequia_alta/models.py`: entidad `Movimiento` y conversion a y desde diccionario.
- `conta_acequia_alta/repository.py`: lectura y escritura JSON en `data/movimientos.json`.
- `conta_acequia_alta/service.py`: validacion de negocio y creacion de movimientos.
- `conta_acequia_alta/web.py`: render HTML y logica WSGI.
- `tests/`: cobertura basica de configuracion, servicio y vista web.
- `product-manager/`: fuente de verdad funcional y trazabilidad de producto.
- `doc-teams/`: manuales y guias mantenidas por documentacion.

## Flujo tecnico
1. La peticion entra por `create_app()` en `conta_acequia_alta/web.py`.
2. La capa web instancia `MovimientoRepository` y `MovimientoService`.
3. La capa web resuelve la ruta publica usando `SCRIPT_NAME` y el `BASE_PATH` configurado.
4. El servicio valida el payload.
5. Si la validacion pasa, se genera un identificador `MOV-XXXXXXXX`.
6. El repositorio persiste el movimiento en `data/movimientos.json`.
7. La vista renderiza el libro de asientos en orden cronologico ascendente, con el filtrado aplicado si existe rango de fechas y con numeracion anual calculada sobre los movimientos visibles.

## Validaciones implementadas
- `fecha` es obligatoria y debe usar formato `AAAA-MM-DD`.
- `concepto` es obligatorio.
- `categoria` es obligatoria.
- `tipo` es obligatorio y solo acepta `gasto` o `ingreso`.
- `importe` es obligatorio, debe ser numerico y mayor que cero.
- Si se actualiza un movimiento y cambia de ejercicio anual, la numeracion visible se recalcula dentro del ejercicio de destino.

## Comportamiento de persistencia
- Si `data/movimientos.json` no existe, el repositorio lo crea automaticamente con un array vacio.
- Cada alta reescribe el fichero completo con la lista serializada.
- Los datos se guardan en JSON legible para facilitar inspeccion manual y restauracion.
- Una lectura o escritura fallida se convierte en `StorageError` para que la capa web pueda devolver un `503` controlado.

## Comandos utiles
- `python3 -m venv .venv`: crea el entorno virtual de trabajo en la raiz del repositorio.
- `source .venv/bin/activate`: activa el entorno virtual en Bash o Zsh antes de instalar o ejecutar comandos.
- `python -m pip install --upgrade pip`: actualiza `pip` dentro del entorno antes de instalar dependencias.
- `make run`: arranca la aplicacion local con el servidor WSGI de la libreria estandar.
- `make test`: ejecuta la suite de `unittest`.
- `python3 app.py`: alternativa directa para iniciar la aplicacion.
- `python3 -m unittest discover -s tests -v`: ejecucion explicita de los tests.

## Verificacion recomendada
1. Ejecutar `make test`.
2. Arrancar `make run`.
3. Abrir `http://127.0.0.1:8000`.
4. Registrar un movimiento valido.
5. Comprobar que el identificador aparece en la confirmacion y en la lista inferior.
6. Probar un envio invalido para verificar la respuesta de validacion.

## Dependencias tecnicas abiertas
- Falta implementar busqueda, resumen financiero, importacion, presupuestos y cierre anual.
- Falta definir autenticacion y permisos si el producto va a distinguir administradores de vecinos.
- Falta decidir una estrategia de despliegue distinta del servidor local de desarrollo.
- No existe capa de API separada ni almacenamiento alternativo al fichero JSON local.
- Falta completar la ayuda de clasificacion contable descrita en `product-manager/requisitos-funcionales.md`.
- La ayuda de clasificacion contable sigue siendo una dependencia funcional abierta y no debe confundirse con la edicion inline ya integrada.

## Scripts de soporte
### `run-codex.sh`
El script sigue siendo util para orquestacion del entorno local de trabajo del repositorio.
No forma parte de la aplicacion de contabilidad.

### Lanzadores de rol
- `1_rol-product-manager.sh`
- `2_rol-developer-teams.sh`
- `3_rol-qa-teams.sh`
- `4_rol-doc-teams.sh`
- `5_rol-agile-coach.sh`

Cada lanzador invoca el prompt del rol correspondiente mediante `run-codex.sh`.

## Recomendacion tecnica
La base actual ya permite documentar instalacion local, pruebas y operacion minima.
Cuando desarrollo entregue nuevas capacidades y estas queden validadas en `main`, este manual debera ampliarse con los flujos adicionales.
