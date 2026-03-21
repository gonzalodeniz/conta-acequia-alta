# Analisis de proceso

## Contexto analizado
- El repositorio ya dispone de backlog funcional y de issues operativas en curso, por lo que el problema principal ya no es la ausencia de cola sino su sincronizacion con el estado real de cada issue.
- `product-manager/product-backlog.md` esta poblado, pero sigue siendo sensible a desalineaciones manuales cuando las issues avanzan a `en desarrollo`, `listo para qa`, `validado` o `cerrado`.
- En `changelog/2026-03-21.md` aparecio una entrada firmada como `codex`, que no refleja un rol operativo activado de forma explicita.
- El flujo entre `product-manager`, `developer-teams`, `qa-teams` y `doc-teams` ya esta bastante cerrado, pero varias reglas siguen repartidas entre `AGENTS.md` raiz, los `AGENTS.md` de rol y los artefactos de `agile-coach/`.

## Hallazgos principales

### 1. El backlog persistente sigue sin actuar como fuente de verdad viva
- Evidencia observada: el backlog ya existe, pero sus items enlazados a issues dependen de actualizacion manual y pueden quedarse atras respecto al ultimo estado operativo visible en GitHub.
- Impacto: la priorizacion real puede apoyarse en una fotografia desfasada del trabajo, especialmente tras validacion o cierre administrativo.
- Lectura operativa: el flujo tiene reglas de backlog, pero necesita una sincronizacion explicita con el ciclo de vida de la issue para seguir siendo una referencia cotidiana fiable.

### 2. La firma del `changelog` debe asociarse siempre a un rol activado
- Evidencia observada: en `changelog/2026-03-21.md` aparecio una entrada firmada como `codex`.
- Impacto: esa firma complica la auditoria diaria y debilita la trazabilidad operativa.
- Lectura operativa: la regla existe, pero conviene endurecerla para que solo se usen firmas ligadas a roles activados expresamente.

### 3. La operativa esta bien definida, pero demasiado dispersa
- Evidencia observada: los estados, handoffs y checkpoints estan repartidos entre varios documentos.
- Impacto: aumenta el riesgo de deriva entre documentos cuando una regla cambia.
- Lectura operativa: hace falta una referencia canonica mas clara para plantillas, secuencia y propagacion de cambios.

### 4. Faltaba una gobernanza explicita del cambio de proceso
- Evidencia observada: no estaba explicitado que una mejora de coordinacion debe propagarse en la misma iteracion a la referencia operativa y a los `AGENTS.md` afectados.
- Impacto: una mejora puede quedar aplicada solo de forma parcial y distintos equipos pueden seguir versiones distintas de la misma regla.
- Lectura operativa: la coordinacion necesita un guardarrail documental que evite bifurcaciones silenciosas.

### 5. No existia una metrica ligera para detectar divergencia entre backlog e issue
- Evidencia observada: las metricas actuales cubren estados operativos, QA y cierre, pero no la coherencia entre el backlog persistente y el estado real de las issues enlazadas.
- Impacto: la desalineacion entre backlog y flujo operativo puede pasar desapercibida aunque el resto de la trazabilidad documental este correcta.
- Lectura operativa: conviene medir si el backlog sigue la misma realidad que GitHub y no se queda congelado en estados previos.

## Propuestas de mejora

### A. Introducir un checkpoint minimo de backlog vivo
- Requerir que `product-manager` mantenga al menos un item priorizado y trazable en `product-manager/product-backlog.md` cuando exista demanda activa.
- Vincular cada issue lista para desarrollo con ese backlog antes de pasar a `en desarrollo` y mantener el estado del item sincronizado con el ultimo estado operativo de la issue.
- Beneficio: mejora la priorizacion, evita arranques sin fuente de verdad y reduce preguntas de contexto al inicio de una implementacion.

### B. Normalizar la firma de `changelog`
- Exigir que cada entrada se firme con el nombre del rol activado explicitamente en el prompt.
- Prohibir etiquetas genericas o de herramienta como firma del resumen.
- Beneficio: mejora la auditabilidad y permite detectar con facilidad que rol produjo cada cambio de proceso.

### C. Usar `acuerdos-operativos.md` como referencia canonica y propagar cambios en la misma iteracion
- Tratar `agile-coach/acuerdos-operativos.md` como referencia operativa canonica para estados, plantillas y reglas de handoff.
- Exigir que cualquier cambio de coordinacion actualice en la misma iteracion el documento canonico y los `AGENTS.md` afectados.
- Beneficio: reduce deriva documental y hace mas predecible el mantenimiento de reglas comunes.

### D. Añadir una metrica ligera de divergencia documental
- Medir cuantas veces una revision de proceso detecta que una misma regla aparece distinta entre `acuerdos-operativos.md` y los `AGENTS.md` afectados.
- Beneficio: permite saber si la operativa esta bifurcandose antes de que el problema llegue a los handoffs del dia a dia.

## Tradeoffs
- El control operativo gana disciplina, pero tambien exige que `product-manager` y los demas roles cuiden un poco mas el mantenimiento del backlog y de las firmas.
- La carga documental sigue siendo ligera si las mejoras se limitan a campos y reglas cortas, pero puede crecer si se intenta compensar con texto narrativo en lugar de reglas concretas.
- Centralizar la referencia de proceso simplifica la lectura, pero obliga a mantener esa referencia canonica al dia.

## Riesgos
- Si el backlog se mantiene vacio, la priorizacion real seguira ocurriendo fuera de los artefactos del repositorio.
- Si las firmas de `changelog` no se normalizan, la trazabilidad diaria seguira perdiendo valor para auditoria y seguimiento.
- Si los cambios de proceso no se propagan en la misma iteracion, volvera la deriva entre documentos y equipos.

## Dependencias
- Que los roles mantengan el habito de reflejar las transiciones en la issue y en el `changelog/` cuando aplique.
- Que las revisiones de proceso consideren la coherencia documental como parte del trabajo, no como una tarea auxiliar.
- Que `agile-coach/acuerdos-operativos.md` se mantenga como referencia canonica y no se convierta en un resumen desactualizado.
