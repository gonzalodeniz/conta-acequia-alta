# Product Backlog

## Contexto
La vision vigente define una aplicacion web para gestionar la contabilidad de una comunidad de vecinos con foco en transparencia, control economico y soporte al cierre anual. A fecha de 2026-03-21 el repositorio no contiene una aplicacion funcional validada ni un backlog previo poblado, por lo que este documento inicializa la fuente de verdad operativa para `product-manager`.

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
- Estado: listo para issue

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
- Estado: listo para issue

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
- Estado: listo para issue

### PB-004 - Permitir acceso de solo lectura para vecinos
- Descripcion: Habilitar que un vecino consulte la informacion economica publicada sin capacidad de modificar datos.
- Prioridad: Alta
- Valor de negocio: Alto. Es la pieza principal de transparencia para el usuario no administrador.
- Historia de usuario: HU-004
- Caso de uso: CU-004
- Issue GitHub: pendiente de crear tras cerrar regla de visibilidad para vecinos
- Criterios de aceptacion:
  - Un vecino puede acceder a la informacion financiera disponible para consulta.
  - Un vecino no puede crear, editar ni borrar movimientos.
  - El vecino puede consultar al menos resumenes y libro de asientos publicados.
  - El sistema diferencia claramente el alcance de consulta del vecino frente al del administrador.
  - Si un vecino intenta acceder a una accion de gestion, el sistema lo bloquea de forma explicita.
- Dependencias: PB-002, PB-003
- Estado: listo para issue

### PB-005 - Importar movimientos desde una hoja de calculo
- Descripcion: Permitir una carga inicial de movimientos historicos desde un formato tabular acordado para acelerar la adopcion.
- Prioridad: Media
- Valor de negocio: Alto. Reduce barrera de entrada y evita migraciones manuales lentas.
- Historia de usuario: HU-005
- Caso de uso: CU-005
- Issue GitHub: no creada; falta refinamiento funcional
- Criterios de aceptacion:
  - El administrador puede cargar un fichero con movimientos historicos usando un formato previamente definido.
  - El sistema valida los campos minimos requeridos antes de importar.
  - El sistema informa cuantas filas se importan correctamente y cuales fallan.
  - Las filas invalidas quedan identificadas con el motivo funcional del rechazo.
  - Los movimientos importados pasan a ser consultables en el libro de asientos y en el resumen financiero.
- Dependencias: PB-001, PB-002
- Estado: refinamiento pendiente

### PB-006 - Preparar el cierre contable anual
- Descripcion: Facilitar una vista o proceso que permita revisar el ejercicio anual cerrado con sus totales y reportes asociados.
- Prioridad: Media
- Valor de negocio: Alto. Responde a una necesidad clave de gestion formal de la comunidad.
- Historia de usuario: HU-006
- Caso de uso: CU-006
- Issue GitHub: no creada; falta refinamiento funcional
- Criterios de aceptacion:
  - El administrador puede seleccionar un ejercicio anual para revisar su cierre.
  - El sistema muestra el total anual de ingresos, gastos y saldo final del ejercicio.
  - El cierre identifica si existen periodos sin movimientos o posibles vacios de registro.
  - El resultado del cierre puede usarse como base para compartir informacion con vecinos.
  - El ejercicio cerrado conserva trazabilidad con los movimientos que lo componen.
- Dependencias: PB-002, PB-003
- Estado: refinamiento pendiente

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
- Falta definir el formato funcional minimo aceptado para la importacion de movimientos.
- Falta acordar que informacion financiera puede ver un vecino cuando existan datos sensibles o incidencias de conciliacion.
- Falta concretar si el cierre anual requiere solo visualizacion consolidada o tambien bloqueo operativo del ejercicio.

## Riesgos de producto
- Existe una brecha entre la vision del producto y la ausencia de una base funcional implementada en `main`.
- Si se intenta abordar importacion, vecinos y cierre anual sin entregar antes el registro de movimientos y la consulta del libro, aumentara la ambiguedad de validacion.
- La falta de decisiones sobre permisos y datos visibles para vecinos puede generar retrabajo en historias posteriores.

## Preguntas abiertas
- Se considera obligatorio soportar presupuestos en el MVP o se posponen a una fase posterior del roadmap?
- El acceso de vecinos debe permitir ver el detalle de cada asiento o solo resumenes y reportes aprobados?
- La importacion inicial debe admitir una sola plantilla oficial o varias fuentes equivalentes?
