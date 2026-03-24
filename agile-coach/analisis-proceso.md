# Analisis de proceso

Fecha de escritura: 2026-03-24 23:01:17 UTC
Changelog consultado: changelog/2026-03-24.md
Vigencia de ejemplos: vigente

## Contexto analizado
- El repositorio ya dispone de backlog funcional y de issues operativas en curso, por lo que el problema principal ya no es la ausencia de cola sino su sincronizacion con el estado real de cada issue.
- `product-manager/product-backlog.md` esta poblado, pero sigue siendo sensible a desalineaciones manuales cuando las issues avanzan a `en desarrollo`, `listo para qa`, `validado` o `cerrado`.
- La iteracion de `PB-001` y la issue `#1` mostro que una referencia de proceso puede quedar obsoleta en pocas horas si no se revalida contra el ultimo `changelog/` antes de reutilizarla como ejemplo vigente.
- El flujo entre `product-manager`, `developer-teams`, `qa-teams` y `doc-teams` ya esta bastante cerrado, pero varias reglas siguen repartidas entre `AGENTS.md` raiz, los `AGENTS.md` de rol y los artefactos de `agile-coach/`.

## Hallazgos principales

### 1. Las referencias concretas envejecen demasiado rapido si no se anclan a una revision reciente
- Evidencia observada: la secuencia de `PB-001` y la issue `#1` avanzo de trabajo operativo a validacion e integracion en el mismo ciclo, lo que dejo obsoletos algunos ejemplos de proceso que seguian citando la fotografia anterior.
- Impacto: un documento de proceso puede inducir a error si presenta como vigente un caso que solo era cierto en el momento de la captura.
- Lectura operativa: antes de reutilizar un ejemplo concreto, hay que revalidarlo contra el ultimo `changelog/` y dejar claro si es vigente o historico.

### 2. El backlog persistente sigue necesitando sincronizacion manual con el estado real de las issues
- Evidencia observada: el backlog ya existe, pero sus items enlazados a issues dependen de actualizacion manual y pueden quedarse atras respecto al ultimo estado operativo visible en GitHub.
- Impacto: la priorizacion real puede apoyarse en una fotografia desfasada del trabajo, especialmente tras validacion o cierre administrativo.
- Lectura operativa: el flujo tiene reglas de backlog, pero necesita una sincronizacion explicita con el ciclo de vida de la issue para seguir siendo una referencia cotidiana fiable.

### 3. La firma del `changelog` debe asociarse siempre a un rol activado
- Evidencia observada: en `changelog/2026-03-21.md` aparecio una entrada firmada como `codex`.
- Impacto: esa firma complica la auditoria diaria y debilita la trazabilidad operativa.
- Lectura operativa: la regla existe, pero conviene endurecerla para que solo se usen firmas ligadas a roles activados expresamente.

### 4. La operativa esta bien definida, pero demasiado dispersa
- Evidencia observada: los estados, handoffs y checkpoints estan repartidos entre varios documentos.
- Impacto: aumenta el riesgo de deriva entre documentos cuando una regla cambia.
- Lectura operativa: hace falta una referencia canonica mas clara para plantillas, secuencia y propagacion de cambios.

### 5. Faltaba una gobernanza explicita del cambio de proceso
- Evidencia observada: no estaba explicitado que una mejora de coordinacion debe propagarse en la misma iteracion a la referencia operativa y a los `AGENTS.md` afectados.
- Impacto: una mejora puede quedar aplicada solo de forma parcial y distintos equipos pueden seguir versiones distintas de la misma regla.
- Lectura operativa: la coordinacion necesita un guardarrail documental que evite bifurcaciones silenciosas.

### 6. No existia una metrica ligera para detectar vigencia de ejemplos de proceso
- Evidencia observada: las metricas actuales cubren estados operativos, QA y cierre, pero no si un analisis o riesgo se redacta con referencias ya caducadas.
- Impacto: una fotografia historica puede entrar en un documento como si fuera un estado actual y confundir a quien lo consulte despues.
- Lectura operativa: conviene medir si los ejemplos citados siguen siendo vigentes y si el documento explicita la fecha de la ultima revision.

### 7. La validacion puede quedar abierta sin checkpoint administrativo visible
- Evidencia observada: el flujo define que una issue validada puede seguir abierta mientras se documenta el motivo operativo, pero esa ventana sigue siendo facil de confundir con trabajo pendiente real.
- Impacto: otros equipos leen una entrega aceptada pero no saben si el siguiente paso es integracion, espera documental o cierre administrativo.
- Lectura operativa: hace falta vigilar la latencia entre validacion y cierre visible para que la issue no quede en limbo.

### 8. El backlog mezcla estado operativo con estado de refinamiento
- Evidencia observada: en `product-manager/product-backlog.md` los items enlazados a issue usan `Estado operativo:`, mientras que el item pendiente de refinamiento `PB-007` usa `Estado de backlog: refinamiento pendiente`.
- Impacto: un lector del backlog puede interpretar que todos los estados tienen la misma semantica, cuando en realidad unos describen el ciclo de vida de una issue y otros solo la madurez de una iniciativa aun no operable.
- Lectura operativa: conviene separar el campo que refleja ejecucion real del campo que refleja priorizacion o refinamiento para no mezclar cola de trabajo con cola de definicion.

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

### E. Vigilar la latencia entre `validado` y el checkpoint administrativo
- Medir el tiempo entre el comentario de `qa-teams` con `Estado operativo: validado` y el comentario administrativo de `product-manager` cuando la issue permanece abierta.
- Beneficio: hace visible el limbo post-validacion y permite detectar si el atasco esta en integracion, cierre o simple falta de actualizacion documental.
- Tradeoffs: añade una metrica mas al seguimiento operativo, aunque de lectura sencilla.
- Riesgos y dependencias: requiere que `product-manager` mantenga el comentario administrativo y la sincronizacion de estado sin retrasos innecesarios.

### F. Verificar la vigencia de los ejemplos antes de publicarlos como analisis vigente
- Requerir que cada analisis o riesgo de `agile-coach/` contraste la referencia mas reciente de `changelog/` y marque los casos concretos como `vigente` o `historico` a la fecha de escritura.
- Beneficio: evita que una fotografia operativa caducada se lea como evidencia actual y reduce la probabilidad de decisiones basadas en contexto desfasado.
- Tradeoffs: introduce una comprobacion extra antes de publicar el documento.
- Riesgos y dependencias: depende de que `changelog/` este al dia; si no lo esta, el analisis debe detenerse y pedir revalidacion del caso citado.

### G. Medir la vigencia de los documentos de proceso
- Seguir el porcentaje de analisis y riesgos de `agile-coach/` que incluyen hora de ultima revision y referencia a la entrada mas reciente de `changelog/` consultada.
- Beneficio: hace visible si el area de proceso esta describiendo el presente o reutilizando contexto historico como si fuera actual.
- Tradeoffs: requiere disciplina minima al redactar cada documento.
- Riesgos y dependencias: si la fecha de revision no se actualiza, la metrica pierde valor y el documento puede parecer vigente sin estarlo.

### H. Separar el estado operativo del backlog del estado de refinamiento
- Usar `Estado operativo:` para items enlazados a issue y `Estado de backlog:` para items aun en refinamiento o sin issue.
- Beneficio: reduce ambiguedad entre trabajo ejecutable y priorizacion interna, y simplifica la lectura del backlog para `product-manager`, `developer-teams` y `qa-teams`.
- Tradeoffs: exige actualizar la estructura de `product-manager/product-backlog.md` y mantenerla coherente en cada iteracion.
- Riesgos y dependencias: si se vuelve a mezclar la semantica de ambos campos, reaparecera la ambiguedad y la mejora perdera valor operativo.

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
