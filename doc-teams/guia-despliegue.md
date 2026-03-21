# Guia de despliegue

## Publico objetivo
Equipo tecnico y administracion que necesiten entender como se publica o expone el contenido del repositorio.

## Estado actual
- No existe una aplicacion web desplegable documentada en el repositorio.
- No se observa pipeline de despliegue ni destino de produccion para la app.
- El flujo vigente es documental: cambios en `main`, commit en espanol y sincronizacion con el remoto.

## Despliegue de la documentacion
En el estado actual, la forma efectiva de "publicar" cambios es:
1. Modificar los documentos correspondientes.
2. Hacer commit en `main`.
3. Enviar los cambios al remoto.

Eso deja el contenido disponible para el resto de roles y para futuras revisiones.

## Despliegue de aplicacion
No documentado.

Motivos:
- No hay artefactos de aplicacion visibles.
- No existe evidencia de configuracion de servidor, contenedores, servicios o infraestructura.
- No es responsable inventar una estrategia de despliegue sin una base tecnica real.

## Dependencias abiertas
- Falta una definicion tecnica de la arquitectura de la futura aplicacion.
- Falta un backlog funcional que permita enlazar despliegues con entregas validables.
- Falta una referencia de entorno objetivo para produccion, pruebas o preproduccion.

## Recomendacion
Cuando desarrollo entregue una version ejecutable, esta guia debera ampliarse con:
- Preparacion del entorno objetivo.
- Pasos de despliegue por entorno.
- Variables de configuracion.
- Verificacion postdespliegue.
- Procedimiento de rollback.
