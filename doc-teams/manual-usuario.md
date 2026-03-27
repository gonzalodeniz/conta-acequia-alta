# Manual de usuario

## Publico objetivo
Vecinos y administradores de fincas que necesitan entender el uso real de la entrega minima disponible.

## Alcance
Este documento describe el comportamiento funcional que ya se puede verificar en la aplicacion web minima del repositorio.
Tambien deja explicitas las capacidades que siguen solo en vision o backlog para evitar confundirlas con funcionamiento vigente.

## Estado de verificacion
- Existe una aplicacion WSGI minima en Python en `app.py`.
- La pantalla actual combina un libro de asientos editable y un listado de movimientos ya registrados.
- La entrega actual permite registrar y actualizar movimientos contables de gasto o ingreso directamente en la tabla.
- Cada movimiento queda persistido en `data/movimientos.json`.
- La lista se muestra ordenada cronologicamente por fecha y, si coincide la fecha, por identificador.
- El libro de asientos puede filtrarse por rango de fechas desde la misma pantalla.
- Cada fila visible incluye un numero de asiento correlativo dentro de su ejercicio anual.
- La aplicacion devuelve mensajes claros de validacion cuando falta un campo, la fecha no es valida, el tipo no es `gasto` o `ingreso`, o el importe no es mayor que cero.
- Si el fichero de datos falta, esta corrupto o no puede guardarse, la aplicacion responde con un error de disponibilidad `503` y conserva el formulario visible para reintento.
- No hay autenticacion ni perfiles de acceso diferenciados en la entrega actual.
- Las capacidades de presupuestos, importacion, cierre anual, vecinos en solo lectura y notificaciones no estan implementadas en esta base.

## Que puede hacer el usuario hoy
- Dar de alta un movimiento con fecha, concepto, categoria, tipo e importe.
- Actualizar un movimiento existente directamente desde la tabla.
- Registrar un gasto o un ingreso.
- Ver una lista de los movimientos registrados hasta ese momento.
- Filtrar el libro por fecha inicial y fecha final.
- Recibir validaciones de formulario cuando un campo es obligatorio, la fecha no tiene formato `AAAA-MM-DD`, el tipo no es valido o el importe no es mayor que cero.
- Ver el identificador unico generado para cada movimiento correcto.
- Ver el numero de asiento anual asociado a cada movimiento mostrado en pantalla.

## Campos del formulario
- `Fecha`: obligatoria y con formato `AAAA-MM-DD`.
- `Tipo`: solo admite `gasto` o `ingreso`.
- `Concepto`: texto libre obligatorio para describir el movimiento.
- `Categoria`: texto libre obligatorio para clasificar el movimiento desde un punto de vista operativo.
- `Importe`: valor numerico mayor que cero.

## Uso esperado por perfil
### Administrador de la comunidad
1. Abre la aplicacion local.
2. Rellena una fila nueva de la tabla con los datos del movimiento.
3. Guarda un gasto o ingreso desde la accion de alta de la propia tabla.
4. Si necesita corregir un apunte, edita la fila existente y confirma la actualizacion.
5. Revisa la lista de ultimos movimientos para confirmar la operacion.
6. Si necesita acotar una revision, usa los filtros `Desde` y `Hasta` del libro de asientos.

### Vecino
1. En la vision de producto, el vecino deberia tener acceso de solo lectura.
2. En la entrega actual no existe todavia un acceso de vecino separado, asi que ese comportamiento sigue pendiente de desarrollo.
3. No debe asumirse que el vecino pueda filtrar, editar o consultar resumenes, porque esas capacidades no estan implementadas.

## Flujo de uso
1. Inicia la aplicacion con `make run` o `python3 app.py`.
2. Abre `http://127.0.0.1:8000`.
3. Completa una fila nueva de la tabla o edita una existente.
4. Guarda el movimiento o la actualizacion.
5. Verifica que el mensaje de exito muestra el identificador generado.
6. Revisa la lista inferior para confirmar que el movimiento quedo visible con su numero de asiento.
7. Si el libro necesita una revision acotada, prueba el filtro por rango de fechas.

## Lo que no debe asumirse todavia
- No se documentan pantallas adicionales porque la entrega actual solo expone una vista unica.
- No se documenta busqueda ni resumen financiero porque aun no estan disponibles en la base ejecutable.
- No se documenta gestion de presupuestos como funcionalidad operativa porque sigue pendiente en el backlog.
- No se debe asumir que la vista actual sustituye una aplicacion de produccion completa.
- No existe, por ahora, una configuracion de usuarios, permisos o auditoria por perfil.
- No existe garantia de disponibilidad si falla el fichero `data/movimientos.json`; en ese caso el usuario debe reintentar tras corregir el almacenamiento o restaurar una copia valida.

## Errores habituales
- Si falta un campo obligatorio, el formulario muestra el mensaje `Este campo es obligatorio.` debajo del campo afectado.
- Si la fecha no sigue el formato esperado, la aplicacion informa que debe usar `AAAA-MM-DD`.
- Si el tipo no es `gasto` o `ingreso`, la aplicacion rechaza el envio.
- Si el importe no es valido o no es mayor que cero, la aplicacion no crea el movimiento.
- Si el libro no se puede leer o guardar, la aplicacion muestra un error de disponibilidad `503` y no confirma el alta.

## Dependencias abiertas
- Falta cerrar la implementacion de PB-003 para ampliar el uso funcional del resumen financiero.
- Falta concretar la politica de visibilidad para vecinos antes de documentar el acceso de solo lectura como comportamiento real.
- Falta definir el alcance tecnico de importacion, cierre anual y notificaciones antes de que este manual pueda ampliarse.
- La clasificacion contable asistida de `PB-009` sigue siendo una dependencia funcional abierta y no debe asumirse como disponible en esta interfaz.

## Limitaciones
- Esta guia describe una entrega minima local, no un producto completo listo para usuarios finales.
- Los cambios funcionales futuros deben reflejarse aqui solo cuando esten integrados en `main` y puedan verificarse en el arbol de trabajo.
