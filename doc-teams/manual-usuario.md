# Manual de usuario

## Publico objetivo
Vecinos y administradores de fincas que necesitan entender el uso real de la entrega minima disponible.

## Alcance
Este documento describe el comportamiento funcional que ya se puede verificar en la aplicacion web minima del repositorio.
Tambien deja explicitas las capacidades que siguen solo en vision o backlog para evitar confundirlas con funcionamiento vigente.

## Estado de verificacion
- Existe una aplicacion WSGI minima en Python en `app.py`.
- La entrega actual permite registrar movimientos contables de gasto o ingreso.
- Cada movimiento queda persistido en `data/movimientos.json`.
- No hay autenticacion ni perfiles de acceso diferenciados en la entrega actual.
- Las capacidades de presupuestos, importacion, cierre anual, vecinos en solo lectura y notificaciones no estan implementadas en esta base.

## Que puede hacer el usuario hoy
- Dar de alta un movimiento con fecha, concepto, categoria, tipo e importe.
- Registrar un gasto o un ingreso.
- Ver una lista de los movimientos registrados hasta ese momento.
- Recibir validaciones de formulario cuando un campo es obligatorio, la fecha no tiene formato `AAAA-MM-DD`, el tipo no es valido o el importe no es mayor que cero.
- Ver el identificador unico generado para cada movimiento correcto.

## Uso esperado por perfil
### Administrador de la comunidad
1. Abre la aplicacion local.
2. Rellena el formulario con los datos del movimiento.
3. Guarda un gasto o ingreso.
4. Revisa la lista de ultimos movimientos para confirmar el alta.

### Vecino
1. En la vision de producto, el vecino deberia tener acceso de solo lectura.
2. En la entrega actual no existe todavia un acceso de vecino separado, asi que ese comportamiento sigue pendiente de desarrollo.

## Flujo de uso
1. Inicia la aplicacion con `make run` o `python3 app.py`.
2. Abre `http://127.0.0.1:8000`.
3. Completa el formulario de registro.
4. Guarda el movimiento.
5. Verifica que el mensaje de exito muestra el identificador generado.
6. Revisa la lista inferior para confirmar que el movimiento quedo visible.

## Lo que no debe asumirse todavia
- No se documentan pantallas adicionales porque la entrega actual solo expone una vista unica.
- No se documenta busqueda, filtrado ni resumen financiero porque aun no estan disponibles en la base ejecutable.
- No se documenta gestion de presupuestos como funcionalidad operativa porque sigue pendiente en el backlog.
- No se debe asumir que la vista actual sustituye una aplicacion de produccion completa.

## Dependencias abiertas
- Falta cerrar la implementacion de PB-002 y PB-003 para ampliar el uso funcional de la consulta y el resumen.
- Falta concretar la politica de visibilidad para vecinos antes de documentar el acceso de solo lectura como comportamiento real.
- Falta definir el alcance tecnico de importacion, cierre anual y notificaciones antes de que este manual pueda ampliarse.

## Limitaciones
- Esta guia describe una entrega minima local, no un producto completo listo para usuarios finales.
- Los cambios funcionales futuros deben reflejarse aqui solo cuando esten integrados en `main` y puedan verificarse en el arbol de trabajo.
