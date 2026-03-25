# Riesgos actuales de coordinacion

Fecha de escritura: 2026-03-25 23:01:12 UTC
Changelog consultado: changelog/2026-03-25.md
Vigencia de ejemplos: vigente

## Objetivo
Registrar los riesgos de coordinacion que siguen activos tras los ajustes de proceso ya aplicados y dejar visible que senales deben vigilar los equipos.

## Riesgo 1: issues `validado` que permanecen abiertas sin cierre administrativo claro
- Senal observable: issue abierta con validacion de QA pero sin comentario estructurado de bloqueo, responsable siguiente y paso operativo.
- Impacto: distorsiona la lectura del backlog abierto y oculta si el atasco es real o solo administrativo.
- Mitigacion acordada: comentario obligatorio de `product-manager` con `Bloqueo actual:`, `Siguiente responsable:`, `Siguiente paso operativo:` y `Estado de integracion:`.
- Ejemplo historico util: la secuencia de `PB-001`/issue `#1` demostro que una entrega puede pasar de valida a integrada en poco tiempo y volver obsoletos los ejemplos de proceso si no se revalidan contra el ultimo `changelog/`.

## Riesgo 2: deriva en el formato de handoff entre iteraciones
- Senal observable: comentarios de entrega o revision con el estado operativo incrustado en texto libre o con claves distintas entre issues.
- Impacto: aumenta el tiempo de lectura, complica revalidaciones y reduce la calidad de metricas ligeras.
- Mitigacion acordada: plantillas literales minimas para `developer-teams`, `qa-teams` y seguimiento administrativo de `product-manager`.

## Riesgo 3: reaparicion de conflictos por `changelog/` en ramas tecnicas largas
- Senal observable: una rama tecnica permanece abierta mientras `main` sigue recibiendo entradas nuevas en `changelog/`.
- Impacto: QA vuelve a asumir conflictos administrativos antes de validar funcionalmente.
- Mitigacion acordada: resincronizar la rama con `main` antes de cada nuevo handoff a QA.

## Riesgo 4: activacion tardia de `doc-teams`
- Senal observable: entrega con `Impacto documental: si` y `Estado operativo: validado` sin movimiento posterior en documentacion.
- Impacto: el producto validado queda operativamente desalineado de su documentacion oficial.
- Mitigacion acordada: usar `Impacto documental: si` como disparador y revisar esta cola al cierre de cada entrega validada.

## Riesgo 5: arranque de desarrollo sobre issues aun no operables
- Senal observable: la issue se mueve a `en desarrollo` sin incluir `Backlog:`, `Historia de usuario:`, `Caso de uso:`, `Criterios de aceptacion:` o `Dependencias:`.
- Impacto: se trasladan ambiguedades funcionales al trabajo tecnico y se desperdicia capacidad de desarrollo en aclaraciones tardias.
- Mitigacion acordada: paquete minimo obligatorio de issue antes de abrir rama y bloqueo explicito de inicio si falta ese contexto.

## Riesgo 6: deriva en el formato del `changelog/` por seguir ejemplos historicos
- Senal observable: nuevas entradas sin hora exacta o con estructura copiada de ficheros anteriores a la regla vigente.
- Impacto: baja la calidad de la trazabilidad diaria y aumenta la interpretacion manual entre roles.
- Mitigacion acordada: mantener un formato claro, cronologico y consistente con el resto de entradas existentes en `changelog/`, tratando los ficheros historicos solo como contexto del nivel de detalle.

## Riesgo 7: arranque ambiguo de issues en desarrollo
- Senal observable: la issue pasa a trabajo activo sin comentario minimo con `Rama:` y `Estado operativo: en desarrollo`.
- Impacto: se pierde visibilidad rapida sobre que rama esta activa y se debilita el control del limite de ramas tecnicas.
- Mitigacion acordada: comentario de arranque obligatorio y literal al tomar la issue.

## Riesgo 8: QA consume tiempo en entregas sin gate previo superado
- Senal observable: la revision funcional empieza aunque falte la plantilla minima de handoff o existan conflictos evitables con `main`.
- Impacto: QA invierte capacidad en reconstruir contexto o diagnosticar integracion antes de validar comportamiento.
- Mitigacion acordada: comprobacion previa obligatoria y cierre con `Estado operativo: no validado` cuando el handoff no sea operable.

## Riesgo 9: backlog visible con estados operativos desfasados
- Senal observable: el cuerpo de la issue sigue mostrando `Estado operativo: nuevo` aunque existan comentarios posteriores con `en desarrollo`, `listo para qa`, `no validado` o `validado`.
- Impacto: la priorizacion y la lectura rapida del backlog se apoyan en un estado engañoso o incompleto.
- Mitigacion acordada: actualizar el `Estado operativo:` del cuerpo de la issue en cada transicion operativa relevante.

## Riesgo 10: documentacion adelantada respecto a la integracion real
- Senal observable: una issue queda `validado` con `Impacto documental: si`, pero la rama tecnica sigue abierta o la capacidad aun no existe en `main`.
- Impacto: la documentacion oficial puede describir un comportamiento todavia no integrado y crear incoherencia entre manuales, backlog visible y producto real.
- Mitigacion acordada: activar a `doc-teams` solo cuando la entrega validada ya este fusionada en `main` y reforzar la prioridad de merge tras QA.

## Riesgo 11: backlog persistente desactualizado o sin priorizacion visible
- Senal observable: `product-manager/product-backlog.md` contiene items, pero sus estados o referencias no reflejan el ultimo estado operativo real de las issues enlazadas.
- Impacto: la priorizacion compartida sigue existiendo, pero se apoya en una fotografia desfasada del trabajo y pierde utilidad para triaje o cierre.
- Mitigacion acordada: mantener un backlog vivo, priorizado, trazable y sincronizado con el ultimo estado operativo visible de cada issue enlazada.
- Ejemplo historico util: `PB-001` ayudo a detectar la necesidad de sincronizar el item del backlog con el ultimo estado de la issue enlazada en la misma iteracion.

## Riesgo 12: entradas de `changelog` firmadas con etiquetas no vinculadas a un rol
- Senal observable: firmas como `codex` o nombres de herramienta en lugar del nombre del rol activado explicitamente.
- Impacto: se debilita la auditabilidad diaria y cuesta atribuir cada cambio de proceso a su responsable operativo.
- Mitigacion acordada: firmar siempre con el rol correspondiente y tratar cualquier etiqueta generica como desviacion del proceso.

## Riesgo 13: deriva entre documentos de proceso
- Senal observable: una regla de handoff, un estado operativo o una plantilla literal cambia en un documento pero no en los `AGENTS.md` afectados o en `acuerdos-operativos.md`.
- Impacto: cada equipo puede acabar siguiendo una version distinta de la misma regla, lo que incrementa retrabajo, preguntas de aclaracion y riesgo de ejecutar flujos incompatibles entre si.
- Mitigacion acordada: tratar `acuerdos-operativos.md` como referencia canonica y exigir que cualquier cambio operativo se propague en la misma iteracion a los `AGENTS.md` afectados y al `changelog/`.

## Riesgo 14: backlog visible desalineado respecto al ciclo de vida de la issue
- Senal observable: la issue ya paso a `en desarrollo`, `listo para qa`, `validado` o `cerrado`, pero el item correspondiente del backlog conserva un estado anterior.
- Impacto: `product-manager`, `developer-teams` y `qa-teams` leen estados distintos segun el artefacto consultado, lo que complica la priorizacion y la lectura rapida del flujo.
- Mitigacion acordada: sincronizar el item de backlog en la misma iteracion en que la issue cambie de estado operativo visible.

## Riesgo 15: ejemplos de proceso tratados como vigentes sin revalidacion
- Senal observable: un analisis, mejora o riesgo cita una issue, un backlog item o un estado operativo concreto sin verificar la entrada mas reciente de `changelog/` sobre `main`.
- Impacto: una fotografia historica puede ser leida como si fuera estado actual y orientar mal la priorizacion o el cierre administrativo.
- Mitigacion acordada: anclar cada documento de `agile-coach/` a una hora de escritura y contrastar la referencia viva antes de publicar ejemplos concretos como evidencia vigente.

## Riesgo 16: backlog con semantica mezclada entre ejecucion y refinamiento
- Senal observable: el backlog usa el mismo campo o la misma etiqueta para items enlazados a issue y para items que solo estan en refinamiento.
- Impacto: se pierde la distincion entre trabajo ejecutable y trabajo aun no operable, lo que complica la priorizacion y la lectura rapida del flujo.
- Mitigacion acordada: usar `Estado operativo:` para items enlazados a issue y `Estado de backlog:` para iniciativas que siguen en definicion o no tienen issue.

## Riesgo 17: artefactos de proceso que se quedan atras respecto al ultimo changelog relevante
- Senal observable: un documento de `agile-coach/` sigue citando como vigente una fotografia anterior aunque la entrada mas reciente de `changelog/` ya cambio el estado de la misma issue, rama o handoff.
- Impacto: el analisis puede describir un presente desfasado y empujar decisiones de coordinacion basadas en evidencia vieja.
- Mitigacion acordada: refrescar o marcar como historicos los documentos de proceso cuando un `changelog/` posterior invalide la fotografia citada.
