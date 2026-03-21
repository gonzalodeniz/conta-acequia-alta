# Manual tecnico

## Publico objetivo
Equipo tecnico, soporte interno y cualquier persona que necesite entender la estructura actual del repositorio.

## Alcance
Este manual documenta la organizacion tecnica visible en el repositorio y las restricciones operativas que se derivan del estado actual.

## Estado tecnico actual
- El repositorio no contiene una aplicacion web desplegable.
- No hay codigo de backend, frontend, base de datos ni pipeline de despliegue identificado en la rama `main`.
- El contenido visible se compone principalmente de documentos, scripts de apoyo y reglas operativas de roles.

## Estructura relevante
- `product-manager/`: vision funcional, prompt de rol y backlog de producto.
- `doc-teams/`: instrucciones y documentacion de referencia para el equipo de documentacion.
- `agile-coach/`: acuerdos operativos, metricas y riesgos de coordinacion.
- `run-codex.sh`: wrapper para ejecutar Codex con el entorno local preparado.
- `*_rol-*.sh`: lanzadores de prompts por rol.

## Scripts de operacion local
### `run-codex.sh`
El script espera:
- Un fichero `.env` en la raiz del repositorio.
- Una variable `GITHUB_PAT` disponible tras cargar `.env`.
- Un entorno virtual en `.venv/bin/activate`.

Si falta alguno de esos elementos, el script detiene la ejecucion con un mensaje explicito.

### Lanzadores de rol
- `1_rol-product-manager.sh`
- `2_rol-developer-teams.sh`
- `3_rol-qa-teams.sh`
- `4_rol-doc-teams.sh`
- `5_rol-agile-coach.sh`

Cada lanzador:
- Comprueba que existe el prompt del rol correspondiente.
- Asegura permisos de ejecucion sobre `run-codex.sh` si fuera necesario.
- Invoca `run-codex.sh` con el modelo definido para ese rol.

## Requisitos tecnicos inferidos
Los siguientes requisitos se deducen del contenido de los scripts, no de una aplicacion productiva ya instalada:
- Bash compatible con `set -euo pipefail`.
- `codex` disponible en el `PATH`.
- Un entorno virtual Python ya creado.
- Un token personal de GitHub en `GITHUB_PAT`.

## Contradicciones o huecos detectados
- La vision del producto describe una aplicacion web para gestion contable, pero el repositorio visible no incluye esa implementacion.
- `README.md` y `Makefile` aparecen vacios en la revision del repositorio, asi que no existe una guia tecnica de arranque del producto.
- `product-manager/product-backlog.md` esta vacio, por lo que falta trazabilidad funcional hacia desarrollo.

## Recomendacion tecnica
Antes de documentar instalacion, despliegue o soporte de usuario final, conviene que desarrollo entregue una base ejecutable y que QA la valide. Hasta entonces, la documentacion tecnica debe tratar este repositorio como un armazon documental y operacional, no como un sistema en produccion.
