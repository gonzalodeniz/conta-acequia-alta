# Requisitos funcionales

## Objetivo
Recoger requisitos funcionales transversales y de detalle que complementan la vision, el backlog y los artefactos de trazabilidad del producto.

## RF-001 - Uso del Plan General de Contabilidad de Espana
- Descripcion: La aplicacion debe utilizar el Plan General de Contabilidad de Espana como marco de referencia para la clasificacion contable de los movimientos registrados en la comunidad.
- Justificacion: Aporta consistencia contable, reduce ambiguedad en la seleccion de cuentas y facilita una operativa reconocible para administradores y revisores.
- Trazabilidad:
  - Backlog: PB-001
  - Historia de usuario: HU-001
  - Caso de uso: CU-001

## RF-002 - Ayuda guiada para seleccionar la cuenta contable
- Descripcion: La aplicacion debe ofrecer ayuda funcional al administrador para seleccionar la cuenta correcta del Plan General de Contabilidad al registrar un movimiento.
- Reglas funcionales:
  - La ayuda debe priorizar primero cuentas sencillas de gastos e ingresos.
  - La ayuda debe sugerir cuentas populares en una comunidad de vecinos, incluyendo al menos banco, caja, proveedores y acreedores.
  - La ayuda debe reducir la necesidad de navegar por todo el plan contable completo cuando exista una opcion habitual y suficiente para el contexto del movimiento.
  - La ayuda debe mantener disponible la referencia al Plan General de Contabilidad para que el usuario pueda confirmar la clasificacion elegida.
- Trazabilidad:
  - Backlog: PB-001
  - Historia de usuario: HU-001
  - Caso de uso: CU-001

## RF-003 - Exclusiones funcionales del alcance contable inicial
- Descripcion: La contabilidad objetivo de la comunidad no utilizara cuentas de amortizacion en el alcance funcional actual.
- Reglas funcionales:
  - La ayuda de seleccion no debe priorizar ni sugerir cuentas de amortizacion.
  - El alcance del producto inicial se centra en gastos, ingresos y cuentas operativas habituales de tesoreria y terceros para comunidades de vecinos.
- Impacto en producto:
  - Reduce complejidad funcional del alta de movimientos.
  - Mantiene el MVP alineado con una contabilidad comunitaria operativa y no con escenarios societarios mas complejos.
- Trazabilidad:
  - Backlog: PB-001
  - Historia de usuario: HU-001
  - Caso de uso: CU-001

## Supuestos
- La comunidad necesita una contabilidad practica y trazable, no una cobertura completa de todos los casos del Plan General de Contabilidad desde el primer incremento.
- La ayuda de seleccion debe orientarse a minimizar errores de clasificacion para personal administrativo no especializado.

## Riesgos
- Si no se define una lista inicial de cuentas sugeridas por defecto, `developer-teams` podria implementar una ayuda demasiado generica o poco util para el contexto de comunidad de vecinos.
- Si no se mantiene visible la referencia al Plan General de Contabilidad, la ayuda podria percibirse como una clasificacion cerrada y poco auditables.
