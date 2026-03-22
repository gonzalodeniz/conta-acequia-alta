# Manual tecnico

## Publico objetivo
Equipo tecnico, soporte interno y cualquier persona que necesite entender la estructura y las limitaciones verificables del repositorio.

## Alcance
Este manual documenta la base tecnica real visible en el arbol de trabajo.
No inventa arquitectura ni dependencias externas que no esten respaldadas por los ficheros del repositorio.

## Estado tecnico verificado
- Existe una aplicacion WSGI minima en Python en `app.py`.
- El paquete `conta_acequia_alta/` contiene modelos, repositorio, servicio y capa web.
- Los tests automaticos viven en `tests/test_service.py` y `tests/test_web.py`.
- La persistencia de datos usa `data/movimientos.json`.
- `requirements.txt` existe, pero por ahora no declara dependencias externas.
- La aplicacion valida campos obligatorios, formato de fecha, tipo de movimiento e importe positivo.
- La vista web actual es unica y sirve tanto para alta como para consulta del ultimo estado persistido.

## Estructura relevante
- `app.py`: punto de entrada para levantar el servidor WSGI local.
- `conta_acequia_alta/models.py`: entidad `Movimiento` y conversion a y desde diccionario.
- `conta_acequia_alta/repository.py`: lectura y escritura JSON en `data/movimientos.json`.
- `conta_acequia_alta/service.py`: validacion de negocio y creacion de movimientos.
- `conta_acequia_alta/web.py`: render HTML y logica WSGI.
- `tests/`: cobertura basica de servicio y vista web.
- `product-manager/`: fuente de verdad funcional y trazabilidad de producto.
- `doc-teams/`: manuales y guias mantenidas por documentacion.

## Flujo tecnico
1. La peticion entra por `create_app()` en `conta_acequia_alta/web.py`.
2. La capa web instancia `MovimientoRepository` y `MovimientoService`.
3. El servicio valida el payload.
4. Si la validacion pasa, se genera un identificador `MOV-XXXXXXXX`.
5. El repositorio persiste el movimiento en `data/movimientos.json`.
6. La vista renderiza la lista de movimientos en orden inverso de insercion.

## Comandos utiles
- `make run`: arranca la aplicacion local con el servidor WSGI de la libreria estandar.
- `make test`: ejecuta la suite de `unittest`.
- `python3 app.py`: alternativa directa para iniciar la aplicacion.
- `python3 -m unittest discover -s tests -v`: ejecucion explicita de los tests.

## Reglas de validacion actuales
- `fecha` es obligatoria y debe usar formato `AAAA-MM-DD`.
- `concepto` es obligatorio.
- `categoria` es obligatoria.
- `tipo` es obligatorio y solo acepta `gasto` o `ingreso`.
- `importe` es obligatorio, debe ser numerico y mayor que cero.

## Persistencia
- El fichero de datos es `data/movimientos.json`.
- Si el fichero no existe, el repositorio lo crea con un array vacio.
- Cada alta vuelve a escribir el fichero completo con la lista serializada.
- La informacion persiste en formato JSON legible.

## Dependencias tecnicas abiertas
- Falta implementar busqueda, filtrado, resumen financiero, importacion, presupuestos y cierre anual.
- Falta definir autenticacion y permisos si el producto va a distinguir administradores de vecinos.
- Falta decidir una estrategia de despliegue distinta del servidor local de desarrollo.

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
