# Historias de usuario

## Criterios de redaccion
- Todas las historias se alinean con `vision-product.md`.
- Los criterios de aceptacion se redactan para validacion funcional por `qa-teams`.
- La trazabilidad se mantiene mediante los identificadores `HU-*`, `PB-*` y `CU-*`.

## HU-001 - Registro de movimientos contables
- Backlog relacionado: PB-001
- Caso de uso relacionado: CU-001
- Historia: Como administrador de la comunidad quiero registrar gastos e ingresos con los datos minimos obligatorios para mantener la contabilidad actualizada y trazable.
- Criterios de aceptacion:
  - Puedo registrar un movimiento indicando fecha, concepto, categoria, tipo e importe.
  - El sistema distingue si el movimiento es gasto o ingreso.
  - No puedo guardar un movimiento si falta algun dato obligatorio.
  - Al registrar un movimiento, este queda disponible para consulta posterior.
  - El sistema muestra un resultado claro de alta correcta o rechazo.

## HU-009 - Clasificacion contable asistida
- Backlog relacionado: PB-009
- Caso de uso relacionado: CU-009
- Historia: Como administrador de la comunidad quiero recibir ayuda para clasificar cada movimiento con una cuenta habitual del Plan General de Contabilidad de Espana para reducir errores de imputacion y mantener una contabilidad mas fiable.
- Criterios de aceptacion:
  - El sistema me ofrece sugerencias de cuentas contables al registrar un gasto o un ingreso.
  - Las sugerencias priorizan cuentas habituales de una comunidad de vecinos.
  - Puedo confirmar una cuenta sugerida o escoger otra opcion permitida.
  - La ayuda no prioriza cuentas de amortizacion en este alcance.
  - La cuenta seleccionada queda visible en la informacion del movimiento.

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

## HU-010 - Gestion editable del libro de asientos
- Backlog relacionado: PB-010
- Caso de uso relacionado: CU-010
- Historia: Como administrador de la comunidad quiero trabajar directamente sobre el libro de asientos en una vista tipo hoja de calculo para registrar y corregir movimientos con menos friccion operativa.
- Criterios de aceptacion:
  - Veo un menu lateral izquierdo con iconos que me permite navegar por las secciones principales de la interfaz.
  - El libro de asientos se presenta como una tabla con estetica de hoja de calculo y columnas claramente identificadas.
  - Puedo anadir un nuevo asiento directamente en la tabla sin depender de un formulario separado.
  - Puedo modificar un asiento existente directamente en la tabla.
  - Cada asiento muestra un numero de asiento visible y correlativo dentro de su ejercicio anual.
  - La numeracion de asientos se reinicia en `1` al comenzar cada nuevo ano contable.
  - El formulario independiente de registro de movimientos deja de ser necesario en la operativa principal del administrador.

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
  - Puedo consultar un resumen economico mensual y anual en modo solo lectura.
  - Puedo consultar el listado de movimientos visibles para la comunidad con fecha, concepto, categoria, tipo e importe.
  - No dispongo de acciones para modificar movimientos o configuraciones.
  - Si intento realizar una accion reservada al administrador, el sistema me bloquea.
  - La experiencia deja claro que mi perfil es de consulta.

## HU-005 - Importacion historica de datos
- Backlog relacionado: PB-005
- Caso de uso relacionado: CU-005
- Historia: Como administrador de la comunidad quiero importar movimientos historicos desde una hoja de calculo para arrancar la plataforma sin recarga manual completa.
- Criterios de aceptacion:
  - Puedo cargar la plantilla oficial de importacion con las columnas `fecha`, `tipo`, `concepto`, `categoria` e `importe`, y `referencia_externa` opcional.
  - El sistema valida si cada fila contiene los datos obligatorios y si el tipo es compatible con gasto o ingreso.
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
  - Veo que meses del ejercicio no tienen movimientos o presentan vacios de registro.
  - El sistema deja trazabilidad hacia los movimientos del ejercicio.
  - El resultado es apto para soporte de revision comunitaria sin bloquear correcciones posteriores del ejercicio en esta primera version.

## HU-007 - Recordatorios de hitos relevantes
- Backlog relacionado: PB-007
- Caso de uso relacionado: CU-007
- Historia: Como administrador de la comunidad quiero definir recordatorios internos de pagos, reuniones o revisiones para mejorar el seguimiento operativo de la comunidad sin depender de avisos externos.
- Criterios de aceptacion:
  - Puedo crear un recordatorio con fecha, tipo de hito y mensaje.
  - Puedo consultar los recordatorios configurados con su estado.
  - En el alcance inicial, los recordatorios solo estan disponibles para el administrador.
  - Distingo de forma clara si un recordatorio esta pendiente o vencido.
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
  - En el alcance inicial solo existe una version vigente del presupuesto por ejercicio.
  - El presupuesto queda identificado por ejercicio y disponible para consulta posterior.
  - Si un ejercicio no tiene presupuesto, el sistema me lo comunica con claridad.
