# Mejoras de proceso propuestas

## Mejora 1: introducir estados operativos comunes en la issue
### Problema detectado
No existe un lenguaje operativo unico para saber en que punto exacto del flujo esta cada issue.

### Propuesta
Estandarizar estos estados operativos en comentarios y handoffs:
- `nuevo`
- `en desarrollo`
- `listo para qa`
- `no validado`
- `validado`
- `cerrado`

### Impacto esperado
- Reduce ambiguedad sobre el siguiente responsable de actuar.
- Facilita la priorizacion de `developer-teams` sobre trabajo ya empezado.
- Hace mas auditable el flujo real entre equipos.

### Tradeoffs
- Añade una pequena disciplina documental por iteracion.

### Riesgos y dependencias
- Requiere que todos los roles reutilicen la misma nomenclatura.
- Conviene mantenerlo simple y no convertirlo en burocracia adicional.
- Si el backlog persistente no refleja el mismo estado que la issue, la mejora pierde parte de su valor y conviene sincronizar ambos artefactos en la misma iteracion.

## Mejora 2: fijar un paquete minimo de handoff a QA
### Problema detectado
El contexto entregado por desarrollo a QA no tiene un contrato minimo comun.

### Propuesta
Obligar a que el comentario final de `developer-teams` antes de QA incluya:
- rama revisable
- resumen de lo realizado
- decisiones relevantes
- limitaciones conocidas
- comandos de verificacion ejecutados
- impacto documental: `si` o `no`
- estado operativo: `listo para qa`

### Impacto esperado
- QA reduce tiempo de reconstruccion del contexto.
- Mejora la calidad y repetibilidad de las revisiones.
- `doc-teams` recibe una senal temprana y verificable de impacto documental.

### Tradeoffs
- Desarrollo debe ser mas explicito al cerrar cada entrega.

### Riesgos y dependencias
- Si se convierte en texto largo no estructurado, se pierde el beneficio.
- Debe mantenerse como checklist breve.

## Mejora 3: explicitar el ciclo de revalidacion
### Problema detectado
No hay una regla clara para volver de `no validado` a una nueva revision.

### Propuesta
Mantener la misma issue y la misma rama del trabajo mientras siga siendo el mismo alcance. Tras un `no validado`:
1. `developer-teams` corrige en la misma rama.
2. Publica un nuevo comentario de entrega con cambios realizados y evidencias nuevas.
3. Marca de nuevo `estado operativo: listo para qa`.
4. `qa-teams` realiza una nueva revision sobre esa misma issue.

### Impacto esperado
- Conserva trazabilidad completa del ciclo de correccion.
- Reduce dispersion de contexto entre ramas o issues duplicadas.

### Tradeoffs
- La issue puede acumular varios comentarios de iteraciones.

### Riesgos y dependencias
- Si el alcance cambia materialmente, `product-manager` debe decidir si sigue siendo la misma issue o si hace falta una nueva.

## Mejora 4: fijar el disparador de `doc-teams`
### Problema detectado
La documentacion depende de interpretacion y puede desalinearse respecto al estado real de la entrega.

### Propuesta
Activar a `doc-teams` cuando se cumplan ambas condiciones:
1. `qa-teams` ha dejado `validado`.
2. La entrega indica `impacto documental: si`.

Si el impacto documental es `no`, `doc-teams` no necesita intervenir en esa iteracion salvo solicitud expresa.

### Impacto esperado
- Se evita documentar funcionalidades aun inestables.
- Se reduce trabajo documental innecesario.
- Mejora la sincronizacion entre entrega validada y documentacion oficial.

### Tradeoffs
- Desarrollo debe evaluar con criterio si existe impacto documental.

### Riesgos y dependencias
- Si `developer-teams` marca mal el impacto documental, el flujo puede omitir documentacion necesaria.
- Conviene que QA senale el riesgo si detecta impacto documental no declarado.

## Mejora 5: introducir metricas ligeras de flujo
### Problema detectado
El repositorio no define como medir si los cambios de proceso mejoran realmente la coordinacion.

### Propuesta
Seguir de forma ligera estas metricas:
- tiempo desde issue abierta hasta `en desarrollo`
- tiempo desde `listo para qa` hasta resultado de QA
- porcentaje de issues que requieren revalidacion
- tiempo desde `validado` hasta cierre por `product-manager`

### Impacto esperado
- Permite detectar cuellos de botella reales.
- Da criterio para decidir si el bloqueo esta en desarrollo, QA o cierre.

### Tradeoffs
- Requiere disciplina minima en comentarios y fechas.

### Riesgos y dependencias
- Sin estados operativos comunes, estas metricas pierden calidad.

## Mejora 6: separar la trazabilidad del `changelog/` de la entrega tecnica del issue
### Problema detectado
El `changelog/` debe actualizarse en `main`, pero no existia una regla operativa suficiente para evitar que esa actividad contaminara ramas tecnicas o generara conflictos de integracion.

### Propuesta
- Mantener el `changelog/` solo en `main` y dejar explicito que nunca forma parte de la entrega tecnica a QA.
- Si `developer-teams` o `qa-teams` actualizan `changelog/` mientras mantienen una rama abierta, deben sincronizar despues esa rama con `main` antes del siguiente handoff.

### Impacto esperado
- Reduce conflictos evitables en validacion e integracion.
- Evita que QA invierta tiempo en incidencias administrativas derivadas del registro diario.
- Mantiene la trazabilidad diaria sin mezclarla con el alcance tecnico del issue.

### Tradeoffs
- Obliga a un paso adicional de sincronizacion cuando una rama permanece abierta mas de un bloque de trabajo.

### Riesgos y dependencias
- Si los equipos olvidan resincronizar la rama tras actualizar `main`, el conflicto reaparecera.
- Requiere que la secuencia operativa de `developer-teams` explicite esa comprobacion antes de QA.

## Mejora 7: reforzar el checkpoint posterior a `validado`
### Problema detectado
Una issue puede quedar abierta tras `validado` sin dejar claro si el bloqueo es integracion, cierre administrativo o dependencia documental.

### Propuesta
Si `product-manager` mantiene abierta una issue ya `validado`, debe dejar en la propia issue:
- bloqueo actual
- siguiente responsable
- siguiente paso operativo

### Impacto esperado
- Evita que una issue validada siga abierta sin contexto accionable.
- Mejora la lectura real del backlog y del trabajo pendiente.
- Facilita a `agile-coach` y al resto de equipos detectar bloqueos de cierre en lugar de confundirlos con trabajo aun no aceptado.

### Tradeoffs
- Introduce una pequena disciplina administrativa adicional en el cierre.

### Riesgos y dependencias
- Si el comentario se vuelve ambiguo, reaparecera el mismo problema con mas texto pero sin mas claridad.

## Mejora 8: fijar una plantilla literal para comentarios de handoff
### Problema detectado
Los equipos ya comparten que informacion debe aparecer en las issues, pero no una plantilla literal estable que facilite localizarla y compararla entre iteraciones.

### Propuesta
- Exigir a `developer-teams` y `qa-teams` que reutilicen siempre las mismas claves literales y en el mismo orden para sus comentarios de handoff.
- Exigir a `product-manager` una plantilla administrativa minima cuando una issue siga abierta tras `validado`.

### Impacto esperado
- Reduce tiempo de lectura y reinterpretacion entre equipos.
- Mejora la trazabilidad de revalidaciones y cierres administrativos.
- Hace mas viable medir cumplimiento de handoffs y tiempos de espera por estado.

### Tradeoffs
- Introduce mas disciplina formal en los comentarios de issue.

### Riesgos y dependencias
- Si las plantillas se vuelven demasiado largas, los equipos pueden tender a rellenarlas de forma mecanica.
- Conviene mantener solo los campos necesarios para decidir el siguiente paso operativo.

## Mejora 9: fijar un paquete minimo para que una issue sea ejecutable
### Problema detectado
Una issue puede pasar a desarrollo sin dejar trazado de forma literal su origen funcional ni sus dependencias, obligando a reinterpretar documentos antes de empezar.

### Propuesta
Exigir que toda issue lista para `developer-teams` incluya y mantenga en este orden:
- `Backlog:`
- `Historia de usuario:`
- `Caso de uso:`
- `Criterios de aceptacion:`
- `Dependencias:`
- `Estado operativo: nuevo`

Ademas, `developer-teams` no debe iniciar implementacion si ese paquete minimo falta.

### Impacto esperado
- Reduce arranques en falso y preguntas repetidas antes de abrir rama.
- Hace mas visible si el bloqueo esta en refinamiento funcional y no en capacidad tecnica.
- Mejora la trazabilidad entre producto, desarrollo y QA desde el inicio del ciclo.

### Tradeoffs
- `product-manager` debe invertir algo mas de disciplina al abrir o refrescar issues.

### Riesgos y dependencias
- Si los campos se rellenan con texto ambiguo, el beneficio baja aunque el formato exista.
- Requiere que `developer-teams` frene el inicio cuando la issue no sea realmente operable.

## Mejora 10: sustituir la referencia historica de `changelog/` por una guia vigente
### Problema detectado
La referencia usada por los roles para el `changelog/` ya no refleja todas las reglas actuales, en especial la hora obligatoria por entrada.

### Propuesta
Definir y mantener una referencia estable de formato para `changelog/`, ya sea mediante una guia dedicada o mediante reglas explicitas en los `AGENTS.md`, con plantilla minima y nota explicita de que los ficheros historicos anteriores pueden no cumplir reglas introducidas despues.

### Impacto esperado
- Reduce contradicciones entre ejemplo historico y norma vigente.
- Facilita que todos los roles registren entradas homogeneas sin reinterpretar excepciones.
- Mejora la utilidad del `changelog/` como evidencia operativa y fuente de auditoria ligera.

### Tradeoffs
- Introduce un fichero documental adicional de mantenimiento sencillo.

### Riesgos y dependencias
- Si los roles siguen copiando formatos antiguos por inercia, la mejora tardara en consolidarse.
- Conviene actualizar tambien las referencias en todos los `AGENTS.md` afectados.

## Mejora 11: activar documentacion solo tras integracion real en `main`
### Problema detectado
`doc-teams` trabaja sobre `main`, pero podia activarse con una entrega `validado` todavia no fusionada, lo que fuerza a distinguir manualmente entre trabajo aceptado y comportamiento realmente disponible.

### Propuesta
- Cambiar el disparador de `doc-teams` para exigir simultaneamente `Estado operativo: validado`, `Impacto documental: si` y rama tecnica ya fusionada en `main`.
- Reforzar que `developer-teams` priorice el merge y el borrado de rama tras QA antes de iniciar una nueva issue, salvo bloqueo operativo documentado.

### Impacto esperado
- Evita que la documentacion oficial se adelante a la realidad integrada del producto.
- Reduce el tiempo en que una issue queda `validado` pero sin cierre operativo claro.
- Hace mas lineal la secuencia `validado -> merge -> documentacion -> cierre administrativo`.

### Tradeoffs
- `doc-teams` puede entrar un poco mas tarde en algunas iteraciones si el merge no se ejecuta con disciplina.

### Riesgos y dependencias
- Si `developer-teams` retrasa el merge sin dejar bloqueo explicito, la cola documental seguira esperando aunque QA ya haya aceptado la entrega.
- Requiere que `product-manager` mantenga visible el bloqueo cuando una issue validada no pueda cerrarse aun.

## Mejora 12: fijar un comentario minimo de arranque para `developer-teams`
### Problema detectado
El inicio de una issue exige informar rama y estado, pero no quedaba anclado a una plantilla literal unica.

### Propuesta
Obligar a que el arranque de una issue use al menos:
- `Rama:`
- `Estado operativo: en desarrollo`

### Impacto esperado
- Hace visible de inmediato que rama esta activa en cada issue.
- Facilita vigilar el limite de dos ramas tecnicas abiertas.
- Mejora la lectura del tiempo real hasta inicio de desarrollo.

### Tradeoffs
- Introduce un comentario adicional muy corto al comienzo del trabajo tecnico.

### Riesgos y dependencias
- Si el comentario se publica tarde, la metrica de arranque seguira distorsionada.
- Requiere que `developer-teams` mantenga actualizada la referencia si cambia de rama.

## Mejora 13: mantener sincronizado el `Estado operativo:` visible en la issue
### Problema detectado
El cuerpo de la issue puede seguir mostrando `Estado operativo: nuevo` aunque el trabajo real ya este en desarrollo, en QA o incluso `no validado`.

### Propuesta
Exigir que el rol que produzca cada transicion operativa actualice tambien el campo `Estado operativo:` del cuerpo de la issue en GitHub, ademas de dejar su comentario estructurado.

### Impacto esperado
- Mejora la lectura rapida del backlog abierto sin obligar a inspeccionar comentarios.
- Reduce errores de priorizacion sobre issues aparentemente `nuevo` que en realidad ya estan en curso o devueltas por QA.
- Hace mas util el estado operativo como fuente de verdad compartida.

### Tradeoffs
- Introduce una accion adicional de mantenimiento en GitHub para los roles que ya comentan la issue.

### Riesgos y dependencias
- Si la actualizacion del cuerpo se olvida, reaparece la divergencia entre backlog visible y flujo real.
- Conviene limitar la edicion al campo `Estado operativo:` para no reescribir contexto funcional por error.

## Mejora 14: reforzar la reentrega tras `no validado`
### Problema detectado
La regla de revalidacion existe, pero `developer-teams` aun podia interpretar que bastaba con corregir codigo sin reemitir un handoff completo ni reflejar el nuevo estado visible en la issue.

### Propuesta
Tras un `no validado`, exigir a `developer-teams` que:
- priorice esa misma issue frente a nuevas issues
- mantenga la misma rama mientras el alcance no cambie
- publique un nuevo comentario de entrega con la plantilla completa
- vuelva a actualizar el `Estado operativo:` del cuerpo de la issue a `listo para qa`

### Impacto esperado
- Reduce revalidaciones ambiguas o sin contexto incremental claro.
- Mantiene trazabilidad comparable entre la primera entrega y las reentregas.
- Evita que QA tenga que deducir si ya existe una nueva entrega realmente revisable.

### Tradeoffs
- La iteracion de correccion gana algo de disciplina documental.

### Riesgos y dependencias
- Si el alcance cambia materialmente y se mantiene la misma issue, la reentrega seguira siendo confusa.
- Requiere que `product-manager` abra una nueva issue cuando la correccion deje de ser el mismo alcance.

## Mejora 15: convertir el paquete minimo de handoff en gate explicito de QA
### Problema detectado
La plantilla de entrega existia, pero QA no tenia una regla suficientemente clara para rechazar desde el inicio una entrega incompleta o desalineada con `main`.

### Propuesta
Antes de validar funcionalmente, `qa-teams` debe comprobar que:
- el comentario de `developer-teams` incluye la plantilla minima de handoff
- la rama integra limpia con `main`

Si alguna condicion falla, QA debe cerrar la revision como `Estado operativo: no validado`.

### Impacto esperado
- Evita que QA asuma trabajo de reconstruccion del contexto.
- Separa defectos de proceso de defectos funcionales.
- Refuerza el cumplimiento real de las reglas de handoff.

### Tradeoffs
- Puede aumentar el numero de `no validado` por causas operativas en el corto plazo.

### Riesgos y dependencias
- Si QA aplica la regla de forma mecanica sin describir bien el bloqueo, desarrollo no tendra feedback accionable.
- Requiere que `developer-teams` siga tratando la sincronizacion con `main` como paso previo real y no solo declarado.

## Mejora 16: exigir un backlog vivo minimo antes de abrir nueva implementacion
### Problema detectado
`product-manager/product-backlog.md` puede quedar vacio o sin items priorizados aun cuando el flujo espera que el backlog sea la base de triaje y priorizacion.

### Propuesta
Antes de mover una issue a desarrollo, `product-manager` debe verificar que exista al menos un item priorizado y trazable en el backlog, y que toda issue activa quede vinculada a ese backlog.

### Impacto esperado
- Reduce arranques sin fuente de verdad funcional.
- Mejora la priorizacion entre issues nuevas y re-trabajo.
- Evita que desarrollo dependa de interpretacion oral o de memoria operativa.

### Tradeoffs
- `product-manager` debe mantener el backlog con un minimo de higiene continua.

### Riesgos y dependencias
- Si el backlog se convierte en un inventario sin priorizacion real, la mejora pierde valor.
- Requiere que `developer-teams` frene el inicio cuando no exista esa base funcional.

## Mejora 17: impedir firmas de `changelog` que no correspondan a un rol activado
### Problema detectado
Una entrada de `changelog` firmada con una etiqueta generica o de herramienta rompe la trazabilidad por rol.

### Propuesta
Exigir que cada entrada de `changelog/` se firme con el nombre del rol explicitamente activado en el prompt, y no con etiquetas genericas ni de herramienta.

### Impacto esperado
- Mejora la auditabilidad y la lectura historica del repositorio.
- Permite detectar rapidamente quien produjo cada actualizacion de proceso.
- Reduce ambiguedad cuando varias personas o agentes intervienen sobre `main`.

### Tradeoffs
- Introduce una validacion adicional muy pequeña al cerrar la tarea.

### Riesgos y dependencias
- Si la firma no coincide con el rol real, la trazabilidad diaria vuelve a degradarse.
- Conviene tratar cualquier firma generica como una desviacion del proceso y no como un caso valido.

## Mejora 18: sincronizar el backlog persistente con el ciclo de vida de la issue
### Problema detectado
El backlog ya no esta vacio, pero puede mostrar un estado desfasado respecto a la issue vinculada cuando esta cambia a `en desarrollo`, `listo para qa`, `validado` o `cerrado`.

### Propuesta
Exigir que `product-manager` actualice en la misma iteracion el item del backlog enlazado a cada issue cuando cambie su estado operativo visible. El backlog debe reflejar al menos el ultimo estado operativo conocido y no quedarse congelado en `listo para issue` o `refinamiento pendiente` una vez la issue ha avanzado.

### Impacto esperado
- Evita que el backlog muestre una fotografia historica en lugar del estado real del trabajo.
- Mejora la priorizacion de nuevas tareas y el seguimiento de trabajo ya empezado.

### Tradeoffs
- `product-manager` debe mantener la actualizacion de estado con mas disciplina para no degradar la fiabilidad del backlog.

### Riesgos y dependencias
- Si la actualizacion de estado se olvida aunque exista una issue validada o cerrada, el backlog vuelve a perder valor operativo.
- Requiere que el cierre administrativo y la actualizacion del backlog se hagan dentro de la misma iteracion de trabajo.

## Mejora 19: vigilar la latencia entre `validado` y el checkpoint administrativo
### Problema detectado
Una issue puede quedar `validado` y seguir abierta sin un comentario administrativo visible que aclare bloqueo, siguiente responsable y siguiente paso operativo.

### Propuesta
Medir el tiempo entre el comentario de `qa-teams` con `Estado operativo: validado` y el comentario administrativo de `product-manager` cuando la issue permanece abierta. Si la issue se cierra, registrar igualmente la latencia hasta el cierre administrativo para distinguir integracion y cierre.

### Impacto esperado
- Hace visible el limbo post-validacion antes de que se convierta en una espera larga o confusa.
- Ayuda a separar problemas de integracion de simples retrasos de cierre administrativo.
- Refuerza la lectura del backlog cuando una issue sigue abierta por motivos explicitos y no por olvido.

### Tradeoffs
- Añade una metrica operativa mas que revisar al cierre de cada iteracion.

### Riesgos y dependencias
- Requiere que `product-manager` mantenga el comentario administrativo o el cierre con disciplina.
- Si el estado visible de la issue no se actualiza a la vez, la metrica seguira siendo util pero el backlog visible seguira desalineado.
- Reduce la confusion entre backlog, issue y estado administrativo de cierre.
