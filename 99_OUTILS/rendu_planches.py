#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rasteriseur de contrôle pour les planches.

Ne sert QU'À VÉRIFIER le dessin : il ne comprend que le sous-ensemble de SVG
produit par planches.py (rect, circle, ellipse, line, path M/L/Q/q/l/a/Z,
et les trames, approximées par un gris de densité équivalente).

    python 99_OUTILS/rendu_planches.py

Écrit des PNG dans docs/planches/_controle/. Ces fichiers ne partent pas en
ligne : le site sert les SVG, qui sont nets à toute taille et suivent le thème.
"""

import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def _police(taille):
    for base in (r"C:\Windows\Fonts", "/System/Library/Fonts",
                 "/usr/share/fonts/truetype/dejavu"):
        for n in ("consola.ttf", "Menlo.ttc", "DejaVuSansMono.ttf"):
            f = Path(base) / n
            if f.exists():
                try:
                    return ImageFont.truetype(str(f), taille)
                except Exception:
                    pass
    return ImageFont.load_default()

RACINE = Path(__file__).resolve().parent.parent
SRC = RACINE / "docs" / "planches"
DST = RACINE / "99_OUTILS" / "_controle_planches"

ECHELLE = 2          # suréchantillonnage pour lisser
NOIR = (17, 17, 17)
BLANC = (255, 255, 255)

# les trames, rendues par un gris de densité voisine
GRIS = {"t1": (214, 214, 214), "t2": (186, 186, 186),
        "t3": (150, 150, 150), "hach": (170, 170, 170), "fondu": (120, 120, 120)}


def couleur(v, defaut=None):
    if v is None or v in ("none", ""):
        return defaut
    m = re.match(r"url\(#([\w-]+)\)", v)
    if m:
        return GRIS.get(m.group(1), (190, 190, 190))
    if "--pl-ink" in v:
        return NOIR
    if "--pl-paper" in v:
        return BLANC
    if v.startswith("#"):
        v = v.lstrip("#")
        if len(v) == 3:
            v = "".join(c * 2 for c in v)
        return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))
    return defaut


def melange(base, dessus, a):
    return tuple(int(b + (d - b) * a) for b, d in zip(base, dessus))


def nombre(e, k, d=0.0):
    v = e.get(k)
    if v is None:
        return d
    v = v.strip().rstrip("%")
    try:
        return float(v)
    except ValueError:
        return d


def chemin_points(d, ech):
    """Convertit un attribut d en une liste de sous-chemins (listes de points)."""
    jetons = re.findall(r"[MmLlQqAaZzHhVv]|-?\d*\.?\d+(?:e-?\d+)?", d)
    sous, cur, x, y, dep = [], [], 0.0, 0.0, (0.0, 0.0)
    i, cmd = 0, None
    while i < len(jetons):
        t = jetons[i]
        if t.isalpha():
            cmd = t
            i += 1
            if cmd in "Zz":
                if cur:
                    cur.append(dep)
                    sous.append(cur)
                    cur = []
                x, y = dep
            continue
        n = lambda k: float(jetons[i + k])
        if cmd in "Mm":
            nx, ny = (n(0), n(1)) if cmd == "M" else (x + n(0), y + n(1))
            if cur:
                sous.append(cur)
            x, y = nx, ny
            dep = (x, y)
            cur = [(x, y)]
            i += 2
            cmd = "L" if cmd == "M" else "l"
        elif cmd in "Ll":
            nx, ny = (n(0), n(1)) if cmd == "L" else (x + n(0), y + n(1))
            cur.append((nx, ny))
            x, y = nx, ny
            i += 2
        elif cmd in "Hh":
            nx = n(0) if cmd == "H" else x + n(0)
            cur.append((nx, y))
            x = nx
            i += 1
        elif cmd in "Vv":
            ny = n(0) if cmd == "V" else y + n(0)
            cur.append((x, ny))
            y = ny
            i += 1
        elif cmd in "Qq":
            if cmd == "Q":
                cx, cy, nx, ny = n(0), n(1), n(2), n(3)
            else:
                cx, cy, nx, ny = x + n(0), y + n(1), x + n(2), y + n(3)
            for s in range(1, 17):
                u = s / 16
                px = (1 - u) ** 2 * x + 2 * (1 - u) * u * cx + u * u * nx
                py = (1 - u) ** 2 * y + 2 * (1 - u) * u * cy + u * u * ny
                cur.append((px, py))
            x, y = nx, ny
            i += 4
        elif cmd in "Aa":
            rx, ry = n(0), n(1)
            nx, ny = (n(5), n(6)) if cmd == "A" else (x + n(5), y + n(6))
            balayage = n(4)
            mx, my = (x + nx) / 2, (y + ny) / 2
            dx, dy = nx - x, ny - y
            long = math.hypot(dx, dy) or 1
            fl = 1 if balayage else -1
            bx, by = mx - dy / long * rx * .55 * fl, my + dx / long * ry * .55 * fl
            for s in range(1, 21):
                u = s / 20
                px = (1 - u) ** 2 * x + 2 * (1 - u) * u * bx + u * u * nx
                py = (1 - u) ** 2 * y + 2 * (1 - u) * u * by + u * u * ny
                cur.append((px, py))
            x, y = nx, ny
            i += 7
        else:
            i += 1
    if cur:
        sous.append(cur)
    return [[(px * ech, py * ech) for px, py in s] for s in sous if len(s) > 1]


def dessiner(e, toile, ech, herite):
    """Compose l'élément sur `toile` (RGBA). Chaque forme passe par son propre
    calque transparent : c'est le seul moyen de rendre correctement à la fois
    les aplats blancs et les opacités partielles."""
    tag = e.tag.split("}")[-1]
    if tag in ("defs", "pattern", "linearGradient", "stop"):
        return toile

    a_fill = e.get("fill")
    a_stroke = e.get("stroke")
    fill = couleur(a_fill, herite.get("fill")) if a_fill or herite.get("fill") else None
    stroke = couleur(a_stroke, herite.get("stroke")) if a_stroke else None
    sw = max(1, int(round(nombre(e, "stroke-width", 1) * ech)))
    op = nombre(e, "opacity", herite.get("opacity", 1.0))
    alpha = max(0, min(255, int(round(255 * op))))

    fa = fill + (alpha,) if fill else None
    sa = stroke + (alpha,) if stroke else None

    if tag == "text":
        calque = Image.new("RGBA", toile.size, (0, 0, 0, 0))
        cd = ImageDraw.Draw(calque)
        taille = int(nombre(e, "font-size", 16) * ech)
        ancre = {"start": "ls", "middle": "ms", "end": "rs"}.get(
            e.get("text-anchor", "start"), "ls")
        txt = (e.text or "").replace("&amp;", "&")
        cd.text((nombre(e, "x") * ech, nombre(e, "y") * ech), txt,
                font=_police(taille), fill=(fill or NOIR) + (alpha,), anchor=ancre)
        toile = Image.alpha_composite(toile, calque)

    if tag in ("rect", "circle", "ellipse", "line", "path"):
        calque = Image.new("RGBA", toile.size, (0, 0, 0, 0))
        cd = ImageDraw.Draw(calque)

        if tag == "rect":
            x, y = nombre(e, "x") * ech, nombre(e, "y") * ech
            # les pourcentages se résolvent sur la dimension correspondante :
            # sans ça un fond en width="100%" devient un carré de 100 pixels.
            bw, bh = toile.size
            vw, vh = e.get("width", ""), e.get("height", "")
            w = (bw * float(vw.rstrip("%")) / 100 if vw.endswith("%")
                 else nombre(e, "width", bw / ech) * ech)
            h = (bh * float(vh.rstrip("%")) / 100 if vh.endswith("%")
                 else nombre(e, "height", bh / ech) * ech)
            if fa:
                cd.rectangle([x, y, x + w, y + h], fill=fa)
        elif tag == "circle":
            cx, cy, r = nombre(e, "cx") * ech, nombre(e, "cy") * ech, nombre(e, "r") * ech
            cd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fa, outline=sa, width=sw)
        elif tag == "ellipse":
            cx, cy = nombre(e, "cx") * ech, nombre(e, "cy") * ech
            rx, ry = nombre(e, "rx") * ech, nombre(e, "ry") * ech
            cd.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fa, outline=sa, width=sw)
        elif tag == "line":
            cd.line([nombre(e, "x1") * ech, nombre(e, "y1") * ech,
                     nombre(e, "x2") * ech, nombre(e, "y2") * ech],
                    fill=sa or (NOIR + (alpha,)), width=sw)
        elif tag == "path":
            for pts in chemin_points(e.get("d", ""), ech):
                if fa and len(pts) > 2:
                    cd.polygon(pts, fill=fa)
                if sa:
                    cd.line(pts, fill=sa, width=sw, joint="curve")

        toile = Image.alpha_composite(toile, calque)

    fils = {"fill": fill if a_fill else herite.get("fill"),
            "stroke": stroke if a_stroke else herite.get("stroke"),
            "opacity": op}
    for enfant in e:
        toile = dessiner(enfant, toile, ech, fils)
    return toile


def rendre(chemin_svg, sortie):
    racine = ET.fromstring(chemin_svg.read_text(encoding="utf-8"))
    vb = [float(v) for v in racine.get("viewBox").split()]
    w, h = int(vb[2] * ECHELLE), int(vb[3] * ECHELLE)
    toile = Image.new("RGBA", (w, h), BLANC + (255,))
    for e in racine:
        toile = dessiner(e, toile, ECHELLE, {"fill": None, "stroke": None, "opacity": 1.0})
    im = toile.convert("RGB").resize((int(vb[2]), int(vb[3])), Image.LANCZOS)
    im.save(sortie, "PNG", optimize=True)


if __name__ == "__main__":
    DST.mkdir(parents=True, exist_ok=True)
    for f in sorted(SRC.glob("*.svg")):
        rendre(f, DST / (f.stem + ".png"))
        print("rendu %s" % f.name)
    # planche de contact unique
    fichiers = sorted(DST.glob("*.png"))
    ims = [Image.open(f) for f in fichiers]
    larg = 800
    vign = [i.resize((larg, int(i.height * larg / i.width)), Image.LANCZOS) for i in ims]
    total = sum(v.height + 10 for v in vign)
    feuille = Image.new("RGB", (larg, total), (245, 245, 245))
    y = 0
    for v in vign:
        feuille.paste(v, (0, y))
        y += v.height + 10
    feuille.save(DST / "_contact.png", "PNG", optimize=True)
    print("planche de contact : %s" % (DST / "_contact.png"))
