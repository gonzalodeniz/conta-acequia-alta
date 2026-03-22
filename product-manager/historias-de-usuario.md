# Historias de usuario

## Criterios de redaccion
- Todas las historias se alinean con `vision-product.md`.
- Los criterios de aceptacion se redactan para validacion funcional por `qa-teams`.
- La trazabilidad se mantiene mediante los identificadores `HU-*`, `PB-*` y `CU-*`.

## HU-001 - Registro de movimientos contables
- Backlog relacionado: PB-001
- Caso de uso relacionado: CU-001
- Historia: Como administrador de la comunidad quiero registrar gastos e ingresos con ayuda para elegir la cuenta correcta del Plan General de Contabilidad de Espana para mantener la contabilidad actualizada, fiable y facil de clasificar.
- Criterios de aceptacion:
  - Puedo registrar un movimiento indicando fecha, concepto, categoria, tipo e importe.
  - El sistema me ayuda a seleccionar la cuenta contable correcta usando el Plan General de Contabilidad de Espana como referencia.
  - La ayuda me sugiere primero cuentas sencillas de gastos e ingresos y cuentas habituales de la comunidad, como banco, caja, proveedores y acreedores.
  - No se me presentan cuentas de amortizacion como opcion sugerida en este alcance.
  - El sistema distingue si el movimiento es gasto o ingreso.
  - No puedo guardar un movimiento si falta algun dato obligatorio.
  - Al registrar un movimiento, este queda disponible para consulta posterior.
  - El sistema muestra un resultado claro de alta correcta o rechazo.

## HU-002 - Consulta del libro de asientos
- Backlog relacionado: PB-002
- Caso de uso relacionado: CU-002
- Historia: Como administrador de la comunidad quiero consultar el libro de asientos para revisar el historial economico y detectar incidencias.
- Criterios de aceptacion:
  - Puedo ver los movimientos ordenados por fecha.
  - Puedo filtrar la consulta por rango de fechas.
  - En cada asiento veo fecha, concepto, categoria, tipo e importe.
  - Si no hay resultados, el sistema me lo indica de forma clara.
  - La informacion consultada refleja los movimientos realmente registrados.

## HU-003 - Resumen financiero por periodo
- Backlog relacionado: PB-003
- Caso de uso relacionado: CU-003
- Historia: Como administrador de la comunidad quiero ver un resumen financiero por periodo para conocer rapidamente ingresos, gastos y saldo.
- Criterios de aceptacion:
  - Puedo seleccionar al menos un periodo mensual o anual.
  - Veo total de ingresos, total de gastos y saldo del periodo.
  - Los importes del resumen coinciden con los movimientos del periodo consultado.
  - Si no hay movimientos, el sistema devuelve importes a cero.
  - El resumen se puede consultar sin revisar asiento por asiento.

## HU-004 - Transparencia para vecinos
- Backlog relacionado: PB-004
- Caso de uso relacionado: CU-004
- Historia: Como vecino quiero consultar informacion economica de la comunidad en modo solo lectura para entender la evolucion financiera sin depender de peticiones manuales.
- Criterios de aceptacion:
  - Puedo consultar la informacion economica que el producto defina como visible para vecinos.
  - No dispongo de acciones para modificar movimientos o configuraciones.
  - Puedo revisar al menos un resumen del estado economico y el historial publicado.
  - Si intento realizar una accion reservada al administrador, el sistema me bloquea.
  - La experiencia deja claro que mi perfil es de consulta.

## HU-005 - Importacion historica de datos
- Backlog relacionado: PB-005
- Caso de uso relacionado: CU-005
- Historia: Como administrador de la comunidad quiero importar movimientos historicos desde una hoja de calculo para arrancar la plataforma sin recarga manual completa.
- Criterios de aceptacion:
  - Puedo cargar un fichero con la estructura funcional acordada.
  - El sistema valida si cada fila contiene los datos obligatorios.
  - Recibo un resumen con filas importadas y filas rechazadas.
  - Los rechazos indican el motivo funcional.
  - Los movimientos validos quedan disponibles para consulta y resumen.

## HU-006 - Cierre del ejercicio anual
- Backlog relacionado: PB-006
- Caso de uso relacionado: CU-006
- Historia: Como administrador de la comunidad quiero revisar el cierre anual para disponer de una vision consolidada del ejercicio y preparar la comunicacion a vecinos.
- Criterios de aceptacion:
  - Puedo seleccionar un ejercicio anual concreto.
  - Veo ingresos, gastos y saldo total del ejercicio.
  - El sistema deja trazabilidad hacia los movimientos del ejercicio.
  - Se identifican vacios de informacion si existen periodos sin registros.
  - El resultado es apto para soporte de revision comunitaria.

## HU-007 - Recordatorios de hitos relevantes
- Backlog relacionado: PB-007
- Caso de uso relacionado: CU-007
- Historia: Como administrador de la comunidad quiero definir recordatorios de pagos o reuniones para mejorar el seguimiento operativo de la comunidad.
- Criterios de aceptacion:
  - Puedo crear un recordatorio con fecha y mensaje.
  - Puedo consultar los recordatorios configurados.
  - Los recordatorios visibles para vecinos no permiten acciones de gestion.
  - El estado de cada recordatorio es comprensible.
  - Los recordatorios no alteran los datos contables.

## HU-008 - Presupuesto anual de la comunidad
- Backlog relacionado: PB-008
- Caso de uso relacionado: CU-008
- Historia: Como administrador de la comunidad quiero definir un presupuesto anual de ingresos y gastos para planificar el ejercicio y contrastar despues la ejecucion economica real.
- Criterios de aceptacion:
  - Puedo crear un presupuesto para un ejercicio anual concreto.
  - Puedo registrar partidas previstas de ingreso y de gasto.
  - En cada partida veo al menos concepto, tipo e importe previsto.
  - Puedo consultar total previsto de ingresos, total previsto de gastos y saldo presupuestado.
  - El presupuesto queda identificado por ejercicio y disponible para consulta posterior.
  - Si un ejercicio no tiene presupuesto, el sistema me lo comunica con claridad.
