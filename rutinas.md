# Procesos rutinarios de Cindy

Armado con el calendario del 01/09 al 26/10/2026 y lo que Cindy ha contado. Se va ajustando.

## Cómo es su día
- Arranca entre 6:00 y 7:00. De 7:00 a 8:15 organiza la agenda y desde las 8:00 trabaja.
- Pone sus pendientes como **tareas con hora** en el calendario principal (cindypzac@gmail.com), en bloques seguidos de 15 min a 2 horas.
- Lo administrativo pesado (planilla, IVA, Siigo, documentos) le queda casi siempre para la noche, hasta las 11 p. m. o 12 a. m.
- El calendario "PROGRAMACIONES DE PAGOS / REPORTES / RECOGER MERCANCÍA" está **vacío desde abril**: los vencimientos no están agendados en ningún lado.

## Lo que más se repite (en orden de peso)
1. **Nómina / PILA / seguridad social** — novedades, ingresos de personal, errores de planilla, ARL, pago de nómina. Skill: `novedades-de-personal`.
2. **Pagos y contabilidad** — viáticos, Siigo, IVA, facturas de proveedores, cobros. Skill: `area-contable-enlace`.
3. **Personal / RR.HH.** — liquidaciones, casos de empleados, exámenes médicos, capacitación.
4. **SST** — revisión semanal y documentación (bloques largos).
5. **Compras y almacén** — cotizaciones, compras de equipos, confirmar envíos.
6. **Técnico** — asignación y validación de IPs, configuraciones de TV, equipos.
7. **Clientes y contratos** — Puerto Berrío (UT VMAS), La Piedra (qué facturar), Serena del Mar, cobros.
8. **TeleGuatapé** — compras, pagos, dinero.
9. **Trámites** — RUT, Cámara de Comercio, Alcaldía.
10. **Personal / familia** — no va en la contabilidad de Enlace (Bosque Rosa va a Dinero en Pareja).

## Calendario fijo
| Cuándo | Qué | Estado |
|---|---|---|
| Cada lunes 8:00 | Revisar Control SST y Dashboard SST | Ya está en el calendario |
| Día 1 de cada mes 8:30 | Revisión mensual SG-SST | Ya está en el calendario |
| Primeros días hábiles del mes | Pago PILA en Aportes en Línea | **No está agendado** |
| Del 2 al 5 de cada mes | Entrega de facturación (Jerry) | Solo apareció en septiembre |
| Alrededor del 15 y fin de mes | Pago de nómina (Siigo) | **No está agendado** |
| Mensual (según último dígito del NIT: 2) | Declarar y pagar retención en la fuente (formulario 350) | **No está agendado** — plazo general: período sep hasta el 23/10/2026 y oct hasta el 25/11/2026 ([Gerencie](https://www.gerencie.com/calendario-dian)); la fecha exacta para el dígito 2 está en pendientes |
| Bimestral | IVA (formulario 300) | **No está agendado** — plazo general bimestre sep-oct hasta el 25/11/2026 ([Gerencie](https://www.gerencie.com/calendario-dian)) |
| Trimestral | FONTIC en MinTIC (plataforma SER) | **No está agendado** |
| Después de cada viático | Pedir recibos y legalizar | **No hay recordatorio** |
| 4 a 5 días después de cada compra | Confirmar llegada a Guatapé | Se programa con cada compra |

## Qué se puede automatizar
| Proceso | Cómo | Quién lo hace |
|---|---|---|
| Resumen del día | Al decir /asistente, Claude lee el calendario y dice qué hay, qué quedó atrás y qué toca registrar | Claude |
| Vencimientos (PILA, nómina, 350, IVA, FONTIC) | Llenar el calendario administrativo con eventos que se repiten y avisan antes | Claude los crea una vez |
| Legalizar viáticos | Cada viático registrado crea un recordatorio para pedir recibos | Claude |
| Llegada de compras | Recordatorio a los 4-5 días con el mensaje listo | Claude |
| Facturas que llegan al correo | Leer los correos de facturas electrónicas y pasarlas al registro de compras | Gemini (tarea menuda), Claude revisa |
| Alertas del banco (enlaceguatape@gmail.com) | Clasificar entradas y salidas para cuadrar con WispHub y el registro | Gemini / n8n |
| Monitoreo de red y TV | Alertas por zona cuando caen ONUs | n8n en el PC servidor (proyecto Centro de Monitoreo) |
