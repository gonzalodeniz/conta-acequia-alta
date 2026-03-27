# Glosario

## `main`
Rama de referencia del repositorio. Para `doc-teams`, la documentacion se actualiza directamente sobre esta rama.

## `WSGI`
Interfaz estandar de Python usada por la aplicacion minima del repositorio para atender peticiones web locales.

## `app.py`
Punto de entrada de la aplicacion minima. Arranca un servidor local en `127.0.0.1:8000`.

## `PORT`
Variable de entorno usada por `app.py` para cambiar el puerto de escucha. Tambien puede leerse desde `.env`.

## `HOST`
Variable de entorno usada por `app.py` para definir la interfaz de escucha. Tambien puede leerse desde `.env`.

## `BASE_PATH`
Subruta publica opcional usada por `app.py` para desplegar la aplicacion bajo un prefijo concreto.

## `data/movimientos.json`
Fichero JSON donde la entrega actual persiste los movimientos contables registrados.

## `503 Service Unavailable`
Respuesta HTTP que la aplicacion devuelve cuando no puede leer o guardar el fichero de datos de movimientos.

## `Movimiento`
Entidad funcional que representa un gasto o ingreso con identificador, fecha, concepto, categoria, tipo e importe.

## `Libro de asientos editable`
Vista unica de la aplicacion donde el administrador puede crear o actualizar movimientos directamente en una tabla, sin formulario independiente de alta.

## `numero_asiento`
Numero correlativo mostrado en la tabla para cada movimiento dentro de su ejercicio anual. Se reinicia al comenzar un nuevo ano contable.

## `product-manager`
Rol responsable de la vision funcional, el backlog y la definicion de producto.

## `developer-teams`
Rol responsable de implementar la funcionalidad tecnica y de entregar la base verificable del producto.

## `qa-teams`
Rol responsable de validar funcionalmente las entregas antes de su integracion final.

## `doc-teams`
Rol responsable de crear y mantener manuales, guias y documentacion transversal.

## `changelog/`
Directorio donde se registra el resumen cronologico de actividad por rol.

## `Estado operativo`
Campo comun usado en issues y comentarios para indicar el estado real de una entrega o una transicion de trabajo.

## `Impacto documental`
Campo del handoff tecnico que indica si una entrega requiere actualizacion de documentacion.

## `GITHUB_PAT`
Token personal de GitHub que `run-codex.sh` espera cargar desde `.env`.

## `.env`
Fichero local con variables de entorno para ejecutar los scripts de soporte.

## `.venv`
Entorno virtual Python esperado por `run-codex.sh`.

## Backlog
Lista priorizada de trabajo funcional o tecnico. En el estado actual, `product-manager/product-backlog.md` esta poblado y actua como fuente de trazabilidad funcional.

## Vision del producto
Descripcion de alto nivel del objetivo de negocio y del problema que resuelve la aplicacion.

## Dependencia abierta
Elemento o decision que todavia bloquea una documentacion mas precisa o una entrega funcional completa.

## Handoff
Comentario estructurado que un rol publica para transferir trabajo a otro rol sin perder trazabilidad.
