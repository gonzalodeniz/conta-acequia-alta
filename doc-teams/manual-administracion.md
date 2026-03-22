# Manual de administracion

## Publico objetivo
Administracion del proyecto, coordinacion operativa y responsables de mantenimiento documental.

## Alcance
Este manual describe como se gobierna el repositorio desde el punto de vista documental y operativo.
Tambien resume las precauciones minimas para administrar una base de datos local y no confundir una entrega minima con una instalacion de produccion.

## Estado actual
- El proyecto mantiene una estructura por roles.
- La actividad documental y de coordinacion se registra sobre `main`.
- Los cambios documentales requieren `git add`, `git commit` en espanol y `git push`.
- Existe una aplicacion minima con persistencia en `data/movimientos.json`.
- El backlog funcional ya esta poblado, por lo que la trazabilidad entre producto y documentacion puede seguirse sin partir de un vacio inicial.

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
- Cualquier contradiccion entre vision, backlog, documento y estado del arbol debe quedar explicitada.

## Tareas de administracion recomendadas
1. Revisar si la documentacion existente sigue alineada con la vision del producto y con el backlog vigente.
2. Confirmar si la entrega tecnica revisada ya esta fusionada en `main` antes de documentarla como vigente.
3. Verificar que cualquier dependencia abierta quede visible para evitar manuales ambiguos.
4. Mantener rastreadas las contradicciones entre el changelog y el arbol de trabajo cuando aparezcan.
5. Hacer copia de seguridad de `data/movimientos.json` antes de borrar o reponer el entorno, porque ahi se guardan los movimientos.
6. Restaurar `data/movimientos.json` desde respaldo si se necesita conservar datos historicos.

## Riesgos actuales
- Existe una brecha entre la vision del producto, el backlog completo y la entrega minima actualmente implementada.
- La persistencia local en un unico fichero hace que la perdida de `data/movimientos.json` implique perdida de datos si no hay copia previa.
- Si no se resuelve la discrepancia documental, puede documentarse como vigente algo que todavia no esta comprobado en `main`.

## Criterio administrativo
Mientras no exista una entrega completa validada e integrada, la administracion debe tratar este repositorio como un espacio de coordinacion documental y operativa, no como una plataforma lista para explotacion completa de usuarios finales.
