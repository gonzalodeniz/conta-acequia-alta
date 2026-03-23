# Refinamiento funcional

## Objetivo
Reducir ambiguedad antes de crear o priorizar nuevas issues para `developer-teams`.

## Estado de refinamiento actual

### Listo para desarrollo inmediato
- PB-001 - Registrar gastos e ingresos de la comunidad
  - Ya validado por `qa-teams` en la issue `#1`.
  - Ya integrado en `main` y cerrado administrativamente.
- PB-002 - Consultar el libro de asientos contables
  - Dependencia directa de PB-001.
  - Flujo de consulta bien definido.
- PB-003 - Visualizar resumen financiero del periodo
  - Dependencia directa de PB-001.
  - Valor alto y validacion clara.
- PB-004 - Permitir acceso de solo lectura para vecinos
  - Se fija para el alcance inicial un modo solo lectura con resumen economico mensual y anual mas listado visible de movimientos para la comunidad.
  - No incluye acciones de gestion ni reglas avanzadas de publicacion selectiva en esta primera iteracion.
- PB-008 - Gestionar presupuestos anuales de la comunidad
  - La vision ya exige esta capacidad y el alcance inicial puede validarse sin decisiones tecnicas complejas.
  - Se limita a definicion y consulta del presupuesto por ejercicio, sin comparativa avanzada contra ejecucion real en esta primera entrega.
- PB-005 - Importar movimientos desde una hoja de calculo
  - La plantilla funcional oficial minima queda fijada con columnas obligatorias y rechazo funcional por tipo invalido.
  - El alcance inicial puede validarse sobre una sola plantilla oficial sin abrir todavia compatibilidad con multiples fuentes.
- PB-006 - Preparar el cierre contable anual
  - Se fija para la primera version una consulta consolidada del ejercicio, con trazabilidad y deteccion de meses sin movimientos.
  - No incluye bloqueo funcional del ejercicio ni exportacion formal en esta iteracion.
- PB-009 - Guiar la clasificacion contable con PGC simplificado
  - Corrige una brecha actual entre la vision y la entrega real de PB-001.
  - Puede ejecutarse como entrega acotada sobre el flujo ya integrado en `main`.

### Requiere refinamiento adicional
- PB-007 - Enviar notificaciones y recordatorios operativos
  - Falta definir canales, destinatarios y eventos obligatorios.

## Decisiones funcionales tomadas
- El MVP inicial se centra en base contable, consulta del libro y resumen financiero.
- La transparencia para vecinos se apoya sobre informacion ya consolidada y no sobre edicion distribuida.
- En la primera iteracion de vecinos, el alcance visible sera resumen economico mensual y anual mas listado de movimientos en modo solo lectura.
- Presupuestos entra en el backlog ejecutable como capacidad de planificacion anual, pero sin comparativas avanzadas ni historico de revisiones en la primera iteracion.
- La importacion inicial partira de una sola plantilla oficial con columnas `fecha`, `tipo`, `concepto`, `categoria`, `importe` y `referencia_externa` opcional.
- El cierre anual inicial sera una consulta consolidada con trazabilidad y deteccion de meses sin movimientos, sin bloqueo del ejercicio.
- La importacion, el cierre anual y las notificaciones quedan despues del flujo contable principal.
- La clasificacion contable asistida se separa del registro basico ya entregado y pasa a `PB-009` para corregir la brecha con la vision.
- La ayuda de seleccion de `PB-009` priorizara cuentas sencillas de gastos e ingresos y cuentas populares para la operativa de una comunidad de vecinos, como banco, caja, proveedores, acreedores, suministros y reparaciones.
- Las cuentas de amortizacion quedan fuera del alcance funcional actual.

## Dependencias abiertas
- Presupuestos:
  - Pendiente decidir si el ejercicio admite una sola version vigente o multiples revisiones trazables.
- Importacion:
  - Pendiente decidir si, ademas de la plantilla oficial, se aceptaran fuentes equivalentes.
- Ayuda de cuentas PGC:
  - Pendiente concretar el listado inicial de cuentas sugeridas por defecto y si se presentaran por tipo de movimiento, por frecuencia o por ambos criterios.
- Cierre anual:
  - Pendiente decidir si en una fase posterior se necesitara exportacion formal o una marca funcional de cierre revisado.

## Riesgos
- Si se interpreta `PB-001` como si ya incluyera ayuda PGC, se perdera trazabilidad sobre una parte de la vision que todavia no se ha entregado.
- Si se intenta introducir presupuestos antes de cerrar el MVP contable, se fragmentara el foco del producto.
- La ausencia de `README.md` y `Makefile` con contexto de producto o ejecucion aumenta la dependencia documental en los artefactos de `product-manager`.

## Propuesta operativa inmediata
1. Priorizar `#2` y `#3` como siguiente tramo del flujo base del MVP.
2. Mantener `#4` como trazabilidad ejecutable de `PB-008`.
3. Mantener visibles `#6`, `#7`, `#8` y `#9` para que `developer-teams` tome trabajo ya refinado cuando el flujo lo permita.
4. Resolver la lista inicial de cuentas sugeridas para `PB-009` antes del handoff funcional de esa issue.
5. Mantener `PB-007` fuera de ejecucion hasta cerrar canales, destinatarios y eventos obligatorios.
