# Product Backlog

## Contexto
La vision vigente define una aplicacion web para gestionar la contabilidad de una comunidad de vecinos con foco en transparencia, control economico, presupuestos y soporte al cierre anual. A fecha de 2026-03-23 la primera entrega del registro basico de movimientos (`PB-001`) ya fue validada por `qa-teams` e integrada en `main`, pero sigue existiendo un hueco funcional frente a la vision: la ayuda guiada de clasificacion contable basada en el Plan General de Contabilidad todavia no esta trazada como entrega independiente y debe mantenerse visible en backlog.

## Criterios de priorizacion
- Valor de negocio inmediato para administradores y vecinos.
- Reduccion de riesgo funcional y de ambiguedad para `developer-teams`.
- Dependencias entre capacidades clave del producto.
- Capacidad de validacion clara por parte de `qa-teams`.

## Backlog priorizado

### PB-001 - Registrar gastos e ingresos de la comunidad
- Descripcion: Permitir que el administrador registre movimientos economicos con fecha, concepto, importe, tipo de movimiento e identificacion minima para su seguimiento.
- Prioridad: Alta
- Valor de negocio: Alto. Sin registro fiable de movimientos no existe base contable para el resto del producto.
- Historia de usuario: HU-001
- Caso de uso: CU-001
- Issue GitHub: #1
- Criterios de aceptacion:
  - El administrador puede crear un gasto indicando fecha, concepto, categoria e importe.
  - El administrador puede crear un ingreso indicando fecha, concepto, categoria e importe.
  - Cada movimiento queda identificado de forma unica y visible para su consulta posterior.
  - No se permite guardar movimientos sin los campos minimos obligatorios definidos por negocio.
  - El sistema diferencia claramente entre gasto e ingreso en el registro.
- Dependencias: Ninguna
- Estado: cerrado

### PB-009 - Guiar la clasificacion contable con PGC simplificado
- Descripcion: Permitir que el administrador reciba ayuda funcional para asociar una cuenta contable adecuada del Plan General de Contabilidad de Espana al registrar un movimiento, priorizando cuentas habituales de una comunidad de vecinos y manteniendo fuera del foco las cuentas de amortizacion.
- Prioridad: Alta
- Valor de negocio: Alto. Cierra la brecha entre la vision del producto y la entrega actual de registro basico, reduciendo errores de imputacion y mejorando la calidad de la informacion contable.
- Historia de usuario: HU-009
- Caso de uso: CU-009
- Issue GitHub: #6
- Criterios de aceptacion:
  - El administrador recibe ayuda para clasificar un movimiento con una cuenta del Plan General de Contabilidad de Espana.
  - La ayuda prioriza una lista inicial de cuentas habituales para comunidades de vecinos, incluyendo al menos banco, caja, proveedores, acreedores, suministros y reparaciones.
  - La ayuda diferencia sugerencias segun el tipo de movimiento, como gasto o ingreso.
  - El administrador puede confirmar una cuenta sugerida o elegir otra opcion permitida dentro del alcance funcional definido.
  - La ayuda no prioriza ni sugiere cuentas de amortizacion en el alcance actual.
  - La cuenta asociada al movimiento queda visible para su consulta posterior.
- Dependencias: PB-001
- Estado: nuevo

### PB-002 - Consultar el libro de asientos contables
- Descripcion: Permitir revisar el historial de movimientos registrados en un libro ordenado y filtrable por periodo y tipo de movimiento.
- Prioridad: Alta
- Valor de negocio: Alto. Aporta trazabilidad y visibilidad operativa sobre la contabilidad diaria.
- Historia de usuario: HU-002
- Caso de uso: CU-002
- Issue GitHub: #2
- Criterios de aceptacion:
  - El administrador puede consultar todos los movimientos registrados en orden cronologico.
  - El administrador puede filtrar por rango de fechas.
  - El administrador puede distinguir visualmente gastos e ingresos dentro del listado.
  - El libro muestra como minimo fecha, concepto, categoria, tipo e importe de cada movimiento.
  - Si no existen movimientos en el periodo consultado, el sistema lo comunica sin ambiguedad.
- Dependencias: PB-001
- Estado: nuevo

### PB-003 - Visualizar resumen financiero del periodo
- Descripcion: Ofrecer un resumen consolidado con total de ingresos, total de gastos y saldo para un periodo seleccionable.
- Prioridad: Alta
- Valor de negocio: Alto. Permite entender el estado economico sin revisar asiento por asiento.
- Historia de usuario: HU-003
- Caso de uso: CU-003
- Issue GitHub: #3
- Criterios de aceptacion:
  - El administrador puede consultar un resumen financiero por periodo.
  - El resumen muestra total de ingresos, total de gastos y saldo resultante.
  - Los totales del resumen coinciden con los movimientos registrados del periodo.
  - El sistema permite al menos consultar el periodo mensual y anual.
  - Si no hay movimientos en el periodo, el resumen devuelve importes a cero y un mensaje claro.
- Dependencias: PB-001
- Estado: nuevo

### PB-004 - Permitir acceso de solo lectura para vecinos
- Descripcion: Habilitar que un vecino consulte informacion economica de la comunidad en modo solo lectura, con un alcance visible y verificable por negocio.
- Prioridad: Alta
- Valor de negocio: Alto. Es la pieza principal de transparencia para el usuario no administrador.
- Historia de usuario: HU-004
- Caso de uso: CU-004
- Issue GitHub: #7
- Criterios de aceptacion:
  - Un vecino puede consultar un resumen economico mensual y anual en modo solo lectura.
  - Un vecino puede consultar el listado de movimientos visibles para la comunidad mostrando al menos fecha, concepto, categoria, tipo e importe.
  - Un vecino no puede crear, editar ni borrar movimientos.
  - El sistema diferencia claramente el alcance de consulta del vecino frente al del administrador.
  - Si un vecino intenta acceder a una accion de gestion, el sistema lo bloquea de forma explicita.
  - Si todavia no existe informacion economica disponible, el sistema lo comunica con un mensaje claro sin exponer acciones de gestion.
- Dependencias: PB-002, PB-003
- Estado: nuevo

### PB-008 - Gestionar presupuestos anuales de la comunidad
- Descripcion: Permitir que el administrador defina y consulte un presupuesto anual con partidas previstas de ingresos y gastos para compararlo despues con la ejecucion real de la comunidad.
- Prioridad: Media
- Valor de negocio: Alto. Traduce a plan economico una capacidad explicitamente mencionada en la vision y facilita la toma de decisiones antes del cierre anual.
- Historia de usuario: HU-008
- Caso de uso: CU-008
- Issue GitHub: #4
- Criterios de aceptacion:
  - El administrador puede crear un presupuesto para un ejercicio anual concreto.
  - El presupuesto permite registrar partidas previstas diferenciando ingresos y gastos.
  - El sistema muestra para cada partida al menos concepto, tipo e importe previsto.
  - El administrador puede consultar el total presupuestado de ingresos, gastos y saldo previsto del ejercicio.
  - El presupuesto queda identificado por ejercicio y disponible para consulta posterior.
  - El sistema comunica de forma clara cuando un ejercicio todavia no tiene presupuesto definido.
- Dependencias: PB-001, PB-003
- Estado: nuevo

### PB-005 - Importar movimientos desde una hoja de calculo
- Descripcion: Permitir una carga inicial de movimientos historicos desde un formato tabular acordado para acelerar la adopcion.
- Prioridad: Media
- Valor de negocio: Alto. Reduce barrera de entrada y evita migraciones manuales lentas.
- Historia de usuario: HU-005
- Caso de uso: CU-005
- Issue GitHub: #8
- Criterios de aceptacion:
  - El administrador puede cargar una plantilla oficial de importacion con las columnas `fecha`, `tipo`, `concepto`, `categoria` e `importe`, y una columna opcional `referencia_externa`.
  - El sistema valida los campos minimos requeridos antes de importar y rechaza filas cuyo `tipo` no sea gasto o ingreso.
  - El sistema informa cuantas filas se importan correctamente y cuales fallan.
  - Las filas invalidas quedan identificadas con el motivo funcional del rechazo.
  - Los movimientos importados pasan a ser consultables en el libro de asientos y en el resumen financiero.
- Dependencias: PB-001, PB-002
- Estado: nuevo

### PB-006 - Preparar el cierre contable anual
- Descripcion: Facilitar una revision funcional del ejercicio anual con sus totales y trazabilidad, sin incluir bloqueo tecnico del ejercicio en esta primera iteracion.
- Prioridad: Media
- Valor de negocio: Alto. Responde a una necesidad clave de gestion formal de la comunidad.
- Historia de usuario: HU-006
- Caso de uso: CU-006
- Issue GitHub: #9
- Criterios de aceptacion:
  - El administrador puede seleccionar un ejercicio anual para revisar su cierre.
  - El sistema muestra el total anual de ingresos, gastos y saldo final del ejercicio.
  - El cierre identifica los meses del ejercicio sin movimientos o con posibles vacios de registro.
  - El cierre ofrece una vista de detalle o trazabilidad suficiente para llegar a los movimientos que componen el ejercicio.
  - El resultado del cierre puede usarse como base para compartir informacion con vecinos, sin bloquear nuevas correcciones contables en esta primera version.
  - El ejercicio cerrado conserva trazabilidad con los movimientos que lo componen.
- Dependencias: PB-002, PB-003
- Estado: nuevo

### PB-007 - Enviar notificaciones y recordatorios operativos
- Descripcion: Notificar hitos relevantes como fechas de pago, reuniones o revisiones de cierre para mejorar seguimiento y comunicacion.
- Prioridad: Media
- Valor de negocio: Medio. Incrementa el uso recurrente, pero no desbloquea la base contable.
- Historia de usuario: HU-007
- Caso de uso: CU-007
- Issue GitHub: no creada; falta refinamiento funcional
- Criterios de aceptacion:
  - El administrador puede definir al menos un recordatorio asociado a una fecha relevante.
  - El sistema muestra el mensaje y la fecha del recordatorio.
  - El vecino solo visualiza notificaciones que le apliquen por negocio.
  - El administrador puede consultar el estado de cada recordatorio configurado.
  - Las notificaciones no alteran la informacion contable registrada.
- Dependencias: PB-004
- Estado: refinamiento pendiente

## Dependencias abiertas de producto
- Falta concretar la lista inicial canonica de cuentas del Plan General de Contabilidad que se sugeriran por defecto en `PB-009`.
- Falta decidir si el presupuesto anual necesitara versionado por revisiones o si el MVP aceptara un unico presupuesto vigente por ejercicio.
- Falta definir si el acceso de vecinos debe incluir todos los movimientos visibles o solo los marcados como consolidados cuando el producto introduzca estados de revision.

## Riesgos de producto
- Existe una brecha entre la vision y la entrega real de `PB-001`: el registro basico ya esta integrado, pero la clasificacion contable asistida sigue pendiente y puede inducir una falsa sensacion de cobertura funcional completa.
- Si se intenta abordar importacion, vecinos y cierre anual sin entregar antes el registro de movimientos y la consulta del libro, aumentara la ambiguedad de validacion.
- Si no se incorpora presupuestos al backlog ejecutable, la vision quedara parcialmente traducida y se perdera trazabilidad de una capacidad de negocio ya comprometida.
- Si se deja sin cerrar la politica inicial de visibilidad para vecinos, `developer-teams` y `qa-teams` pueden interpretar alcances distintos sobre `PB-004`.

## Preguntas abiertas
- Se considera obligatorio soportar presupuestos en el MVP o se posponen a una fase posterior del roadmap?
- El acceso de vecinos debera evolucionar en el futuro hacia una publicacion selectiva de movimientos cuando existan estados de conciliacion o incidencias sensibles?
- La importacion inicial debera admitir varias fuentes equivalentes ademas de la plantilla oficial?
- Que listado inicial de cuentas del Plan General de Contabilidad se considera canonico para la ayuda de clasificacion de `PB-009`?
- El presupuesto anual necesita permitir ajustes posteriores sobre el mismo ejercicio o basta con una primera version editable sin historico en el alcance actual?
