# Roadmap

## Objetivo
Traducir la vision del producto a una secuencia de entregas manejable para `developer-teams` y verificable por `qa-teams`, priorizando primero la base contable del producto.

## Supuestos
- El producto se encuentra en fase de definicion funcional y no existe una entrega validada en `main`.
- `developer-teams` trabajara una issue cada vez.
- El roadmap expresa prioridad funcional, no compromiso tecnico de fechas cerradas.

## Fase 1 - Base contable del MVP
- Backlog incluido: PB-001, PB-002, PB-003
- Objetivo: Conseguir que la comunidad pueda registrar movimientos y consultar su impacto economico basico.
- Resultado esperado:
  - Alta de gastos e ingresos.
  - Libro de asientos consultable.
  - Resumen financiero por periodo.
- Dependencias clave: Ninguna externa visible a nivel de producto.
- Riesgo principal: Intentar introducir capacidades accesorias antes de que exista una base contable fiable.

## Fase 2 - Transparencia para vecinos
- Backlog incluido: PB-004
- Objetivo: Habilitar consulta de informacion economica sin capacidad de modificacion.
- Resultado esperado:
  - Acceso de solo lectura para vecinos.
  - Reglas de visibilidad claras para informacion publicada.
- Dependencias clave: PB-002, PB-003
- Riesgo principal: No definir con precision que informacion es visible para el vecino.

## Fase 3 - Migracion y cierre operativo
- Backlog incluido: PB-005, PB-006
- Objetivo: Facilitar puesta en marcha con datos historicos y preparar la operativa anual.
- Resultado esperado:
  - Importacion inicial desde hoja de calculo.
  - Revision funcional del cierre anual.
- Dependencias clave: PB-001, PB-002, PB-003
- Riesgo principal: Elevar complejidad del MVP si no se acota la importacion y el cierre anual.

## Fase 4 - Comunicacion proactiva
- Backlog incluido: PB-007
- Objetivo: Mejorar seguimiento de hitos relevantes mediante recordatorios.
- Resultado esperado:
  - Recordatorios configurables para administradores.
  - Visualizacion controlada para vecinos cuando aplique.
- Dependencias clave: PB-004
- Riesgo principal: Introducir notificaciones antes de consolidar el flujo contable principal.

## Dependencias abiertas
- Definir el alcance funcional exacto de presupuestos, ya que la vision los menciona pero no existe todavia backlog refinado especifico.
- Confirmar si el cierre anual requiere una salida formal exportable o solo una consulta consolidada.
- Definir politica de visibilidad para vecinos antes de ejecutar PB-004.
