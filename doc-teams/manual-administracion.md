# Manual de administracion

## Publico objetivo
Administracion del proyecto, coordinacion operativa y responsables de mantenimiento documental.

## Alcance
Este manual describe como se gobierna el repositorio desde el punto de vista operativo y documental.

## Estado actual
- El proyecto mantiene una estructura por roles.
- La actividad documental y de coordinacion se registra sobre `main`.
- Los cambios documentales requieren commit en espanol y subida al remoto.

## Reglas operativas relevantes
### Rama y versionado
- `main` es la rama de referencia para documentacion y coordinacion.
- `doc-teams` no debe crear ramas propias para cambios ordinarios.
- Si se cambia temporalmente de rama por necesidad excepcional, el ultimo paso debe devolver el trabajo a `main`.

### Registro de actividad
- Cada actualizacion documental debe quedar registrada en `changelog/`.
- Las entradas deben incluir hora exacta de escritura.
- Si se realizan varias actualizaciones el mismo dia, deben añadirse como entradas separadas al final del fichero del dia.

### Trazabilidad
- La documentacion funcional proviene de `product-manager/`.
- La documentacion tecnica debe alinearse con el comportamiento real o con las limitaciones verificadas del repositorio.
- Cualquier contradiccion entre vision, documento e implementacion debe quedar explicitada.

## Tareas de administracion recomendadas
1. Revisar si la documentacion existente sigue alineada con la vision del producto.
2. Confirmar si ya existe una entrega tecnica validada en `main` antes de describirla como vigente.
3. Verificar que los artefactos de producto tengan suficiente contexto para no generar documentacion ambigua.
4. Mantener visibles las dependencias abiertas y las limitaciones conocidas.

## Riesgos actuales
- Existe una brecha entre la vision del producto y el estado visible del repositorio.
- El backlog de producto no esta poblado, lo que dificulta la priorizacion documental y la trazabilidad.
- La ausencia de una aplicacion ejecutable limita la profundidad de los manuales de operacion.

## Criterio administrativo
Mientras no exista una entrega funcional validada, la administracion debe tratar este repositorio como un espacio de coordinacion documental y operativa, no como una plataforma lista para explotacion de usuarios finales.
