# Roadmap

## Objetivo
Traducir la vision del producto a una secuencia de entregas manejable para `developer-teams` y verificable por `qa-teams`, priorizando primero la base contable del producto.

## Supuestos
- `PB-001` ya esta validado e integrado en `main`, por lo que el roadmap debe construirse sobre una base contable minima ya disponible.
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
  - Resumen economico y listado de movimientos visibles para la comunidad.
- Dependencias clave: PB-002, PB-003
- Riesgo principal: No definir con precision que informacion es visible para el vecino.

## Fase 3 - Migracion y cierre operativo
- Backlog incluido: PB-005, PB-006, PB-008
- Objetivo: Facilitar puesta en marcha con datos historicos y preparar la planificacion y el cierre anual.
- Resultado esperado:
  - Importacion inicial desde hoja de calculo.
  - Presupuesto anual consultable por ejercicio.
  - Revision funcional del cierre anual.
- Dependencias clave: PB-001, PB-002, PB-003
- Riesgo principal: Elevar complejidad del MVP si no se acotan importacion, presupuestos y cierre anual.

## Fase 4 - Comunicacion proactiva
- Backlog incluido: PB-007
- Objetivo: Mejorar seguimiento de hitos relevantes mediante recordatorios.
- Resultado esperado:
  - Recordatorios configurables para administradores.
  - Visualizacion controlada para vecinos cuando aplique.
- Dependencias clave: PB-004
- Riesgo principal: Introducir notificaciones antes de consolidar el flujo contable principal.

## Dependencias abiertas
- Confirmar si el cierre anual requerira en una fase posterior una salida formal exportable ademas de la consulta consolidada del MVP.
- Confirmar si el presupuesto anual necesita versionado de revisiones en el alcance inicial o si basta con una version vigente por ejercicio.
