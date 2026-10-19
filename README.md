# Dirección — Área contable de Enlace Networks SAS

Cindy es la gerente: pide. Claude es el área contable: valida, calcula y registra.

## Cómo funciona
1. Cindy dice qué va a comprar o pagar (a quién, por qué, cuánto).
2. Claude revisa el proveedor (persona natural o empresa, declarante o no, responsable de IVA o no) y el concepto.
3. Claude calcula las retenciones, dice cuánto se le paga neto al proveedor y qué soporte se necesita.
4. Claude lo deja registrado aquí, en `registros/compras-2026.csv`.
5. Lo que Claude no sepa, lo anota en `pendientes.md` y se lo pregunta a Cindy. Con cada respuesta, esta base se va alimentando.

## Carpetas
| Archivo | Qué tiene |
|---|---|
| `empresa.md` | Datos de Enlace según el RUT: NIT, responsabilidades, actividades |
| `normas/retenciones-2026.md` | UVT, bases y tarifas de retención vigentes |
| `normas/como-validar-una-compra.md` | Paso a paso que sigue Claude en cada compra |
| `registros/compras-2026.csv` | Todas las compras y pagos registrados |
| `registros/proveedores.csv` | Datos tributarios de cada proveedor (se llena una vez) |
| `pendientes.md` | Preguntas abiertas y cosas por confirmar |
| `aplicativos.md` | Aplicativos que usa Cindy y para qué |
| `bitacora/` | Qué se hizo cada día |
| `rutinas.md` | Procesos rutinarios, calendario fijo y qué se puede automatizar |
| `proyectos.md` | Proyectos activos y quietos con lo que les falta |
| `calcular.py` | Calculadora de retenciones que usa Claude |
| `CLAUDE.md` | Instrucciones para Claude: cómo trabajar con esta base |
