# Refinamiento funcional

## Objetivo
Reducir ambiguedad antes de crear o priorizar nuevas issues para `developer-teams`.

## Estado de refinamiento actual

### Listo para desarrollo inmediato
- PB-001 - Registrar gastos e ingresos de la comunidad
  - Ya validado por `qa-teams` en la issue `#1`.
  - Ya integrado en `main` y cerrado administrativamente.
- PB-002 - Consultar el libro de asientos contables
  - Ya validado por `qa-teams` en la issue `#2`.
  - Pendiente de fusion en `main` y cierre administrativo posterior.
- PB-003 - Visualizar resumen financiero del periodo
  - Dependencia directa de PB-001.
  - Valor alto y validacion clara.
  - Debe ser la siguiente issue funcional una vez integrada la issue `#2`.
- PB-004 - Permitir acceso de solo lectura para vecinos
  - Se fija para el alcance inicial un modo solo lectura con resumen economico mensual y anual mas listado visible de movimientos para la comunidad.
  - No incluye acciones de gestion ni reglas avanzadas de publicacion selectiva en esta primera iteracion.
- PB-008 - Gestionar presupuestos anuales de la comunidad
  - La vision ya exige esta capacidad y el alcance inicial puede validarse sin decisiones tecnicas complejas.
  - Se limita a definicion y consulta del presupuesto por ejercicio, sin comparativa avanzada contra ejecucion real en esta primera entrega.
  - Se fija una unica version vigente por ejercicio en el alcance inicial.
- PB-005 - Importar movimientos desde una hoja de calculo
  - La plantilla funcional oficial minima queda fijada con columnas obligatorias y rechazo funcional por tipo invalido.
  - El alcance inicial puede validarse sobre una sola plantilla oficial sin abrir todavia compatibilidad con multiples fuentes.
- PB-006 - Preparar el cierre contable anual
  - Se fija para la primera version una consulta consolidada del ejercicio, con trazabilidad y deteccion de meses sin movimientos.
  - No incluye bloqueo funcional del ejercicio ni exportacion formal en esta iteracion.
- PB-009 - Guiar la clasificacion contable con PGC simplificado
  - Corrige una brecha actual entre la vision y la entrega real de PB-001.
  - Puede ejecutarse como entrega acotada sobre el flujo ya integrado en `main`.
- PB-007 - Enviar notificaciones y recordatorios operativos
  - Se acota al administrador como unico destinatario en el MVP.
  - La primera iteracion cubre gestion y consulta interna de recordatorios, sin canales salientes.

### Requiere refinamiento adicional
- Ningun item funcional del backlog principal requiere refinamiento adicional bloqueante para su creacion o mantenimiento de issue.

## Decisiones funcionales tomadas
- El MVP inicial se centra en base contable, consulta del libro y resumen financiero.
- La transparencia para vecinos se apoya sobre informacion ya consolidada y no sobre edicion distribuida.
- En la primera iteracion de vecinos, el alcance visible sera resumen economico mensual y anual mas listado completo de movimientos de la comunidad en modo solo lectura, sin publicacion selectiva.
- Presupuestos entra en el backlog ejecutable como capacidad de planificacion anual, pero sin comparativas avanzadas ni historico de revisiones en la primera iteracion.
- El presupuesto anual del MVP mantendra una unica version vigente por ejercicio.
- La importacion inicial partira de una sola plantilla oficial con columnas `fecha`, `tipo`, `concepto`, `categoria`, `importe` y `referencia_externa` opcional.
- El cierre anual inicial sera una consulta consolidada con trazabilidad y deteccion de meses sin movimientos, sin bloqueo del ejercicio.
- La importacion, el cierre anual y las notificaciones quedan despues del flujo contable principal.
- La clasificacion contable asistida se separa del registro basico ya entregado y pasa a `PB-009` para corregir la brecha con la vision.
- La ayuda de seleccion de `PB-009` priorizara una lista canonica inicial con `570 Caja`, `572 Bancos e instituciones de credito c/c vista`, `400 Proveedores`, `410 Acreedores por prestaciones de servicios`, `623 Servicios de profesionales independientes`, `628 Suministros`, `629 Otros servicios`, `705 Prestaciones de servicios` y `740 Subvenciones, donaciones y legados a la explotacion`.
- La ayuda de `PB-009` se guiara por tipo de movimiento: para gastos se priorizaran `400`, `410`, `623`, `628` y `629`; para ingresos se priorizaran `705` y `740`; `570` y `572` podran presentarse como cuentas operativas de apoyo cuando el movimiento afecte tesoreria.
- Las cuentas de amortizacion quedan fuera del alcance funcional actual.
- Los recordatorios de `PB-007` quedan limitados al administrador en el MVP y no se mostraran a vecinos en esta primera iteracion.
- `PB-007` cubrira gestion y consulta de recordatorios dentro de la aplicacion, sin canales salientes en esta fase.

## Dependencias abiertas
- Importacion:
  - Pendiente decidir si, ademas de la plantilla oficial, se aceptaran fuentes equivalentes.
- Ayuda de cuentas PGC:
  - Resuelto el listado canonico inicial y la prioridad por tipo de movimiento para `PB-009`.
  - Pendiente decidir si una fase posterior necesitara ampliar la ayuda hacia familias adicionales de cuentas habituales sin convertirla en navegacion completa por el PGC.
- Cierre anual:
  - Pendiente decidir si en una fase posterior se necesitara exportacion formal o una marca funcional de cierre revisado.
- Recordatorios:
  - Pendiente decidir si una fase posterior necesitara canales salientes o destinatarios adicionales al administrador.

## Riesgos
- Si se interpreta `PB-001` como si ya incluyera ayuda PGC, se perdera trazabilidad sobre una parte de la vision que todavia no se ha entregado.
- Si se intenta introducir presupuestos antes de cerrar el MVP contable, se fragmentara el foco del producto.
- Si la issue `#2` sigue abierta tras su validacion, el equipo puede perder disciplina de cierre de flujo entre validacion, integracion y cierre administrativo.
- La ausencia de `README.md` y `Makefile` con contexto de producto o ejecucion aumenta la dependencia documental en los artefactos de `product-manager`.

## Propuesta operativa inmediata
1. Exigir la fusion en `main` y el cierre administrativo posterior de la issue `#2` antes de promover una nueva implementacion tecnica.
2. Priorizar `#3` como siguiente tramo del flujo base del MVP.
3. Mantener `#6` como siguiente capacidad de alto valor para cerrar la brecha de vision sobre clasificacion contable.
4. Mantener `#4`, `#7`, `#8`, `#9` y `#10` como backlog ejecutable ya refinado para iteraciones posteriores.
