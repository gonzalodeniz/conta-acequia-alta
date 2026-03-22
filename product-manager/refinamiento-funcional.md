# Refinamiento funcional

## Objetivo
Reducir ambiguedad antes de crear o priorizar nuevas issues para `developer-teams`.

## Estado de refinamiento actual

### Listo para desarrollo inmediato
- PB-001 - Registrar gastos e ingresos de la comunidad
  - Ya validado por `qa-teams` en la issue `#1`.
  - Pendiente de checkpoint administrativo e integracion en `main`.
- PB-002 - Consultar el libro de asientos contables
  - Dependencia directa de PB-001.
  - Flujo de consulta bien definido.
- PB-003 - Visualizar resumen financiero del periodo
  - Dependencia directa de PB-001.
  - Valor alto y validacion clara.
- PB-008 - Gestionar presupuestos anuales de la comunidad
  - La vision ya exige esta capacidad y el alcance inicial puede validarse sin decisiones tecnicas complejas.
  - Se limita a definicion y consulta del presupuesto por ejercicio, sin comparativa avanzada contra ejecucion real en esta primera entrega.

### Requiere refinamiento adicional
- PB-004 - Permitir acceso de solo lectura para vecinos
  - Funcionalmente priorizado, pero requiere cerrar antes una regla de visibilidad minima.
- PB-005 - Importar movimientos desde una hoja de calculo
  - Falta definir plantilla funcional oficial.
  - Falta decidir si la importacion parcial es aceptable en el MVP.
- PB-006 - Preparar el cierre contable anual
  - Falta concretar si incluye bloqueo de ejercicio o solo consulta consolidada.
  - Falta precisar que evidencia necesita el administrador para dar el cierre por revisado.
- PB-007 - Enviar notificaciones y recordatorios operativos
  - Falta definir canales, destinatarios y eventos obligatorios.

## Decisiones funcionales tomadas
- El MVP inicial se centra en base contable, consulta del libro y resumen financiero.
- La transparencia para vecinos se apoya sobre informacion ya consolidada y no sobre edicion distribuida.
- Presupuestos entra en el backlog ejecutable como capacidad de planificacion anual, pero sin comparativas avanzadas ni historico de revisiones en la primera iteracion.
- La importacion, el cierre anual y las notificaciones quedan despues del flujo contable principal.
- La seleccion de cuenta contable en el alta de movimientos se apoyara en el Plan General de Contabilidad de Espana.
- La ayuda de seleccion priorizara cuentas sencillas de gastos e ingresos y cuentas populares para la operativa de una comunidad de vecinos, como banco, caja, proveedores y acreedores.
- Las cuentas de amortizacion quedan fuera del alcance funcional actual.

## Dependencias abiertas
- Regla de visibilidad para vecinos:
  - Pendiente decidir si el vecino vera detalle completo de asientos o solo informacion agregada/publicada.
- Presupuestos:
  - Pendiente decidir si el ejercicio admite una sola version vigente o multiples revisiones trazables.
- Importacion:
  - Pendiente acordar la estructura minima del fichero fuente.
- Ayuda de cuentas PGC:
  - Pendiente concretar el listado inicial de cuentas sugeridas por defecto y si se presentaran por tipo de movimiento, por frecuencia o por ambos criterios.

## Riesgos
- Si se crea una issue de acceso de vecinos sin cerrar la regla de visibilidad, QA no podra validar el alcance con seguridad.
- Si no se integra `PB-001` en `main` tras su validacion, el roadmap seguira bloqueado administrativamente aunque el flujo tecnico haya avanzado.
- Si se intenta introducir presupuestos antes de cerrar el MVP contable, se fragmentara el foco del producto.
- La ausencia de `README.md` y `Makefile` con contexto de producto o ejecucion aumenta la dependencia documental en los artefactos de `product-manager`.

## Propuesta operativa inmediata
1. Dejar checkpoint administrativo en la issue `#1` y promover su integracion para poder cerrarla.
2. Mantener `#2` y `#3` como siguientes issues del flujo base del MVP.
3. Mantener la issue `#4` como trazabilidad ejecutable de `PB-008`.
4. No crear issue para `PB-004` hasta cerrar la politica minima de visibilidad para vecinos.
