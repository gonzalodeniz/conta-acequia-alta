# Roadmap

## Objetivo
Traducir la vision del producto a una secuencia de entregas manejable para `developer-teams` y verificable por `qa-teams`, priorizando primero la base contable del producto.

## Supuestos
- `PB-001` ya esta validado e integrado en `main`, por lo que el roadmap debe construirse sobre una base contable minima ya disponible.
- `PB-002` ya fue validado por `qa-teams` el 24 de marzo de 2026 y su siguiente paso operativo es la fusion en `main` antes de promover nuevo trabajo tecnico.
- `developer-teams` trabajara una issue cada vez.
- El roadmap expresa prioridad funcional, no compromiso tecnico de fechas cerradas.

## Fase 1 - Base contable operativa
- Backlog incluido: PB-001, PB-002, PB-003
- Objetivo: Conseguir que la comunidad pueda registrar movimientos y consultar su impacto economico basico.
- Resultado esperado:
  - Alta de gastos e ingresos.
  - Libro de asientos consultable.
  - Resumen financiero por periodo.
- Dependencias clave: Ninguna externa visible a nivel de producto.
- Riesgo principal: Intentar introducir capacidades accesorias antes de que exista una base contable fiable.

## Fase 1.1 - Clasificacion contable asistida
- Backlog incluido: PB-009
- Objetivo: Completar la traduccion de la vision contable inicial con ayuda guiada para clasificar movimientos segun el Plan General de Contabilidad de Espana.
- Resultado esperado:
  - Sugerencias de cuentas contables habituales para comunidades de vecinos.
  - Trazabilidad entre el movimiento registrado y la cuenta elegida.
  - Exclusiones de amortizacion mantenidas en el alcance inicial.
- Dependencias clave: PB-001
- Riesgo principal: Mantener durante demasiado tiempo un registro de movimientos sin clasificacion asistida puede degradar la calidad contable y alejar el producto de su vision.

## Fase 2 - Transparencia para vecinos
- Backlog incluido: PB-004
- Objetivo: Habilitar consulta de informacion economica sin capacidad de modificacion.
- Resultado esperado:
  - Acceso de solo lectura para vecinos.
  - Resumen economico y listado completo de movimientos visibles para la comunidad en el MVP, sin publicacion selectiva en esta fase.
- Dependencias clave: PB-002, PB-003
- Riesgo principal: No definir con precision que informacion es visible para el vecino.

## Fase 3 - Migracion y cierre operativo
- Backlog incluido: PB-005, PB-006, PB-008
- Objetivo: Facilitar puesta en marcha con datos historicos y preparar la planificacion y el cierre anual.
- Resultado esperado:
  - Importacion inicial desde hoja de calculo.
  - Presupuesto anual consultable por ejercicio con una unica version vigente en el alcance inicial.
  - Revision funcional del cierre anual.
- Dependencias clave: PB-001, PB-002, PB-003
- Riesgo principal: Elevar complejidad del MVP si no se acotan importacion, presupuestos y cierre anual.

## Fase 4 - Comunicacion proactiva
- Backlog incluido: PB-007
- Objetivo: Mejorar seguimiento de hitos relevantes mediante recordatorios.
- Resultado esperado:
  - Recordatorios configurables para administradores dentro de la aplicacion.
  - Consulta de estado de recordatorios sin canales salientes en el MVP.
- Dependencias clave: Ninguna funcional bloqueante, aunque su prioridad queda por detras del flujo contable principal.
- Riesgo principal: Introducir canales o destinatarios adicionales antes de consolidar el flujo contable principal y el alcance administrativo del MVP.

## Dependencias abiertas
- Confirmar si el cierre anual requerira en una fase posterior una salida formal exportable ademas de la consulta consolidada del MVP.
- Confirmar si en una fase posterior los recordatorios necesitaran canales salientes o destinatarios adicionales.

## Siguiente prioridad operativa
1. Completar la fusion en `main` y el cierre administrativo de la issue `#2`.
2. Priorizar `PB-003` como siguiente entrega del flujo base del MVP.
3. Mantener `PB-009` como siguiente capacidad de alto valor una vez consolidado el resumen financiero.
