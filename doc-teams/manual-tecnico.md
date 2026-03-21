# Manual tecnico

## Publico objetivo
Equipo tecnico, soporte interno y cualquier persona que necesite entender la estructura y las limitaciones verificables del repositorio.

## Alcance
Este manual documenta la organizacion tecnica visible en el arbol de trabajo y las restricciones operativas que se derivan de ese estado.
No inventa una arquitectura de aplicacion si no hay artefactos verificables en el repositorio revisado.

## Estado tecnico verificado
- El repositorio contiene documentacion funcional, reglas de proceso y scripts de apoyo.
- `product-manager/product-backlog.md` ya no esta vacio y funciona como fuente de trazabilidad funcional.
- En esta revision no se han encontrado codigo de aplicacion, pruebas automatizadas ni manifiestos de despliegue en el arbol visible.
- Existe una contradiccion documental pendiente de resolver: el `changelog/2026-03-21.md` describe una entrega tecnica en Python, pero esa base no se observa en el arbol de trabajo actual.

## Estructura relevante
- `product-manager/`: vision funcional, backlog, historias de usuario, casos de uso y refinamiento.
- `doc-teams/`: manuales y guias mantenidas por el equipo de documentacion.
- `agile-coach/`: acuerdos operativos, analisis de proceso y riesgos de coordinacion.
- `run-codex.sh`: envoltorio para ejecutar Codex con el entorno local preparado.
- `*_rol-*.sh`: lanzadores de prompts por rol.

## Scripts de operacion local
### `run-codex.sh`
El script espera:
- Un fichero `.env` en la raiz del repositorio.
- Una variable `GITHUB_PAT` disponible tras cargar `.env`.
- Un entorno virtual Python en `.venv/bin/activate`.

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
Los siguientes requisitos se deducen de los scripts visibles, no de una aplicacion productiva ya instalada:
- Bash compatible con `set -euo pipefail`.
- `codex` disponible en el `PATH`.
- Un entorno virtual Python ya creado.
- Un token personal de GitHub en `GITHUB_PAT`.

## Dependencias tecnicas abiertas
- Falta una base ejecutable visible para documentar backend, frontend o persistencia real.
- Falta una referencia de pruebas tecnicas que permita describir comandos de validacion de aplicacion.
- Falta sincronizar el relato del `changelog` con el arbol de trabajo para decidir que version del producto es la vigente.

## Recomendacion tecnica
Antes de documentar instalacion, despliegue o soporte de usuario final, conviene disponer de una base ejecutable integrada en `main` y validada por QA.
Hasta entonces, la documentacion tecnica debe tratar este repositorio como un armazon documental y operacional.
