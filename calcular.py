"""Calculadora de retenciones de Enlace Networks (pagos desde 01/07/2026).

Uso: python3 calcular.py CONCEPTO BASE [opciones]
Conceptos: compras, servicios, honorarios_pj, honorarios_pn, arriendo_muebles,
           arriendo_inmuebles, transporte_carga, transporte_pasajeros, combustibles,
           aseo_vigilancia, temporales
Opciones:
  --iva 19              tarifa de IVA (0 si el proveedor no es responsable de IVA)
  --no-declarante       persona natural no declarante (tarifa más alta)
  --acumulado-mes N     lo ya pagado a ese proveedor en el mes SIN retención
                        (si sumado pasa la base, se retiene sobre todo lo acumulado)
  --aiu N               valor del AIU (aseo/vigilancia y temporales retienen sobre el AIU)
  --supera-3300         honorarios de persona natural que pasan 3.300 UVT en el año → 11 %
  --exterior            servicio de una empresa del exterior: NO usa la tabla nacional
"""
import argparse

UVT = 52374
# concepto: (base mínima en UVT, tarifa declarante, tarifa no declarante)
TABLA = {
    "compras": (10, 0.025, 0.035),
    "servicios": (2, 0.04, 0.06),
    "honorarios_pj": (0, 0.11, 0.11),
    "honorarios_pn": (0, 0.10, 0.10),
    "arriendo_muebles": (0, 0.04, 0.04),
    "arriendo_inmuebles": (10, 0.035, 0.035),
    "transporte_carga": (2, 0.01, 0.01),
    "transporte_pasajeros": (10, 0.035, 0.035),
    "combustibles": (0, 0.001, 0.001),
    "aseo_vigilancia": (2, 0.02, 0.02),  # sobre el AIU
    "temporales": (2, 0.01, 0.01),       # sobre el AIU
}
SOBRE_AIU = {"aseo_vigilancia", "temporales"}


def pesos(v):
    return "$" + f"{round(v):,}".replace(",", ".")


def calcular(concepto, base, iva_pct=19, no_declarante=False, acumulado_mes=0,
             exterior=False, aiu=None, supera_3300=False):
    base_uvt, t_decl, t_no = TABLA[concepto]
    iva = base * iva_pct / 100
    total = base + iva
    r = {"base": base, "iva": iva, "total_factura": total, "base_minima": base_uvt * UVT,
         "aplica": False, "tarifa": 0, "retefuente": 0, "reteiva": 0, "avisos": []}

    if exterior:
        # Pagos al exterior tienen tarifas propias (no la tabla nacional): se revisan caso por caso.
        r["reteiva"] = iva
        r["avisos"].append("Pago al exterior: la retención en la fuente NO es la de la tabla nacional "
                           "(depende del concepto y de si hay convenio). Revisar con María Isabel antes de pagar.")
    else:
        tarifa = t_no if no_declarante else t_decl
        if concepto == "honorarios_pn" and supera_3300:
            tarifa = 0.11
        aplica = (base + acumulado_mes) >= base_uvt * UVT
        if concepto in SOBRE_AIU:
            if aiu is None:
                r["avisos"].append("Falta el valor del AIU: este concepto retiene sobre el AIU, no sobre el total.")
                aiu = 0
            sujeto = aiu
        else:
            # si con lo acumulado del mes se pasa la base, se retiene sobre todo lo no retenido
            sujeto = base + acumulado_mes if (aplica and acumulado_mes) else base
        r.update(aplica=aplica, tarifa=tarifa, retefuente=sujeto * tarifa if aplica else 0)
        if acumulado_mes and aplica:
            r["avisos"].append(f"Incluye la retención de lo acumulado en el mes ({pesos(acumulado_mes)}) "
                               "que no se había retenido.")

    r["neto_a_pagar"] = total - r["retefuente"] - r["reteiva"]
    return r


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("concepto", choices=TABLA)
    p.add_argument("base", type=float)
    p.add_argument("--iva", type=float, default=19)
    p.add_argument("--no-declarante", action="store_true")
    p.add_argument("--acumulado-mes", type=float, default=0)
    p.add_argument("--exterior", action="store_true")
    p.add_argument("--aiu", type=float)
    p.add_argument("--supera-3300", action="store_true")
    a = p.parse_args()
    r = calcular(a.concepto, a.base, a.iva, a.no_declarante, a.acumulado_mes,
                 a.exterior, a.aiu, a.supera_3300)
    print(f"Base: {pesos(r['base'])} | IVA: {pesos(r['iva'])} | Total factura: {pesos(r['total_factura'])}")
    if not a.exterior:
        if r["aplica"]:
            print(f"Retención en la fuente {r['tarifa']*100:g} %: {pesos(r['retefuente'])}")
        else:
            print(f"No pasa la base mínima ({pesos(r['base_minima'])}): sin retención en la fuente")
    if r["reteiva"]:
        print(f"Retención de IVA (exterior 100 %): {pesos(r['reteiva'])}")
    for aviso in r["avisos"]:
        print(f"⚠️ {aviso}")
    print(f"NETO A PAGAR: {pesos(r['neto_a_pagar'])}")
