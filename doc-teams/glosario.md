# Glosario

## `main`
Rama de referencia del repositorio. Para `doc-teams`, la documentacion se actualiza directamente sobre esta rama.

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
Lista priorizada de trabajo funcional o tecnico. En el estado actual, `product-manager/product-backlog.md` esta poblado y actua como fuente de trazabilidad.

## Vision del producto
Descripcion de alto nivel del objetivo de negocio y del problema que resuelve la aplicacion.

## Dependencia abierta
Elemento o decision que todavia bloquea una documentacion mas precisa o una entrega funcional completa.

## Handoff
Comentario estructurado que un rol publica para transferir trabajo a otro rol sin perder trazabilidad.
