# Analisis del proceso

## Objetivo
Documentar hallazgos concretos sobre la coordinacion actual entre equipos y dejar visibles las mejoras de proceso que conviene priorizar.

## Hallazgos principales

### 1. El backlog persistente esta vacio
- Evidencia observada: `product-manager/product-backlog.md` existe pero esta vacio.
- Evidencia complementaria: no hay issues abiertas en GitHub en este momento.
- Impacto: el flujo depende de issues sueltas y no de una cola priorizada y persistente. Eso dificulta saber que trabajo llega despues, reduce la trazabilidad entre vision y ejecucion y debilita la priorizacion cuando aparecen varias necesidades a la vez.
- Lectura operativa: el repositorio tiene reglas de backlog, pero aun no tiene una fuente de verdad funcional viva que haga de referencia cotidiana para `product-manager` y `developer-teams`.

### 2. El `changelog` contiene una firma no asociada a un rol operativo
- Evidencia observada: en `changelog/2026-03-21.md` aparece una entrada firmada como `codex`.
- Impacto: esa firma no ayuda a auditar que rol produjo la entrada ni a leer el historial por responsabilidad operativa.
- Lectura operativa: la regla de trazabilidad existe, pero conviene endurecerla para que solo se usen firmas ligadas a roles activados expresamente.

### 3. El flujo entre equipos esta bien definido, pero faltan dos guardarrailes ligeros
- Lo que ya esta bien: los estados operativos, los handoffs y la separacion de responsabilidades estan bastante claros.
- Lo que falta: una comprobacion explicita de salud del backlog antes de abrir nueva implementacion y una regla mas estricta sobre como firmar el `changelog`.
- Impacto: sin esos dos guardarrailes, el proceso sigue siendo correcto en teoria pero puede degradarse en la practica por falta de una cola de priorizacion viva o por firmas poco auditables.

## Propuestas de mejora

### A. Introducir un checkpoint minimo de backlog vivo
- Requerir que `product-manager` mantenga al menos un item priorizado y trazable en `product-manager/product-backlog.md` cuando exista demanda activa.
- Vincular cada issue lista para desarrollo con ese backlog antes de pasar a `en desarrollo`.
- Beneficio: mejora la priorizacion, evita arranques sin fuente de verdad y reduce preguntas de contexto al inicio de una implementacion.

### B. Normalizar la firma de `changelog`
- Exigir que cada entrada se firme con el nombre del rol activado explicitamente en el prompt.
- Prohibir etiquetas genericas o de herramienta como firma del resumen.
- Beneficio: mejora la auditabilidad y permite detectar con facilidad que rol produjo cada cambio de proceso.

### C. Mantener una trazabilidad explicita de hallazgos recurrentes
- Registrar los problemas repetibles en `mejoras-propuestas.md` y `riesgos-de-coordinacion.md`.
- Actualizar `AGENTS.md` cuando el hallazgo afecte a una obligacion de un rol o a una regla global del flujo.
- Beneficio: evita que los hallazgos queden en notas aisladas sin transformarse en reglas de trabajo.

## Tradeoffs
- El control operativo gana disciplina, pero tambien exige que `product-manager` y los demas roles cuiden un poco mas el mantenimiento del backlog y de las firmas.
- La carga documental sigue siendo ligera si las mejoras se limitan a campos y reglas cortas, pero puede crecer si se intenta compensar con texto narrativo en lugar de reglas concretas.

## Riesgos
- Si el backlog se mantiene vacio, la priorizacion real seguira ocurriendo fuera de los artefactos del repositorio.
- Si las firmas de `changelog` no se normalizan, la trazabilidad diaria seguira perdiendo valor para auditoria y seguimiento.
- Si las mejoras de proceso no se reflejan en los artefactos correctos, el equipo seguira viendo el mismo problema con distinto texto.
