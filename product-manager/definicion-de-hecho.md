# Definicion de hecho

## Objetivo
Establecer el minimo funcional y operativo que una issue debe cumplir para considerarse lista para validacion y, despues, para cierre administrativo.

## Para que una issue este lista para desarrollo
- Existe trazabilidad explicita con `Backlog:`, `Historia de usuario:` y `Caso de uso:`.
- El cuerpo de la issue incluye `Criterios de aceptacion:`, `Dependencias:` y `Estado operativo: nuevo`.
- El alcance es verificable y no mezcla multiples objetivos funcionales incompatibles en una sola entrega.
- Las dependencias abiertas de producto estan visibles.

## Para que una entrega de `developer-teams` este lista para QA
- La issue contiene un comentario de handoff con los campos literales definidos en `AGENTS.md` y `agile-coach/acuerdos-operativos.md`.
- Los criterios de aceptacion de la issue tienen correspondencia clara con la entrega realizada.
- Las limitaciones conocidas y la deuda tecnica identificada estan explicitadas.
- Existe evidencia de verificacion tecnica ejecutada por `developer-teams`.
- El `Estado operativo:` del cuerpo de la issue esta actualizado a `listo para qa`.

## Para considerar una issue funcionalmente validada
- `qa-teams` deja comentario estructurado con resultado `validado`.
- Los criterios de aceptacion quedan cubiertos o cualquier excepcion esta expresamente aceptada y trazada.
- No quedan defectos bloqueantes abiertos sobre el alcance comprometido.

## Para cierre administrativo por `product-manager`
- Existe validacion explicita de `qa-teams`.
- La issue mantiene trazabilidad con backlog, historia y caso de uso.
- El item correspondiente del backlog persistente refleja el mismo estado operativo visible en la issue.
- Si la integracion en `main` ya se realizo, `product-manager` puede cerrar la issue actualizando su cuerpo a `Estado operativo: cerrado`.
- Si la issue sigue abierta tras `validado`, debe existir comentario administrativo con `Bloqueo actual:`, `Siguiente responsable:`, `Siguiente paso operativo:` y `Estado de integracion:`.
- Si la entrega tiene impacto documental y ya fue integrada en `main`, debe quedar visible que `doc-teams` es siguiente consumidor del resultado.

## Criterios de exclusion
- Una issue no se considera hecha solo porque exista implementacion tecnica sin validacion de `qa-teams`.
- Una issue no se considera hecha si el estado operativo del cuerpo esta desalineado con el ultimo comentario estructurado.
- Una issue no se considera hecha si la deuda tecnica critica detectada por otros equipos desaparece del backlog sin decision explicita.
