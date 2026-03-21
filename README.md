# conta-acequia-alta

Repositorio de trabajo para la contabilidad de una comunidad de vecinos.

## Que contiene

- Documentacion funcional y de producto en `product-manager/`.
- Manuales y guias operativas en `doc-teams/`.
- Acuerdos de coordinacion y mejora de proceso en `agile-coach/`.
- Scripts de apoyo para ejecutar los roles del repositorio y el entorno local.

## Estado verificable del repositorio

- La vision funcional y el backlog viven en `product-manager/`.
- La documentacion de usuario, tecnica y administracion vive en `doc-teams/`.
- El arbol actual no muestra una aplicacion web desplegable que pueda documentarse como produccion vigente.
- Los manuales de `doc-teams/` describen el comportamiento esperado y las dependencias abiertas, no una interfaz de usuario verificada en este momento.

## Como orientarse

1. Lee `product-manager/vision-product.md` para entender el objetivo del producto.
2. Revisa `product-manager/product-backlog.md` para ver las prioridades funcionales.
3. Consulta los manuales de `doc-teams/` segun tu perfil:
   - `manual-usuario.md` para usuarios finales.
   - `manual-tecnico.md` para equipo tecnico.
   - `manual-administracion.md` para coordinacion y operacion documental.
4. Usa los scripts `*_rol-*.sh` solo como apoyo para ejecutar los roles del repositorio.

## Notas operativas

- `main` es la rama de referencia para trabajo documental y de coordinacion.
- Si una documentacion describe un comportamiento no visible en el arbol actual, debe tratarse como una dependencia abierta o una contradiccion a resolver, no como hecho consolidado.
