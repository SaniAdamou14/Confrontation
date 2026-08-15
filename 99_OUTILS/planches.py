#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Planches du Poids des dieux — dessin au trait, encre et papier.

Généré, pas dessiné à la main : les silhouettes urbaines, les trames et les
graviers sont posés par un générateur à graine fixe, donc identiques à chaque
build. Appelé par build_site.py.

RÈGLES DE LA SÉRIE, tenues sur les onze planches :

  1. DEUX TONS. De l'encre et du papier. Aucun gris — les demi-teintes
     passent par la trame, comme en impression manga.
  2. LE SUJET EST MINUSCULE. Jamais plus de quelques pour cent de la surface.
     Le vide fait le travail, c'est la grammaire du livre.
  3. AUCUN VISAGE. Le personnage est une silhouette, jamais un portrait.
     C'est une contrainte assumée : ce récit regarde ses dieux de loin,
     par les yeux de gens qui ne comprennent pas ce qu'ils voient.
  4. LE THÈME INVERSE LA PLANCHE. Encre noire sur papier blanc en clair,
     encre claire sur fond sombre en sombre. La composition ne change pas.
"""

import random

L, H = 1600, 640          # format des planches de chapitre
HF = 900                  # hauteur du frontispice

INK = "var(--pl-ink)"
PAP = "var(--pl-paper)"


# ---------------------------------------------------------------- outils

def defs():
    """Trames de demi-teinte, trois densités, plus une hachure."""
    t = []
    for nom, pas, r in (("t1", 14, 1.1), ("t2", 10, 1.5), ("t3", 7, 1.8)):
        t.append(
            '<pattern id="%s" width="%d" height="%d" patternUnits="userSpaceOnUse">'
            '<circle cx="%g" cy="%g" r="%g" fill="%s"/></pattern>'
            % (nom, pas, pas, pas / 2, pas / 2, r, INK))
    t.append(
        '<pattern id="hach" width="9" height="9" patternUnits="userSpaceOnUse" '
        'patternTransform="rotate(35)">'
        '<line x1="0" y1="0" x2="0" y2="9" stroke="%s" stroke-width="1.6"/></pattern>' % INK)
    t.append(
        '<linearGradient id="fondu" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="%s" stop-opacity="0"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="1"/></linearGradient>' % (INK, INK))
    return "<defs>" + "".join(t) + "</defs>"


def fond():
    return '<rect width="100%%" height="100%%" fill="%s"/>' % PAP


def trame(x, y, w, h, niveau="t1", opacite=1.0):
    return ('<rect x="%g" y="%g" width="%g" height="%g" fill="url(#%s)" opacity="%g"/>'
            % (x, y, w, h, niveau, opacite))


def silhouette(x, sol, haut, rng=None, assis=False, penche=0.0,
               miroir=False, creux=False):
    """Une personne vue de loin. Une forme, jamais un portrait.

    Proportions réelles — tête au septième, épaules plus larges que les hanches,
    jambes séparées, bras détachés du corps. Sans ça on obtient un pictogramme
    de signalétique, et un pictogramme ne raconte rien.
    """
    h = haut
    s = -1 if miroir else 1
    if not assis:
        te = h * 0.064                        # rayon de tête
        ep = h * 0.118                        # demi-épaules
        ha = h * 0.088                        # demi-hanches
        d = penche * h * 0.10 * s             # inclinaison du buste

        pts = [
            (x - ep + d, sol - h * 0.855),
            (x - ep * 1.16 + d * .8, sol - h * 0.60),
            (x - ep * 0.86 + d * .6, sol - h * 0.50),
            (x - ha, sol - h * 0.455),
            (x - ha * 0.92, sol),
            (x - ha * 0.22, sol),
            (x, sol - h * 0.285),
            (x + ha * 0.22, sol),
            (x + ha * 0.92, sol),
            (x + ha, sol - h * 0.455),
            (x + ep * 0.86 + d * .6, sol - h * 0.50),
            (x + ep * 1.16 + d * .8, sol - h * 0.60),
            (x + ep + d, sol - h * 0.855),
        ]
        corps = '<path d="M%s Z"/>' % " L".join("%g %g" % p for p in pts)
        cou = '<rect x="%g" y="%g" width="%g" height="%g"/>' % (
            x - te * 0.42 + d, sol - h * 0.885, te * 0.84, h * 0.045)
        tete = '<ellipse cx="%g" cy="%g" rx="%g" ry="%g"/>' % (
            x + d * 1.25, sol - h * 0.935, te * 0.92, te)
        peau = ('fill="%s" stroke="%s" stroke-width="%g"'
                % (PAP, INK, max(1.6, h * .045))) if creux else 'fill="%s"' % INK
        return '<g %s>%s%s%s</g>' % (peau, corps, cou, tete)

    t = h * 0.16
    ep = h * 0.20
    if assis:
        # De trois quarts, les avant-bras sur les cuisses : tête, buste penché,
        # cuisse horizontale, jambe qui descend. Quatre formes, pas une de plus.
        te = h * 0.072
        tete = '<ellipse cx="%g" cy="%g" rx="%g" ry="%g"/>' % (
            x - h * .02, sol - h * 0.80, te * .92, te)
        cou = '<rect x="%g" y="%g" width="%g" height="%g"/>' % (
            x - te * .34, sol - h * 0.755, te * .68, h * .04)
        buste = '<path d="M%g %g L%g %g L%g %g L%g %g Z"/>' % (
            x - h * 0.085, sol - h * 0.735,
            x + h * 0.080, sol - h * 0.715,
            x + h * 0.098, sol - h * 0.315,
            x - h * 0.072, sol - h * 0.335)
        # un seul bras : l'autre manche est vide, et ça ne se commente pas
        bras = '<path d="M%g %g L%g %g L%g %g L%g %g Z"/>' % (
            x + h * 0.062, sol - h * 0.690,
            x + h * 0.108, sol - h * 0.660,
            x + h * 0.140, sol - h * 0.360,
            x + h * 0.092, sol - h * 0.370)
        cuisse = '<rect x="%g" y="%g" width="%g" height="%g" rx="%g"/>' % (
            x - h * 0.075, sol - h * 0.335, h * 0.235, h * 0.105, h * 0.035)
        mollet = '<rect x="%g" y="%g" width="%g" height="%g"/>' % (
            x + h * 0.108, sol - h * 0.240, h * 0.062, h * 0.240)
        pied = '<rect x="%g" y="%g" width="%g" height="%g" rx="%g"/>' % (
            x + h * 0.092, sol - h * 0.030, h * 0.115, h * 0.032, h * .012)
        return '<g fill="%s">%s%s%s%s%s%s%s</g>' % (
            INK, tete, cou, buste, bras, cuisse, mollet, pied)
    return ('<g fill="%s">'
            '<circle cx="%g" cy="%g" r="%g"/>'
            '<path d="M%g %g L%g %g L%g %g L%g %g Z"/>'
            '</g>' % (
                INK, x, sol - h * 0.90, t,
                x - ep, sol - h * 0.72, x + ep, sol - h * 0.72,
                x + ep * 0.62, sol, x - ep * 0.62, sol))


def ville(rng, x0, x1, sol, mini, maxi, fenetres=True, pas=None):
    """Silhouette urbaine en aplat, avec quelques fenêtres évidées."""
    out, x = [], x0
    while x < x1:
        w = pas or rng.randint(38, 96)
        h = rng.randint(mini, maxi)
        out.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>'
                   % (x, sol - h, w, h, INK))
        if fenetres and w > 46 and h > 90 and rng.random() < .8:
            for i in range(rng.randint(2, 5)):
                fx = x + 10 + rng.random() * (w - 24)
                fy = sol - h + 16 + rng.random() * (h - 40)
                out.append('<rect x="%g" y="%g" width="7" height="10" fill="%s" opacity=".85"/>'
                           % (fx, fy, PAP))
        x += w + rng.randint(3, 12)
    return "".join(out)


def rayons(cx, cy, n, r0, r1, rng, largeur=2.2, opacite=.9):
    """Lignes de fuite — le trait de concentration du manga."""
    out = []
    for i in range(n):
        a = (i / n) * 6.28318 + rng.random() * .06
        import math
        c, s = math.cos(a), math.sin(a)
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                   'stroke-width="%g" opacity="%g"/>'
                   % (cx + c * r0, cy + s * r0, cx + c * r1, cy + s * r1,
                      INK, largeur, opacite))
    return "".join(out)


def enveloppe(contenu, h=H):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
            'preserveAspectRatio="xMidYMid slice" role="img">%s%s%s</svg>'
            % (L, h, defs(), fond(), contenu))


# ---------------------------------------------------------------- planches

def frontispice():
    """La déchirure au-dessus de State Street."""
    r = random.Random(7)
    o = [trame(0, 0, L, 700, "t1", .55)]
    o.append(rayons(1000, 320, 56, 0, 1000, r, 1.5, .26))
    # La déchirure. Deux bords en dents irrégulières, jamais symétriques :
    # une fente symétrique se lit comme un œil, pas comme une cassure.
    import math

    def fente(cx, y0, y1, larg, jitter, graine):
        g = random.Random(graine)
        n = 26
        gauche, droite = [], []
        for i in range(n + 1):
            t = i / n
            y = y0 + (y1 - y0) * t
            p = math.sin(math.pi * t) ** 0.62
            gauche.append((cx - larg * p + g.uniform(-jitter, jitter), y))
            droite.append((cx + larg * p * g.uniform(.75, 1.25)
                           + g.uniform(-jitter, jitter), y))
        pts = gauche + droite[::-1]
        return "M" + " L".join("%g %g" % q for q in pts) + " Z"

    o.append('<path d="%s" fill="%s"/>' % (fente(1000, 34, 648, 58, 9, 11), INK))
    o.append('<path d="%s" fill="%s"/>' % (fente(1002, 62, 610, 30, 6, 23), PAP))
    # éclats latéraux, comme un pare-brise qui part
    g = random.Random(31)
    for i in range(7):
        y = 120 + i * 66 + g.randint(-14, 14)
        s = 1 if i % 2 else -1
        lg = g.randint(70, 150)
        o.append('<path d="M%g %g l%g %g l%g %g z" fill="%s"/>'
                 % (1000 + s * 26, y, s * lg, g.randint(-26, -8),
                    -s * lg * .78, g.randint(14, 26), INK))
    # une seule ville, en aplat plein
    o.append(ville(r, -30, L + 40, HF, 170, 430))
    o.append('<rect x="0" y="%d" width="%d" height="52" fill="%s"/>' % (HF - 52, L, INK))
    return enveloppe("".join(o), HF)


def p1():
    """State Street. Le feu suspendu, et quelqu'un au bout de la rue."""
    r = random.Random(1)
    o = [trame(0, 0, L, 300, "t1", .5)]
    o.append('<path d="M0 640 L0 60 L360 190 L360 640 Z" fill="%s"/>' % INK)
    o.append('<path d="M1600 640 L1600 40 L1210 175 L1210 640 Z" fill="%s"/>' % INK)
    o.append('<g opacity=".9">%s</g>' % ville(r, 370, 1205, 470, 40, 150, True, 58))
    # chaussée
    o.append('<path d="M360 640 L1240 640 L980 470 L640 470 Z" fill="url(#t2)" opacity=".5"/>')
    for i in range(5):
        y = 500 + i * 30
        o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="3" '
                 'opacity=".55"/>' % (790 - i * 26, y, 830 + i * 26, y, INK))
    o.append(silhouette(812, 470, 26))
    # le feu, au premier plan
    o.append('<line x1="0" y1="96" x2="1600" y2="128" stroke="%s" stroke-width="4"/>' % INK)
    o.append('<g><rect x="742" y="112" width="116" height="252" rx="14" fill="%s"/>' % INK)
    for k, cy in enumerate((176, 240, 304)):
        o.append('<circle cx="800" cy="%g" r="30" fill="%s" opacity="%s"/>'
                 % (cy, PAP, ".95" if k == 0 else ".28"))
    o.append("</g>")
    return enveloppe("".join(o))


def p2():
    """La cabine. Un pare-brise fendu, une colonne au loin."""
    r = random.Random(2)
    o = [trame(0, 0, L, 640, "t1", .45)]
    o.append('<path d="M300 120 Q800 60 1300 120 L1330 470 Q800 520 270 470 Z" fill="%s"/>' % PAP)
    o.append('<path d="M300 120 Q800 60 1300 120 L1330 470 Q800 520 270 470 Z" '
             'fill="none" stroke="%s" stroke-width="7"/>' % INK)
    o.append('<path d="M0 0 H1600 V640 H0 Z M300 120 Q800 60 1300 120 L1330 470 '
             'Q800 520 270 470 Z" fill="%s" fill-rule="evenodd"/>' % INK)
    # au-dehors
    o.append('<g clip-path="none" opacity=".95">')
    o.append('<path d="M300 380 Q800 356 1330 380 L1330 470 Q800 520 270 470 Z" fill="%s"/>' % INK)
    o.append('<path d="M900 380 Q874 250 906 150 Q938 66 918 20 L1010 20 '
             'Q1000 90 1024 170 Q1052 268 1020 380 Z" fill="url(#t3)" opacity=".85"/>')
    o.append('<g opacity=".8">%s</g>' % ville(r, 320, 880, 380, 14, 54, False, 40))
    o.append("</g>")
    # la fente
    o.append('<path d="M470 148 L742 300 L690 470" stroke="%s" stroke-width="5" fill="none"/>' % INK)
    o.append('<path d="M742 300 L860 262 M742 300 L800 392" stroke="%s" stroke-width="3" '
             'fill="none"/>' % INK)
    # pale
    o.append('<path d="M0 40 Q700 96 1600 26 L1600 0 L0 0 Z" fill="%s"/>' % INK)
    return enveloppe("".join(o))


def p3():
    """La chambre. Un enfant assis sur le lit, pas dedans, et une lampe."""
    o = ['<rect width="100%" height="100%" fill="' + INK + '"/>']
    # la porte entrouverte — la seule source de papier de la planche
    o.append('<rect x="128" y="52" width="188" height="588" fill="%s"/>' % PAP)
    o.append('<rect x="316" y="52" width="16" height="588" fill="%s"/>' % INK)
    o.append('<path d="M128 40 L332 52 L332 640 L128 640 Z" fill="none" '
             'stroke="%s" stroke-width="3" opacity=".5"/>' % PAP)
    # la trainée de lumière au sol, en biais
    o.append('<path d="M332 496 L332 640 L1180 640 L640 496 Z" fill="url(#t2)" opacity=".45"/>')
    o.append('<path d="M332 520 L332 640 L900 640 L560 520 Z" fill="url(#t3)" opacity=".3"/>')
    # la lampe éclaire AVANT que l'enfant soit posé : il doit se détourer
    # dessus. Une silhouette d'encre sur un fond d'encre ne se voit pas.
    o.append('<circle cx="1230" cy="330" r="330" fill="url(#t1)" opacity=".30"/>')
    o.append('<circle cx="1300" cy="356" r="212" fill="url(#t2)" opacity=".34"/>')
    o.append('<circle cx="1392" cy="384" r="104" fill="url(#t3)" opacity=".40"/>')
    # le lit : un plateau et deux pieds
    o.append('<rect x="700" y="470" width="640" height="22" fill="%s"/>' % PAP)
    o.append('<rect x="716" y="492" width="16" height="112" fill="%s"/>' % PAP)
    o.append('<rect x="1308" y="492" width="16" height="112" fill="%s"/>' % PAP)
    # la lampe de chevet, allumée
    o.append('<rect x="1397" y="396" width="10" height="74" fill="%s"/>' % PAP)
    o.append('<path d="M1360 396 L1444 396 L1428 350 L1376 350 Z" fill="%s"/>' % PAP)
    # l'enfant, assis au bord du lit, à contre-jour — un seul bras
    o.append(silhouette(1128, 470, 178, assis=True))
    return enveloppe("".join(o))


# ------------------------------------------------ planches intérieures
# Placées au sommet du chapitre, pas en tête : le light novel met sa pleine
# page au moment le plus chaud, et c'est là qu'elle sert à quelque chose.

def p1b():
    """17 h 03. La sphère. Le seul effet de zone du tome."""
    r = random.Random(101)
    o = [trame(0, 0, L, 640, "t1", .4)]
    cx, cy, rad = 1010, 268, 176
    o.append(rayons(cx, cy, 90, rad, 1500, r, 3.2, .85))
    o.append('<circle cx="%g" cy="%g" r="%g" fill="%s"/>' % (cx, cy, rad + 26, INK))
    o.append('<circle cx="%g" cy="%g" r="%g" fill="%s"/>' % (cx, cy, rad, PAP))
    # la rue en dessous, qui part en morceaux
    o.append('<rect x="0" y="596" width="1600" height="44" fill="%s"/>' % INK)
    for i in range(26):
        x = r.randint(0, 1580)
        h = r.randint(10, 70)
        w = r.randint(8, 34)
        y = 596 - h - r.randint(0, 130)
        o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s" '
                 'transform="rotate(%g %g %g)"/>'
                 % (x, y, w, h, INK, r.randint(-40, 40), x + w / 2, y + h / 2))
    o.append('<g opacity=".9">%s</g>' % ville(r, -20, 560, 596, 60, 300, False, 54))
    o.append('<g opacity=".9">%s</g>' % ville(r, 1420, L + 40, 596, 60, 280, False, 54))
    return enveloppe("".join(o))


def p2b():
    """16 h 54. Une ligne blanche sur quatre cents mètres."""
    r = random.Random(102)
    o = [trame(0, 0, L, 640, "t1", .35)]
    o.append('<rect x="0" y="286" width="1600" height="354" fill="%s"/>' % INK)
    o.append('<g opacity="1">%s</g>' % ville(r, -20, L + 40, 286, 40, 210, False, 66))
    # la ligne, parfaitement droite, qui traverse tout
    o.append('<rect x="0" y="352" width="1600" height="9" fill="%s"/>' % PAP)
    o.append('<rect x="0" y="346" width="1600" height="21" fill="%s" opacity=".28"/>' % PAP)
    # les trous qu'elle laisse dans deux façades, centrés sur la ligne
    for x, w in ((402, 124), (1102, 152)):
        o.append('<path d="M%g 334 l%g -6 l4 52 l%g 6 z" fill="%s"/>'
                 % (x, w, -w, PAP))
    # des morceaux qui tombent — en papier, sinon ils disparaissent dans la masse
    g = random.Random(202)
    for i in range(9):
        x = 300 + g.randint(0, 1100)
        y = 396 + g.randint(0, 150)
        t = g.randint(14, 40)
        o.append('<path d="M%g %g l%g %g l%g %g z" fill="%s" opacity=".9"/>'
                 % (x, y, t, g.randint(6, 20), -g.randint(6, 22), t, PAP))
    return enveloppe("".join(o))


def p4b():
    """J2, 11 h 05. Ils se sont éteints ensemble, et il en regardait un."""
    r = random.Random(104)
    o = [trame(0, 0, L, 452, "t1", .40)]
    o.append('<line x1="0" y1="452" x2="1600" y2="452" stroke="%s" stroke-width="3"/>' % INK)
    o.append('<rect x="0" y="452" width="1600" height="188" fill="url(#t2)" opacity=".28"/>')
    # l'herbe couchée, dans un seul sens
    for i in range(190):
        x = r.randint(0, 1600)
        y = r.randint(456, 636)
        o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                 'stroke-width="1.4" opacity=".45"/>' % (x, y, x + 13, y - 4, INK))
    # la ligne : des contours vides. Ils étaient là et ils n'y sont plus,
    # et rien dans l'image ne dit ce qui s'est passé entre les deux.
    n = 23
    for i in range(n):
        x = 88 + i * 64
        if i == 5:
            continue
        o.append(silhouette(x, 452, 46 + (3 if i % 3 else 0),
                            miroir=(i % 2 == 0), creux=True))
    # le sixième, plein — le seul que quelqu'un ait regardé
    o.append(silhouette(88 + 5 * 64, 452, 56, penche=.28))
    return enveloppe("".join(o))


def p5b():
    """J4, 17 h 44. Le tri. Quatre secondes, et personne ne monte les chercher."""
    r = random.Random(105)
    o = [trame(0, 0, L, 360, "t1", .42)]
    # l'arête, en aplat
    o.append('<path d="M0 640 L0 470 L300 424 L640 356 L900 372 L1210 300 L1600 338 '
             'L1600 640 Z" fill="%s"/>' % INK)
    o.append('<path d="M0 470 L300 424 L640 356 L900 372 L1210 300 L1600 338" '
             'stroke="%s" stroke-width="3" fill="none" opacity=".45"/>' % PAP)
    # la selle est : un debout, deux à terre
    o.append(silhouette(548, 372, 58))
    o.append('<rect x="592" y="362" width="76" height="12" rx="6" fill="%s"/>' % PAP)
    o.append('<rect x="676" y="368" width="68" height="11" rx="5.5" fill="%s"/>' % PAP)
    # lui, assis du côté du vide, très loin
    o.append(silhouette(1246, 300, 50, assis=True))
    # le boîtier, dix mètres plus bas, qui émet toute la nuit
    o.append('<rect x="516" y="470" width="26" height="17" rx="3" fill="%s"/>' % PAP)
    for k in (1, 2, 3):
        o.append('<path d="M%g %g a%g %g 0 0 1 0 %g" fill="none" stroke="%s" '
                 'stroke-width="2.4" opacity="%g"/>'
                 % (546 + k * 13, 470 - k * 7, k * 13, k * 13, 24 + k * 14, PAP, .8 - k * .18))
    # les cailloux de la pente
    for i in range(70):
        o.append('<circle cx="%g" cy="%g" r="%g" fill="%s" opacity=".5"/>'
                 % (r.randint(300, 900), r.randint(390, 630),
                    r.choice((2, 3, 4)), PAP))
    return enveloppe("".join(o))


def p7b():
    """Le rétroviseur. Vingt ans d'habitude, et la banquette est vide."""
    r = random.Random(107)
    o = ['<rect width="100%" height="100%" fill="' + INK + '"/>']
    # le pare-brise : la route qui fuit
    o.append('<path d="M300 640 L640 392 L960 392 L1300 640 Z" fill="url(#t2)" opacity=".4"/>')
    for i in range(7):
        t = i / 7.0
        y = 640 - t * 240
        w = 46 - t * 38
        o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s" opacity="%g"/>'
                 % (800 - w / 2, y - 34 + t * 22, w, 30 - t * 24, PAP, .9 - t * .5))
    # le rétroviseur
    o.append('<rect x="452" y="112" width="700" height="216" rx="26" fill="%s"/>' % PAP)
    o.append('<rect x="470" y="130" width="664" height="180" rx="16" fill="%s"/>' % INK)
    # dedans : la banquette arrière, et rien dessus
    o.append('<rect x="470" y="248" width="664" height="62" fill="url(#t1)" opacity=".55"/>')
    o.append('<rect x="470" y="240" width="664" height="10" fill="%s" opacity=".7"/>' % PAP)
    for x in (556, 762, 968):
        o.append('<rect x="%g" y="176" width="86" height="66" rx="12" fill="url(#t2)" '
                 'opacity=".45"/>' % x)
    o.append('<rect x="770" y="66" width="20" height="52" fill="%s"/>' % PAP)
    return enveloppe("".join(o))


def p8b():
    """Une porte ouverte de trente centimètres, et le jour de l'ouest."""
    o = ['<rect width="100%" height="100%" fill="' + INK + '"/>']
    # l'embrasure
    o.append('<rect x="1006" y="0" width="14" height="640" fill="%s" opacity=".55"/>' % PAP)
    o.append('<path d="M1020 44 L1148 78 L1148 596 L1020 628 Z" fill="%s"/>' % PAP)
    o.append('<path d="M1148 78 L1176 96 L1176 580 L1148 596 Z" fill="url(#t2)" opacity=".5"/>')
    # la bande de jour en travers de la moquette
    o.append('<path d="M1020 470 L1148 452 L560 640 L212 640 Z" fill="url(#t1)" opacity=".6"/>')
    o.append('<path d="M1020 500 L1120 486 L700 640 L410 640 Z" fill="url(#t3)" opacity=".38"/>')
    # la plinthe et le montant, pour donner l'échelle
    o.append('<rect x="0" y="596" width="1006" height="9" fill="%s" opacity=".35"/>' % PAP)
    o.append('<rect x="980" y="0" width="26" height="640" fill="%s" opacity=".18"/>' % PAP)
    return enveloppe("".join(o))


PLANCHES_INTERIEURES = {
    1: (4, p1b), 2: (5, p2b), 4: (3, p4b),
    5: (3, p5b), 7: (5, p7b), 8: (5, p8b),
}


def p4():
    """Le bord ouest. Une ligne de cent quatre-vingt-douze, et un homme assis."""
    r = random.Random(4)
    o = [trame(0, 0, L, 340, "t1", .5)]
    o.append('<path d="M0 640 L0 300 Q420 250 760 330 Q1180 430 1600 330 L1600 640 Z" '
             'fill="%s"/>' % INK)
    o.append('<path d="M0 300 Q420 250 760 330 Q1180 430 1600 330" stroke="%s" '
             'stroke-width="4" fill="none" opacity=".6"/>' % PAP)
    # vapeur
    for x, w in ((260, 200), (700, 260), (1180, 220)):
        o.append('<path d="M%g 320 q%g -190 %g -230 q%g 60 %g 230 z" fill="url(#t2)" '
                 'opacity=".5"/>' % (x, w * .2, w * .5, w * .3, w * .5))
    # la ligne des corps
    for i in range(34):
        x = 120 + i * 40
        y = 372 + (i * 2.1)
        o.append('<rect x="%g" y="%g" width="26" height="7" rx="3.5" fill="%s" opacity=".95"/>'
                 % (x, y, PAP))
    o.append(silhouette(1372, 470, 54, assis=True))
    o.append('<rect x="1300" y="470" width="150" height="9" fill="%s" opacity=".8"/>' % PAP)
    return enveloppe("".join(o))


def p5():
    """La crête. Un homme assis du côté du vide, une ville en dessous."""
    r = random.Random(5)
    o = [trame(0, 0, L, 420, "t1", .45)]
    o.append('<path d="M0 640 L0 470 L280 402 L640 336 L980 366 L1310 300 L1600 344 '
             'L1600 640 Z" fill="%s"/>' % INK)
    o.append(silhouette(1004, 366, 62, assis=True))
    # la ville en contrebas, par rangées
    o.append('<g opacity=".9">')
    for ligne in range(7):
        y = 520 + ligne * 16
        for i in range(26):
            x = 120 + i * 52 + (ligne % 2) * 22
            if r.random() < .78:
                o.append('<rect x="%g" y="%g" width="6" height="6" fill="%s"/>' % (x, y, PAP))
    o.append("</g>")
    o.append('<circle cx="250" cy="130" r="7" fill="%s" opacity=".8"/>' % INK)
    return enveloppe("".join(o))


def p6():
    """La première image. De l'eau noire, ronde, où les rues s'arrêtent."""
    r = random.Random(6)
    o = [trame(0, 0, L, 640, "t1", .30)]
    cx, cy, rad = 800, 316, 246
    # trame de rues
    for i in range(-8, 9):
        o.append('<line x1="%g" y1="0" x2="%g" y2="640" stroke="%s" stroke-width="2" '
                 'opacity=".45"/>' % (800 + i * 94, 800 + i * 94, INK))
    for i in range(-4, 5):
        o.append('<line x1="0" y1="%g" x2="1600" y2="%g" stroke="%s" stroke-width="2" '
                 'opacity=".45"/>' % (316 + i * 78, 316 + i * 78, INK))
    import math
    for gx in range(-8, 8):
        for gy in range(-4, 4):
            x0 = 800 + gx * 94
            y0 = 316 + gy * 78
            if math.hypot(x0 + 47 - cx, y0 + 39 - cy) < rad + 46:
                continue
            if r.random() < .30:
                continue
            m = r.randint(8, 20)
            o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s" opacity=".82"/>'
                     % (x0 + m, y0 + m * .7, 94 - m * 2, 78 - m * 1.4, INK))
    o.append('<circle cx="%g" cy="%g" r="%g" fill="%s"/>' % (cx, cy, rad, INK))
    o.append('<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="5"/>'
             % (cx, cy, rad, PAP))
    return enveloppe("".join(o))


def p7():
    """Le chambranle. Vingt-deux ans de traits, et quatre neufs."""
    o = [trame(0, 0, L, 640, "t1", .28)]
    o.append('<rect x="596" y="0" width="30" height="640" fill="%s"/>' % INK)
    o.append('<rect x="626" y="0" width="10" height="640" fill="url(#hach)" opacity=".5"/>')
    anciens = [(566, 60), (556, 100), (572, 140), (548, 184), (566, 226),
               (540, 268), (558, 306), (536, 348), (552, 386), (530, 424),
               (546, 462), (528, 500)]
    for x, y in anciens:
        o.append('<line x1="%g" y1="%g" x2="596" y2="%g" stroke="%s" stroke-width="4"/>'
                 % (x, y, y, INK))
        o.append('<rect x="%g" y="%g" width="22" height="4" fill="%s" opacity=".45"/>'
                 % (x - 34, y - 2, INK))
    for i, y in enumerate((452, 470, 488, 506)):
        o.append('<line x1="640" y1="%g" x2="686" y2="%g" stroke="%s" stroke-width="4" '
                 'opacity=".9"/>' % (y, y, INK))
    o.append('<line x1="0" y1="600" x2="1600" y2="600" stroke="%s" stroke-width="6"/>' % INK)
    o.append('<rect x="1180" y="470" width="14" height="130" rx="7" fill="%s"/>' % INK)
    o.append('<path d="M1180 470 l7 -22 l7 22 z" fill="%s"/>' % INK)
    return enveloppe("".join(o))


def p8():
    """Trois mètres. Rien entre eux, et rien autour."""
    r = random.Random(8)
    o = [trame(0, 0, L, 470, "t1", .38)]
    o.append('<rect x="0" y="470" width="1600" height="170" fill="url(#t2)" opacity=".35"/>')
    o.append('<line x1="0" y1="470" x2="1600" y2="470" stroke="%s" stroke-width="4"/>' % INK)
    for i in range(120):
        x = r.randint(0, 1600)
        y = r.randint(476, 636)
        o.append('<circle cx="%g" cy="%g" r="%g" fill="%s" opacity=".5"/>'
                 % (x, y, r.choice((1.5, 2, 2.6)), INK))
    o.append(silhouette(852, 470, 62, penche=.12))          # elle, plus grande
    o.append(silhouette(924, 470, 53, miroir=True))          # lui, dix centimetres de moins
    o.append('<line x1="856" y1="502" x2="920" y2="502" stroke="%s" stroke-width="1.6" '
             'opacity=".3"/>' % INK)
    o.append('<rect x="184" y="330" width="5" height="140" fill="%s" opacity=".85"/>' % INK)
    o.append('<line x1="164" y1="330" x2="210" y2="330" stroke="%s" stroke-width="4" '
             'opacity=".85"/>' % INK)
    return enveloppe("".join(o))


def p9():
    """La combe. Un épicéa mort, deux talons, et la lune en plein jour."""
    r = random.Random(9)
    o = [trame(0, 0, L, 400, "t1", .35)]
    o.append('<path d="M0 640 L0 120 L200 90 L330 300 L300 640 Z" fill="%s"/>' % INK)
    o.append('<path d="M300 640 L330 300 L520 396 L780 350 L1010 404 L1240 336 '
             'L1600 400 L1600 640 Z" fill="url(#t3)" opacity=".55"/>')
    o.append('<path d="M300 640 L330 300 L520 396 L780 350 L1010 404 L1240 336 '
             'L1600 400" stroke="%s" stroke-width="4" fill="none"/>' % INK)
    # l'épicéa mort
    o.append('<rect x="686" y="256" width="9" height="120" fill="%s"/>' % INK)
    for i in range(9):
        y = 268 + i * 12
        w = 8 + i * 4.6
        o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.6" '
                 'opacity="%g"/>' % (690 - w, y + 5, 690 + w, y - 3, INK, .85 - i * .05))
    # la lune, au-dessus du col
    o.append('<circle cx="1240" cy="150" r="66" fill="none" stroke="%s" stroke-width="4"/>' % INK)
    o.append('<path d="M1240 84 a66 66 0 0 1 0 132 z" fill="url(#t2)" opacity=".75"/>')
    # les deux talons
    o.append('<ellipse cx="820" cy="560" rx="26" ry="13" fill="%s"/>' % INK)
    o.append('<ellipse cx="892" cy="566" rx="26" ry="13" fill="%s"/>' % INK)
    for i in range(60):
        o.append('<circle cx="%g" cy="%g" r="%g" fill="%s" opacity=".4"/>'
                 % (r.randint(420, 1500), r.randint(470, 630),
                    r.choice((1.6, 2.2, 2.8)), INK))
    return enveloppe("".join(o))


def p10():
    """Une table pliante à trois mètres d'un bloc. Une chaise vide."""
    r = random.Random(10)
    o = [trame(0, 0, L, 430, "t1", .34)]
    o.append('<line x1="0" y1="430" x2="1600" y2="430" stroke="%s" stroke-width="4"/>' % INK)
    o.append('<rect x="0" y="430" width="1600" height="210" fill="url(#t2)" opacity=".3"/>')
    # la table
    o.append('<rect x="612" y="470" width="330" height="12" fill="%s"/>' % INK)
    o.append('<path d="M636 482 L604 596 M918 482 L950 596" stroke="%s" stroke-width="9"/>' % INK)
    # papiers + caillou
    o.append('<rect x="686" y="452" width="92" height="20" fill="%s"/>' % PAP)
    o.append('<rect x="686" y="452" width="92" height="20" fill="none" stroke="%s" '
             'stroke-width="2.5"/>' % INK)
    o.append('<ellipse cx="732" cy="452" rx="17" ry="11" fill="%s"/>' % INK)
    o.append('<rect x="880" y="456" width="46" height="16" rx="3" fill="%s"/>' % INK)
    # deux chaises, une vide
    for x in (566, 986):
        o.append('<path d="M%g 596 L%g 512 L%g 512 L%g 596 M%g 546 L%g 546" '
                 'stroke="%s" stroke-width="8" fill="none"/>'
                 % (x, x, x + 56, x + 56, x, x + 56, INK))
    # le bloc plat, à trois mètres
    o.append('<path d="M1176 596 L1196 546 L1330 546 L1348 596 Z" fill="%s"/>' % INK)
    o.append('<line x1="1010" y1="620" x2="1176" y2="620" stroke="%s" stroke-width="2" '
             'opacity=".6"/>' % INK)
    o.append('<rect x="228" y="250" width="5" height="180" fill="%s" opacity=".85"/>' % INK)
    o.append('<line x1="206" y1="250" x2="256" y2="250" stroke="%s" stroke-width="4" '
             'opacity=".85"/>' % INK)
    for i in range(70):
        o.append('<circle cx="%g" cy="%g" r="%g" fill="%s" opacity=".4"/>'
                 % (r.randint(0, 1600), r.randint(440, 636),
                    r.choice((1.5, 2.1, 2.7)), INK))
    return enveloppe("".join(o))


PLANCHES = {0: frontispice, 1: p1, 2: p2, 3: p3, 4: p4, 5: p5,
            6: p6, 7: p7, 8: p8, 9: p9, 10: p10}


def planche_interieure(n):
    """Planche du sommet du chapitre n : (index de scène, svg) ou None."""
    e = PLANCHES_INTERIEURES.get(n)
    return (e[0], e[1]()) if e else None


def planche(n):
    """Retourne le SVG de la planche n, ou None si elle n'existe pas."""
    f = PLANCHES.get(n)
    return f() if f else None


if __name__ == "__main__":
    from pathlib import Path
    d = Path(__file__).resolve().parent.parent / "docs" / "planches"
    d.mkdir(parents=True, exist_ok=True)
    tout = dict(PLANCHES)
    for n, (_, f) in PLANCHES_INTERIEURES.items():
        tout["%db" % n] = f
    for n, f in tout.items():
        (d / ("%s.svg" % (("%02d" % n) if isinstance(n, int) else n))).write_text(
            f().replace(INK, "#111").replace(PAP, "#fff"), encoding="utf-8")
    print("planches écrites dans %s" % d)
