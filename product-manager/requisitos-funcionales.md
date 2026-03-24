# Requisitos funcionales

## Objetivo
Recoger requisitos funcionales transversales y de detalle que complementan la vision, el backlog y los artefactos de trazabilidad del producto.

## RF-001 - Uso del Plan General de Contabilidad de Espana
- Descripcion: La aplicacion debe utilizar el Plan General de Contabilidad de Espana como marco de referencia para la clasificacion contable de los movimientos registrados en la comunidad.
- Justificacion: Aporta consistencia contable, reduce ambiguedad en la seleccion de cuentas y facilita una operativa reconocible para administradores y revisores.
- Trazabilidad:
  - Backlog: PB-009
  - Historia de usuario: HU-009
  - Caso de uso: CU-009

## RF-002 - Ayuda guiada para seleccionar la cuenta contable
- Descripcion: La aplicacion debe ofrecer ayuda funcional al administrador para seleccionar la cuenta correcta del Plan General de Contabilidad al registrar un movimiento.
- Reglas funcionales:
  - La ayuda debe priorizar primero cuentas sencillas de gastos e ingresos.
  - La ayuda debe sugerir cuentas populares en una comunidad de vecinos usando como lista inicial canonica `570`, `572`, `400`, `410`, `623`, `628`, `629`, `705` y `740`.
  - La ayuda debe priorizar `400`, `410`, `623`, `628` y `629` cuando el movimiento sea gasto.
  - La ayuda debe priorizar `705` y `740` cuando el movimiento sea ingreso.
  - Las cuentas `570` y `572` deben presentarse como apoyo operativo de tesoreria y no como sustituto de la cuenta principal del movimiento cuando exista una categoria mas especifica.
  - La ayuda debe reducir la necesidad de navegar por todo el plan contable completo cuando exista una opcion habitual y suficiente para el contexto del movimiento.
  - La ayuda debe mantener disponible la referencia al Plan General de Contabilidad para que el usuario pueda confirmar la clasificacion elegida.
- Trazabilidad:
  - Backlog: PB-009
  - Historia de usuario: HU-009
  - Caso de uso: CU-009

## RF-003 - Exclusiones funcionales del alcance contable inicial
- Descripcion: La contabilidad objetivo de la comunidad no utilizara cuentas de amortizacion en el alcance funcional actual.
- Reglas funcionales:
  - La ayuda de seleccion no debe priorizar ni sugerir cuentas de amortizacion.
  - El alcance del producto inicial se centra en gastos, ingresos y cuentas operativas habituales de tesoreria y terceros para comunidades de vecinos.
- Impacto en producto:
  - Reduce complejidad funcional del alta de movimientos.
  - Mantiene el MVP alineado con una contabilidad comunitaria operativa y no con escenarios societarios mas complejos.
- Trazabilidad:
  - Backlog: PB-009
  - Historia de usuario: HU-009
  - Caso de uso: CU-009

## Supuestos
- La comunidad necesita una contabilidad practica y trazable, no una cobertura completa de todos los casos del Plan General de Contabilidad desde el primer incremento.
- La ayuda de seleccion debe orientarse a minimizar errores de clasificacion para personal administrativo no especializado.

## Riesgos
- Si no se define una lista inicial de cuentas sugeridas por defecto, `developer-teams` podria implementar una ayuda demasiado generica o poco util para el contexto de comunidad de vecinos.
- Si no se mantiene visible la referencia al Plan General de Contabilidad, la ayuda podria percibirse como una clasificacion cerrada y poco auditables.
- Si se priorizan siempre `570` o `572` por encima de cuentas de gasto o ingreso mas especificas, la clasificacion perdera valor para analisis posterior y cierre anual.
