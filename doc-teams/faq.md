# Preguntas frecuentes

## Por donde empiezo a leer el repositorio?
Empieza por `README.md`, luego revisa `product-manager/vision-product.md` y `product-manager/product-backlog.md`. A partir de ahi, entra en los manuales de `doc-teams/` segun si buscas informacion de usuario, tecnica o administracion.

## Esta listo el producto para usuarios finales?
No hay evidencia en el arbol de trabajo de una aplicacion web operativa. La vision del producto esta definida, pero la base ejecutable no es verificable aqui.

## Donde esta la fuente de verdad funcional?
En `product-manager/`, especialmente en `vision-product.md`, `product-backlog.md`, `historias-de-usuario.md` y `casos-de-uso.md`.

## El backlog esta vacio?
No. `product-manager/product-backlog.md` contiene PB-001 a PB-007 y sirve como fuente de trazabilidad funcional.

## Que tipo de contenido mantiene `doc-teams`?
Manual de usuario, manual tecnico, manual de administracion y guias operativas como instalacion o despliegue cuando existan bases verificables para hacerlo.

## Puedo asumir que hay una app desplegable?
No. Seria incorrecto documentar como vigente algo que no aparece de forma verificable en el arbol del repositorio revisado.

## Como se usan los scripts `*_rol-*.sh`?
Cada script lanza el prompt del rol correspondiente mediante `run-codex.sh`. Son utilidades de coordinacion, no la aplicacion del dominio de negocio.

## Que falta para una documentacion funcional mas completa?
- Una base ejecutable visible en `main`.
- Evidencia de pruebas tecnicas y validacion funcional.
- Cierre de dependencias abiertas como importacion, visibilidad para vecinos y alcance del cierre anual.
- Aclarar la contradiccion entre el relato de `changelog/` y el arbol de trabajo.

## Hay contradicciones en la documentacion?
Si. La principal contradiccion es entre la vision de una aplicacion web de contabilidad, el changelog que describe una entrega tecnica y el arbol de trabajo actual, que no permite verificar esa base como vigente.
