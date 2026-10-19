# Flujo de cada compra o pago

Cada vez que Cindy diga "hice un pago" o "voy a comprar", Claude piensa como un área contable: **¿qué haría una empresa con esto?** y le dice a Cindy qué sigue.

## Paso 1 — Validar (antes o al momento de pagar)
1. **¿Quién es el proveedor?** Buscarlo en `registros/proveedores.csv`. Si no está, pedir su RUT y anotar: tipo (empresa / persona natural), NIT o cédula, responsable de IVA, régimen (ordinario / SIMPLE), autorretenedor, declarante (solo personas naturales), municipio.
2. **¿Qué se compra?** Escoger el concepto de la tabla (`normas/retenciones-2026.md`).
3. **¿Pasa la base?** Sumar lo pagado a ese proveedor en el mismo mes.
4. **Calcular** con `calcular.py`: IVA, retención en la fuente, retención de IVA (solo exterior) y **neto a pagar**.
5. **Soporte que se necesita:**
   - Empresa o persona responsable de IVA → **factura electrónica** a nombre de Enlace Networks SAS, NIT 901.454.922-2.
   - Persona natural no responsable de IVA → **cuenta de cobro** + **documento soporte electrónico** que hace Enlace.
   - Servicio personal → planilla de seguridad social del mes.
6. **Alertas:** gasto sin soporte válido, proveedor sin RUT, efectivo de más de 100 UVT ($5.237.400) a una sola persona, compra a persona natural que quita IVA descontable.

## Paso 2 — Registro contable
- **El registro oficial va en WispHub** (el área contable de Cindy). El archivo `registros/compras-2026.csv` es solo la copia de trabajo de Claude.
- Registrar en `registros/compras-2026.csv` con estado **PAGADO – EN CAMINO** (o **PAGADO** si es un servicio o algo que no llega físico).
- Decir a qué va: **almacén/inventario** (equipos, ONUs, fibra, materiales), **gasto** (servicios, arriendos, papelería que se consume ya) o **activo fijo** (herramientas y equipos que duran más de un año).

## Paso 3 — Recordatorio de llegada
- Si es algo físico que llega a Guatapé: programar recordatorio en **4 a 5 días** en este mismo chat.
- Ese día, Claude le recuerda a Cindy y le deja listo el mensaje para el equipo:
  > "Buenas tardes, ¿me confirman por favor si ya recibieron [qué], de [proveedor]? Gracias."
- Cuando confirmen: estado **RECIBIDO**. Si no ha llegado: nuevo recordatorio en 2 días.

## Paso 4 — Entrada al almacén (WispHub)
- Cuando llega, se registra en el **inventario de WispHub** (Cindy pasa el link de dónde se registra).
- Estado en el registro: **EN ALMACÉN**.

## Paso 5 — Salidas del almacén
- Cada cosa que se use (instalación, reparación, consumo) se descuenta del inventario.
- Pendiente de definir con Cindy dónde se lleva el control de salidas (ver `pendientes.md`).

## Estados posibles en el registro
PAGADO – EN CAMINO → RECIBIDO → EN ALMACÉN → (CONSUMIDO / ASIGNADO)
PAGADO (servicios y gastos que no llegan físicos)
