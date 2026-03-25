# Guia de despliegue

## Publico objetivo
Equipo tecnico y administracion que necesiten entender como se publica o expone la entrega minima del repositorio.

## Estado actual
- Existe una aplicacion WSGI minima ejecutable con `python3 app.py` o `make run`.
- El servidor que levanta la base actual es el servidor local de la libreria estandar.
- No se observa pipeline de despliegue ni destino de produccion documentado.
- El flujo vigente y comprobable sigue siendo: cambios en `main`, commit en espanol y sincronizacion con el remoto.
- La aplicacion escucha en `127.0.0.1` y usa `8000` por defecto, salvo configuracion de `HOST` o `PORT` en el entorno o en `.env`.
- La aplicacion admite una subruta publica opcional mediante `BASE_PATH`.

## Despliegue local
En el estado actual, la forma efectiva de exponer la aplicacion es:
1. Modificar el codigo o la documentacion necesaria.
2. Ejecutar `make test` para comprobar que la entrega sigue estable.
3. Arrancar `make run` o `python3 app.py`.
4. Abrir `http://127.0.0.1:8000` en un navegador, o la ruta equivalente si se definio `HOST`, `PORT` o `BASE_PATH`.

Eso deja la aplicacion disponible solo en local para pruebas y uso de desarrollo.

## Verificacion posterior
- Comprobar que la pagina carga y permite registrar un movimiento valido.
- Verificar que el nuevo movimiento aparece en la lista inferior.
- Confirmar que el fichero `data/movimientos.json` fue actualizado si se ejecuto una alta.
- Revisar que una ruta equivocada responde `404 Not Found` y que un fallo de almacenamiento responde `503 Service Unavailable`.

## Despliegue de produccion
No documentado.

Motivos:
- No hay evidencia de contenedor, servicio systemd, proxy inverso o plataforma de hosting.
- No existe una configuracion de variables o secretos para produccion.
- No es responsable inventar una estrategia de despliegue sin una base tecnica real.
- No existe todavia una guia de publicacion por subruta aparte de la ejecucion local con `BASE_PATH`.

## Dependencias abiertas
- Falta una definicion tecnica de la arquitectura de produccion.
- Falta una referencia de entorno objetivo para pruebas, preproduccion o produccion.
- Falta decidir si el despliegue futuro seguira siendo local o si necesitara un proceso de publicacion formal.
- Falta definir si sera necesario un proceso de migracion de datos antes de publicar nuevas versiones.

## Recomendacion
Cuando desarrollo entregue una version destinada a produccion, esta guia debera ampliarse con:
- Preparacion del entorno objetivo.
- Pasos de despliegue por entorno.
- Variables de configuracion.
- Verificacion postdespliegue.
- Procedimiento de rollback.
