# Casos de uso

## CU-001 - Registrar un movimiento economico
- Backlog relacionado: PB-001
- Historia relacionada: HU-001
- Actor principal: Administrador de la comunidad
- Objetivo: Registrar un gasto o ingreso con la informacion minima necesaria para su control posterior.
- Disparador: El administrador necesita anotar un nuevo movimiento economico.
- Precondiciones:
  - El administrador dispone de acceso de gestion.
  - El sistema permite crear registros contables.
- Flujo principal:
  1. El administrador inicia el alta de un movimiento.
  2. El sistema solicita fecha, concepto, categoria, tipo e importe.
  3. El administrador completa los datos y confirma el registro.
  4. El sistema valida los campos obligatorios.
  5. El sistema guarda el movimiento y confirma el alta.
- Flujos alternativos:
  - Si falta un dato obligatorio, el sistema rechaza el registro e indica que campo debe completarse.
  - Si el importe no cumple la validacion funcional acordada, el sistema no guarda el movimiento.
- Postcondiciones:
  - El movimiento queda registrado y disponible para consulta.
  - La contabilidad del periodo incorpora el nuevo movimiento.

## CU-009 - Clasificar un movimiento con ayuda guiada
- Backlog relacionado: PB-009
- Historia relacionada: HU-009
- Actor principal: Administrador de la comunidad
- Objetivo: Asociar una cuenta contable adecuada a un movimiento usando una ayuda simplificada del Plan General de Contabilidad de Espana.
- Disparador: El administrador registra o revisa un movimiento y necesita clasificarlo correctamente.
- Precondiciones:
  - Existe un movimiento registrable o ya registrado dentro del alcance funcional.
  - El sistema dispone de una lista inicial de cuentas sugeridas para comunidades de vecinos.
- Flujo principal:
  1. El administrador inicia el registro o revision de un movimiento.
  2. El sistema muestra sugerencias de cuentas segun el tipo de movimiento.
  3. El administrador revisa las opciones y selecciona una cuenta.
  4. El sistema asocia la cuenta elegida al movimiento y la deja visible para consulta posterior.
- Flujos alternativos:
  - Si ninguna sugerencia encaja, el sistema permite elegir otra opcion admitida dentro del alcance funcional.
  - Si el movimiento no tiene todavia tipo definido, el sistema solicita completarlo antes de sugerir cuentas.
- Postcondiciones:
  - El movimiento queda clasificado con una cuenta contable visible y trazable.

## CU-002 - Consultar libro de asientos
- Backlog relacionado: PB-002
- Historia relacionada: HU-002
- Actor principal: Administrador de la comunidad
- Objetivo: Revisar el historial de movimientos registrados.
- Disparador: El administrador necesita consultar o auditar movimientos de un periodo.
- Precondiciones:
  - Existen movimientos registrados o el sistema soporta consulta vacia.
  - El administrador dispone de acceso de consulta.
- Flujo principal:
  1. El administrador accede al libro de asientos.
  2. El sistema muestra los movimientos ordenados cronologicamente.
  3. El administrador aplica un filtro de fechas si lo necesita.
  4. El sistema actualiza el listado con los resultados del filtro.
- Flujos alternativos:
  - Si no existen movimientos en el periodo, el sistema muestra una respuesta vacia clara.
- Postcondiciones:
  - El administrador puede verificar la informacion de los asientos del periodo consultado.

## CU-003 - Consultar resumen financiero
- Backlog relacionado: PB-003
- Historia relacionada: HU-003
- Actor principal: Administrador de la comunidad
- Objetivo: Obtener una vision consolidada del estado economico de un periodo.
- Disparador: El administrador necesita conocer rapidamente ingresos, gastos y saldo.
- Precondiciones:
  - El sistema dispone de movimientos registrados o admite periodos vacios.
- Flujo principal:
  1. El administrador selecciona un periodo de consulta.
  2. El sistema calcula totales de ingresos y gastos.
  3. El sistema muestra saldo resultante del periodo.
- Flujos alternativos:
  - Si el periodo no contiene movimientos, el sistema muestra totales a cero y un mensaje claro.
- Postcondiciones:
  - El administrador obtiene una vision sintetica del periodo consultado.

## CU-004 - Consultar informacion economica como vecino
- Backlog relacionado: PB-004
- Historia relacionada: HU-004
- Actor principal: Vecino
- Objetivo: Acceder a informacion financiera de la comunidad en modo solo lectura.
- Disparador: El vecino quiere revisar la situacion economica de la comunidad.
- Precondiciones:
  - Existe informacion financiera disponible para vecinos.
  - El vecino accede con un alcance funcional de consulta.
- Flujo principal:
  1. El vecino accede a la seccion de consulta economica.
  2. El sistema muestra el resumen economico mensual y anual disponible.
  3. El sistema muestra el listado de movimientos visibles para la comunidad en modo solo lectura.
  4. El vecino revisa la informacion economica sin opciones de gestion.
- Flujos alternativos:
  - Si el vecino intenta realizar una accion de gestion, el sistema la bloquea y lo informa.
  - Si todavia no hay informacion economica disponible, el sistema muestra una respuesta clara sin opciones de edicion.
- Postcondiciones:
  - El vecino ha podido revisar informacion economica sin alterar datos.

## CU-005 - Importar movimientos historicos
- Backlog relacionado: PB-005
- Historia relacionada: HU-005
- Actor principal: Administrador de la comunidad
- Objetivo: Incorporar datos historicos desde una hoja de calculo para acelerar la puesta en marcha.
- Disparador: El administrador dispone de un fichero historico y necesita migrarlo.
- Precondiciones:
  - Existe una plantilla oficial de importacion con columnas obligatorias `fecha`, `tipo`, `concepto`, `categoria` e `importe`, y `referencia_externa` opcional.
  - El administrador dispone de acceso de gestion.
- Flujo principal:
  1. El administrador inicia el proceso de importacion.
  2. El sistema solicita el fichero a cargar.
  3. El sistema valida el contenido fila a fila.
  4. El sistema importa los movimientos validos.
  5. El sistema presenta un resumen del resultado.
- Flujos alternativos:
  - Si el fichero no cumple la plantilla esperada, el sistema rechaza la importacion y explica el problema.
  - Si hay filas invalidas, el sistema solo incorpora las validas y reporta las rechazadas.
- Postcondiciones:
  - Los movimientos validos importados quedan disponibles en el libro y en los resumenes.

## CU-006 - Revisar cierre anual
- Backlog relacionado: PB-006
- Historia relacionada: HU-006
- Actor principal: Administrador de la comunidad
- Objetivo: Revisar el resultado consolidado del ejercicio anual.
- Disparador: El administrador necesita preparar el cierre del ejercicio.
- Precondiciones:
  - Existen movimientos del ejercicio a revisar o el sistema admite ejercicios sin actividad.
- Flujo principal:
  1. El administrador selecciona el ejercicio anual.
  2. El sistema consolida los movimientos del ejercicio.
  3. El sistema muestra ingresos, gastos y saldo final.
  4. El sistema identifica los meses del ejercicio sin movimientos o con posibles vacios de registro.
  5. El administrador revisa los datos para su comunicacion posterior.
- Flujos alternativos:
  - Si hay periodos sin registros, el sistema los identifica como advertencia funcional sin bloquear una correccion posterior.
- Postcondiciones:
  - El ejercicio anual queda revisado con trazabilidad hacia sus movimientos.

## CU-007 - Gestionar recordatorios
- Backlog relacionado: PB-007
- Historia relacionada: HU-007
- Actor principal: Administrador de la comunidad
- Objetivo: Crear y consultar recordatorios de hitos relevantes para la comunidad.
- Disparador: El administrador necesita programar un aviso de pago, reunion o revision.
- Precondiciones:
  - El sistema soporta recordatorios configurables.
  - El administrador dispone de acceso de gestion.
- Flujo principal:
  1. El administrador crea un recordatorio con fecha, tipo de hito y mensaje.
  2. El sistema registra el recordatorio.
  3. El sistema clasifica el recordatorio segun su estado temporal.
  4. El administrador consulta el listado de recordatorios.
- Flujos alternativos:
  - Si faltan datos obligatorios, el sistema rechaza el recordatorio.
  - Si el recordatorio ya esta vencido segun la fecha configurada, el sistema lo muestra como vencido sin modificar informacion contable.
- Postcondiciones:
  - El recordatorio queda disponible para su seguimiento por el administrador segun el alcance definido por negocio.

## CU-008 - Definir presupuesto anual
- Backlog relacionado: PB-008
- Historia relacionada: HU-008
- Actor principal: Administrador de la comunidad
- Objetivo: Definir el presupuesto anual de la comunidad para planificar ingresos y gastos del ejercicio.
- Disparador: El administrador necesita preparar o revisar el presupuesto del nuevo ejercicio.
- Precondiciones:
  - El administrador dispone de acceso de gestion.
  - El sistema soporta la definicion de presupuestos por ejercicio.
- Flujo principal:
  1. El administrador inicia la creacion del presupuesto de un ejercicio anual.
  2. El sistema solicita el ejercicio y las partidas previstas.
  3. El administrador registra partidas diferenciando ingresos y gastos con concepto e importe previsto.
  4. El sistema consolida los importes del presupuesto.
  5. El sistema guarda el presupuesto y lo deja disponible para consulta posterior.
- Flujos alternativos:
  - Si falta el ejercicio o una partida obligatoria, el sistema rechaza el guardado e indica el dato pendiente.
  - Si el ejercicio ya tiene presupuesto, el sistema permite revisar o actualizar la version vigente del mismo presupuesto dentro del alcance inicial.
  - Si el ejercicio consultado no tiene presupuesto registrado, el sistema lo informa claramente.
- Postcondiciones:
  - El presupuesto anual queda identificado por ejercicio y preparado para su consulta.
