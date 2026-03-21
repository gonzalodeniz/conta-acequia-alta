# Preguntas frecuentes

## Esta listo el producto para usuarios finales?
No hay evidencia en el repositorio de una aplicacion web operativa. La vision del producto esta definida, pero la implementacion visible no esta completa.

## Donde esta la fuente de verdad funcional?
En `product-manager/`, especialmente en `vision-product.md`. El backlog esta vacio y eso limita la trazabilidad detallada.

## Que tipo de contenido mantiene `doc-teams`?
Manual de usuario, manual tecnico, manual de administracion y guias operativas como instalacion o despliegue cuando existan bases verificables para hacerlo.

## Puedo asumir que hay una app desplegable?
No. Seria incorrecto documentar como vigente algo que no aparece en el arbol del repositorio revisado.

## Como se usan los scripts `*_rol-*.sh`?
Cada script lanza el prompt del rol correspondiente mediante `run-codex.sh`. Son utilidades de coordinacion, no la aplicacion del dominio de negocio.

## Que falta para una documentacion funcional mas completa?
- Backlog de producto poblado.
- Entregas tecnicas validadas en `main`.
- Una base ejecutable del producto.
- Evidencia de pruebas y de flujo operativo real.

## Hay contradicciones en la documentacion?
La principal contradiccion es entre la vision de una aplicacion web de contabilidad y el estado actual del repositorio, que contiene sobre todo documentos y scripts de orquestacion.
