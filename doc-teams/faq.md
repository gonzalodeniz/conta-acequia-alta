# Preguntas frecuentes

## Por donde empiezo a leer el repositorio?
Empieza por `README.md`, luego revisa `product-manager/vision-product.md` y `product-manager/product-backlog.md`. A partir de ahi, entra en los manuales de `doc-teams/` segun si buscas informacion de usuario, tecnica o administracion.

## Esta listo el producto para usuarios finales?
No aun. Existe una primera entrega ejecutable para registrar movimientos, pero el producto completo sigue incompleto y con varias capacidades en backlog.

## Donde esta la fuente de verdad funcional?
En `product-manager/`, especialmente en `vision-product.md`, `product-backlog.md`, `historias-de-usuario.md` y `casos-de-uso.md`.

## El backlog esta vacio?
No. `product-manager/product-backlog.md` contiene PB-001, PB-002, PB-003, PB-004, PB-005, PB-006, PB-007 y PB-008.

## Que tipo de contenido mantiene `doc-teams`?
Manual de usuario, manual tecnico, manual de administracion y guias operativas como instalacion o despliegue cuando existan bases verificables para hacerlo.

## Puedo asumir que hay una app desplegable?
Si hay una aplicacion WSGI minima para uso local con `python3 app.py` o `make run`, pero no un despliegue de produccion verificado.

## Como se usan los scripts `*_rol-*.sh`?
Cada script lanza el prompt del rol correspondiente mediante `run-codex.sh`. Son utilidades de coordinacion, no la aplicacion del dominio de negocio.

## Que falta para una documentacion funcional mas completa?
- Cerrar o validar PB-002 y PB-003 para que la consulta y el resumen pasen de vision a funcionalidad documentada.
- Definir el alcance real de vecinos en solo lectura.
- Confirmar el formato de importacion, el cierre anual y las notificaciones antes de documentarlos como operativos.
- Definir una guia de despliegue de produccion cuando exista una base tecnica para ello.

## Hay contradicciones en la documentacion?
Si. La principal contradiccion que se ha corregido aqui era entre una lectura antigua del repositorio como solo documental y la presencia real de una aplicacion minima en Python junto con su suite de tests.
