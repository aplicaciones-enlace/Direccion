"""Calculadora de retenciones de Enlace Networks (pagos desde 01/07/2026).

Uso: python3 calcular.py CONCEPTO BASE [--iva 19] [--no-declarante] [--acumulado-mes 0] [--exterior]
Conceptos: compras, servicios, honorarios_pj, honorarios_pn, arriendo_muebles,
           arriendo_inmuebles, transporte_carga, transporte_pasajeros, combustibles
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
}


def pesos(v):
    return "$" + f"{round(v):,}".replace(",", ".")


def calcular(concepto, base, iva_pct=19, no_declarante=False, acumulado_mes=0, exterior=False):
    base_uvt, t_decl, t_no = TABLA[concepto]
    iva = base * iva_pct / 100
    tarifa = t_no if no_declarante else t_decl
    aplica = (base + acumulado_mes) >= base_uvt * UVT
    retefuente = base * tarifa if aplica else 0
    reteiva = iva if exterior else 0  # solo servicios del exterior, 100 %
    total = base + iva
    return {
        "base": base, "iva": iva, "base_minima": base_uvt * UVT, "aplica": aplica,
        "tarifa": tarifa, "retefuente": retefuente, "reteiva": reteiva,
        "total_factura": total, "neto_a_pagar": total - retefuente - reteiva,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("concepto", choices=TABLA)
    p.add_argument("base", type=float)
    p.add_argument("--iva", type=float, default=19)
    p.add_argument("--no-declarante", action="store_true")
    p.add_argument("--acumulado-mes", type=float, default=0)
    p.add_argument("--exterior", action="store_true")
    a = p.parse_args()
    r = calcular(a.concepto, a.base, a.iva, a.no_declarante, a.acumulado_mes, a.exterior)
    print(f"Base: {pesos(r['base'])} | IVA: {pesos(r['iva'])} | Total factura: {pesos(r['total_factura'])}")
    if r["aplica"]:
        print(f"Retención en la fuente {r['tarifa']*100:g} %: {pesos(r['retefuente'])}")
    else:
        print(f"No pasa la base mínima ({pesos(r['base_minima'])}): sin retención en la fuente")
    if r["reteiva"]:
        print(f"Retención de IVA (exterior 100 %): {pesos(r['reteiva'])}")
    print(f"NETO A PAGAR: {pesos(r['neto_a_pagar'])}")
