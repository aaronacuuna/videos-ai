#!/usr/bin/env python3
"""Resumen del canal: estado de la configuración y métricas de videos/registro.csv.

Uso: python3 scripts/resumen.py
Solo usa la biblioteca estándar.
"""
import csv
import re
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRO = ROOT / "videos" / "registro.csv"
CANAL = ROOT / "canal"


def num(value):
    try:
        return float(str(value).replace(",", ".").replace("%", "").strip())
    except (TypeError, ValueError):
        return None


def estado_canal():
    print("== Configuración del canal ==")
    for path in sorted(CANAL.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^estado:\s*(\w+)", text, re.MULTILINE)
        estado = match.group(1) if match else "?"
        pendientes = text.count("PENDIENTE")
        extra = f" ({pendientes} hueco{'s' if pendientes > 1 else ''} por rellenar)" if pendientes else ""
        print(f"  {estado:<10} {path.relative_to(ROOT)}{extra}")
    print()


def metricas():
    print("== Vídeos ==")
    with REGISTRO.open(encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
    if not filas:
        print("  Aún no hay vídeos en videos/registro.csv\n")
        return

    publicados = [r for r in filas if r.get("fecha_publicacion")]
    print(f"  Total: {len(filas)} · publicados: {len(publicados)}")

    metrica = "vistas_28d"
    por_formato = defaultdict(list)
    for r in publicados:
        por_formato[r.get("formato") or "?"].append(r)

    for formato, rs in sorted(por_formato.items()):
        print(f"\n  [{formato}] {len(rs)} vídeos")
        for campo in ("vistas_7d", "vistas_28d", "ctr_pct", "retencion_media_pct", "subs_ganados"):
            valores = [v for v in (num(r.get(campo)) for r in rs) if v is not None]
            if valores:
                print(f"    mediana {campo:<22} {statistics.median(valores):>10.1f}  (n={len(valores)})")

        con_dato = [r for r in rs if num(r.get(metrica)) is not None]
        if len(con_dato) >= 2:
            con_dato.sort(key=lambda r: num(r[metrica]), reverse=True)
            mejor, peor = con_dato[0], con_dato[-1]
            print(f"    mejor ({metrica}): {mejor['id']} · {num(mejor[metrica]):.0f} · {mejor.get('titulo', '')}")
            print(f"    peor  ({metrica}): {peor['id']} · {num(peor[metrica]):.0f} · {peor.get('titulo', '')}")

    sin_metricas = [r["id"] for r in publicados if not r.get("vistas_7d")]
    if sin_metricas:
        print(f"\n  Publicados sin métricas: {', '.join(sin_metricas)}")

    horas = sum(v for v in (num(r.get("horas_vistas_28d")) for r in publicados) if v is not None)
    if horas:
        print(f"\n  Horas vistas (suma de 28d registradas): {horas:.0f}")
    print()


if __name__ == "__main__":
    estado_canal()
    metricas()
