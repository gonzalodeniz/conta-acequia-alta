# Guia de instalacion

## Publico objetivo
Equipo tecnico y personas encargadas de preparar el entorno de trabajo del repositorio.

## Estado de cobertura
Esta guia documenta la instalacion local de la entrega minima actual.
No describe instalacion de produccion porque todavia no hay una estrategia de despliegue final verificada.

## Prerrequisitos
- Python 3 disponible como `python3`.
- `git`.
- Bash.
- Un entorno virtual Python es obligatorio para aislar la ejecucion segun la politica del repositorio.

## Instalacion local
1. Clonar el repositorio.
2. Crear el entorno virtual en la raiz del repositorio con `python3 -m venv .venv`.
3. Activarlo antes de instalar o ejecutar nada:
   - Bash o Zsh: `source .venv/bin/activate`
   - Si usas otro shell, aplica el comando equivalente de activacion.
4. Actualizar `pip` dentro del entorno con `python -m pip install --upgrade pip`.
5. Instalar dependencias con `pip install -r requirements.txt`.
6. Verificar que no hay dependencias externas pendientes, porque el fichero actual no declara paquetes adicionales.
7. Ejecutar la suite tecnica con `make test`.
8. Arrancar la aplicacion con `make run` o `python3 app.py`.

## Verificacion minima
Ejecuta `make test` para comprobar que:
- La logica de servicio valida correctamente movimientos validos e invalidos.
- La vista web responde con estado vacio, alta correcta y errores de validacion.

Ejecuta `make run` para comprobar que:
- La aplicacion levanta un servidor WSGI local.
- El servicio responde en `http://127.0.0.1:8000` salvo que `PORT` o `.env` definan otro valor.
- La ruta raiz muestra el formulario y el listado de movimientos.

## Configuracion de ejecucion
- `PORT` define el puerto de escucha.
- Si existe un fichero `.env` en la raiz, `app.py` tambien toma `PORT` desde ahi.
- Si no se define un puerto, la aplicacion usa `8000`.

## Dependencias abiertas
- No existe una infraestructura de produccion documentada para desplegar la aplicacion.
- El fichero `requirements.txt` no contiene dependencias externas por ahora; si en el futuro se añaden, esta guia debera actualizarse.
- El entorno virtual descrito aqui es obligatorio para trabajar con la entrega actual, aunque no haya dependencias externas declaradas.
- La instalacion aqui descrita es la minima necesaria para trabajar con la entrega actual, no una guia de producto final.

## Nota operativa
Mientras el repositorio siga evolucionando, esta guia debe mantenerse sincronizada con los comandos reales de arranque y pruebas.
