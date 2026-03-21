# Guia de instalacion

## Publico objetivo
Equipo tecnico y personas encargadas de preparar el entorno de trabajo del repositorio.

## Estado de cobertura
Esta guia documenta la preparacion del entorno para usar los scripts de soporte del repositorio. No documenta la instalacion de una aplicacion web porque esa implementacion no esta presente en la revision actual.

## Prerrequisitos
- Bash.
- `git`.
- `codex` instalado y accesible en el `PATH`.
- Entorno virtual Python en `.venv/`.
- Fichero `.env` en la raiz del repositorio.
- Variable `GITHUB_PAT` definida dentro de `.env`.

## Preparacion del entorno
1. Clonar el repositorio.
2. Crear el fichero `.env` en la raiz si no existe.
3. Definir `GITHUB_PAT` en `.env`.
4. Crear el entorno virtual en `.venv/`.
5. Activar el entorno virtual.
6. Verificar que `codex` responde correctamente.

## Verificacion minima
Ejecuta `run-codex.sh` para comprobar que:
- El fichero `.env` existe.
- `GITHUB_PAT` se carga sin errores.
- El entorno virtual esta disponible.

Si falta cualquiera de esos elementos, el script informa del problema y termina.

## Dependencias abiertas
- No existe un fichero `requirements.txt` en la raiz que describa dependencias Python del proyecto.
- No hay una guia de instalacion de la aplicacion final porque la aplicacion no esta presente en el arbol visible.

## Nota operativa
Si en el futuro se incorpora una aplicacion real, esta guia debera ampliarse con:
- Dependencias de sistema.
- Dependencias de Python o JavaScript.
- Procedimientos de migracion o provision de datos.
- Pruebas de verificacion postinstalacion.
