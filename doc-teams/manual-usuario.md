# Manual de usuario

## Publico objetivo
Vecinos y administradores de fincas que necesitan entender el uso previsto de `conta-acequia-alta`.

## Alcance
Este documento describe el comportamiento funcional esperado a partir de la documentacion de `product-manager/`.
No sustituye a una guia de uso de una interfaz ya verificada, porque en el arbol de trabajo actual no se ha podido confirmar una aplicacion operativa completa.

## Estado de verificacion
- La vision y el backlog de producto estan definidos.
- En esta revision no se ha podido confirmar una interfaz de usuario desplegable en el arbol visible del repositorio.
- Por tanto, este manual describe uso esperado y restricciones de acceso, no pantallas ni rutas concretas.

## Que ofrece el producto
La solucion esta orientada a:
- Registrar gastos e ingresos de la comunidad.
- Consultar el libro de asientos contables.
- Revisar resumenes financieros por periodo.
- Permitir acceso de solo lectura a vecinos.
- Importar movimientos historicos cuando el formato quede definido.
- Preparar el cierre anual y el seguimiento de hitos relevantes.

## Uso esperado por perfil
### Administrador de la comunidad
1. Registra gastos e ingresos con los datos minimos definidos por negocio.
2. Consulta el libro de asientos para revisar el historial economico.
3. Obtiene resumenes financieros por periodo.
4. Importa datos historicos si dispone de una plantilla compatible.
5. Revisa el cierre anual y los recordatorios operativos cuando existan.

### Vecino
1. Consulta la informacion economica publicada por la comunidad.
2. Revisa resumenes o historiales visibles en modo solo lectura.
3. No crea, edita ni elimina movimientos.
4. Si intenta una accion reservada al administrador, el sistema debe bloquearla con un mensaje claro.

## Lo que no debe asumirse todavia
- No se documentan nombres de pantallas, botones ni recorridos de navegacion.
- No se documenta gestion de presupuestos como funcionalidad operativa porque no esta trazada de forma explicita en el backlog vigente.
- No se debe asumir que todos los datos contables son visibles para vecinos; el alcance exacto sigue siendo una dependencia abierta.

## Dependencias abiertas
- Falta cerrar el formato funcional minimo de importacion.
- Falta concretar el alcance exacto de la informacion visible para vecinos.
- Falta definir si el cierre anual es solo una vista consolidada o si ademas bloquea el ejercicio.

## Limitaciones
- Este manual es una guia de uso esperado, no una guia de usuario de produccion.
- Cualquier cambio validado por desarrollo y QA debe reflejarse aqui solo despues de quedar integrado en `main`.
