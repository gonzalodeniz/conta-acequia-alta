# Metricas ligeras de flujo

Fecha de escritura: 2026-03-26 23:00:44 UTC
Changelog consultado: changelog/2026-03-26.md
Vigencia de ejemplos: vigente

## Objetivo
Medir si el proceso entre equipos mejora en velocidad, claridad y estabilidad sin crear una carga operativa innecesaria.

## Metricas recomendadas

## 1. Tiempo hasta inicio de desarrollo
- Definicion: tiempo desde la creacion de la issue hasta el primer comentario o evidencia de `Estado operativo: en desarrollo`.
- Senal que aporta: detecta espera excesiva antes de empezar trabajo comprometido.

## 2. Tiempo de espera en QA
- Definicion: tiempo desde `Estado operativo: listo para qa` hasta el comentario de QA con `validado` o `no validado`.
- Senal que aporta: detecta cuello de botella en validacion.

## 3. Tasa de revalidacion
- Definicion: porcentaje de issues que pasan al menos una vez por `Estado operativo: no validado`.
- Senal que aporta: detecta calidad insuficiente del handoff o criterios poco claros antes de desarrollo.

## 4. Tiempo de cierre tras validacion
- Definicion: tiempo desde `Estado operativo: validado` hasta cierre de la issue por `product-manager`.
- Senal que aporta: detecta acumulacion de trabajo ya aceptado pero no cerrado.

## 4 bis. Tiempo de integracion tras validacion
- Definicion: tiempo desde `Estado operativo: validado` hasta que la rama tecnica queda fusionada en `main`.
- Senal que aporta: detecta limbo post-QA antes de merge, borrado de rama y activacion de documentacion dependiente.

## 5. Tasa de impacto documental declarado
- Definicion: porcentaje de entregas de desarrollo que marcan `Impacto documental: si`.
- Senal que aporta: ayuda a dimensionar la carga real de `doc-teams`.

## 6. Entregas que llegan a QA con conflicto contra `main`
- Definicion: numero o porcentaje de entregas revisadas por QA que presentan conflictos de integracion con `main`.
- Senal que aporta: detecta fallos de sincronizacion entre la rama tecnica y la rama de referencia del repositorio.

## 7. Issues devueltas por falta de contexto minimo
- Definicion: numero o porcentaje de issues que `developer-teams` no puede iniciar porque faltan campos obligatorios de contexto operativo.
- Senal que aporta: detecta si el cuello de botella real esta en refinamiento funcional antes de abrir trabajo tecnico.

## 8. Entregas rechazadas por handoff incompleto o sin integracion limpia
- Definicion: numero o porcentaje de revisiones que QA cierra en `no validado` porque falta la plantilla minima de entrega o porque la rama no integra limpia con `main`.
- Senal que aporta: detecta si el problema esta en la preparacion operativa del handoff antes de revisar funcionalidad.

## 9. Issues con estado visible desalineado
- Definicion: numero o porcentaje de issues abiertas cuyo cuerpo no refleja el mismo `Estado operativo:` que la ultima transicion operativa registrada en comentarios.
- Senal que aporta: detecta perdida de fiabilidad del backlog visible y deriva entre fuente resumida y flujo real.

## 10. Tasa de divergencia documental
- Definicion: numero de veces que una revision de proceso detecta que una misma regla aparece distinta entre `acuerdos-operativos.md` y los `AGENTS.md` afectados.
- Senal que aporta: mide si el cambio de proceso se esta propagando de forma coherente o si la documentacion esta empezando a bifurcarse.

## 11. Items de backlog desalineados con la issue
- Definicion: numero o porcentaje de items de `product-manager/product-backlog.md` enlazados a una issue cuyo estado visible no coincide con el ultimo estado operativo registrado en GitHub.
- Senal que aporta: detecta si el backlog sigue la realidad del flujo o si ha quedado congelado en un estado anterior.

## 12. Tiempo hasta checkpoint administrativo tras `validado`
- Definicion: tiempo desde el comentario de `qa-teams` con `Estado operativo: validado` hasta el comentario administrativo de `product-manager` cuando la issue permanece abierta.
- Senal que aporta: detecta cuanto tiempo pasa una issue aceptada en limbo antes de que quede claro si sigue abierta por integracion, dependencia o mero cierre administrativo.

## 13. Vigencia de referencias de proceso
- Definicion: porcentaje de documentos de `agile-coach/` que incluyen hora de ultima revision y referencia a la entrada mas reciente de `changelog/` consultada antes de publicar un analisis, riesgo o mejora.
- Senal que aporta: detecta cuando un documento usa ejemplos caducados como si fueran estado vigente y ayuda a vigilar la frescura de los artefactos de coordinacion.

## 14. Coherencia del campo de estado en backlog
- Definicion: porcentaje de items de `product-manager/product-backlog.md` que usan `Estado operativo:` cuando estan enlazados a issue y `Estado de backlog:` cuando siguen en refinamiento, sin mezclar ambas semanticas.
- Senal que aporta: detecta si el backlog distingue claramente entre trabajo ejecutable y priorizacion interna.

## 15. Tiempo de refresco de artefactos de proceso
- Definicion: tiempo transcurrido entre una entrada de `changelog/` sobre `main` que cambia el estado de una issue, rama o handoff citado en un documento de `agile-coach/` y la actualizacion de ese documento o su marcado como historico.
- Senal que aporta: detecta si la documentacion de proceso se mantiene al ritmo de la operativa real o si empieza a describir un pasado ya superado.

## 16. Latencia de refresco del backlog
- Definicion: tiempo transcurrido entre una transicion de estado de una issue en GitHub y la actualizacion del item enlazado en `product-manager/product-backlog.md`.
- Senal que aporta: detecta si el backlog sigue la realidad del flujo o si queda atras frente a la issue que describe.

## Regla de uso
- Revisar estas metricas al cierre de cada iteracion relevante o cuando se acumulen varias issues cerradas.
- Si una metrica empeora de forma sostenida, revisar primero el handoff asociado antes de cambiar responsabilidades entre equipos.
