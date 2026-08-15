#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traitement des tirets cadratins du manuscrit.

    python 99_OUTILS/tirets.py                  rapport seul, rien n'est écrit
    python 99_OUTILS/tirets.py --appliquer      remplace les incises par des virgules
    python 99_OUTILS/tirets.py --dialogue       ⚠ convertit AUSSI les ouvertures de réplique

DEUX USAGES DU TIRET CADRATIN, À NE JAMAIS CONFONDRE :

  1. EN TÊTE DE LIGNE — c'est l'ouverture de réplique. C'est la typographie
     française du dialogue, elle est imposée par LEXIQUE_ET_ORTHOGRAPHES.md §2,
     et un trait d'union à la place est une faute. Ce script n'y touche pas,
     sauf --dialogue, qui existe pour les cas où l'on exporte vers un support
     qui ne sait pas rendre le cadratin.

  2. AU MILIEU D'UNE PHRASE — c'est l'incise. En français elle se rend très bien
     par une paire de virgules, et le tiret y est un tic. C'est la cible.
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CIBLES = ["04_CHAPITRES/T1/CH*.md"]

CADRATIN = "—"   # —
DEMI = "–"       # –


def traiter_ligne(l, dialogue=False):
    """Retourne (ligne, n_incises, n_dialogue)."""
    n_inc = n_dial = 0
    nu = l.lstrip()
    marge = l[:len(l) - len(nu)]

    ouverture = ""
    if nu.startswith(CADRATIN) or nu.startswith(DEMI):
        ouverture, nu = nu[0], nu[1:]
        n_dial = 1

    # incise encadrée : « x — y — z »  ->  « x, y, z »
    nu, k = re.subn(r"\s+[%s%s]\s+(.+?)\s+[%s%s]\s+" % (CADRATIN, DEMI, CADRATIN, DEMI),
                    r", \1, ", nu)
    n_inc += k * 2

    # incise ouvrante seule : « x — y »  ->  « x, y »
    nu, k = re.subn(r"\s+[%s%s]\s+" % (CADRATIN, DEMI), ", ", nu)
    n_inc += k

    # tiret suivi d'une ponctuation : « x —, » -> « x, »   « x —. » -> « x. »
    # (cas fréquent quand la seconde borne d'une incise porte déjà une virgule ;
    #  sans cette règle le script laisse un tiret orphelin.)
    nu, k = re.subn(r"\s*[%s%s](\s*[,.;:!?…»])" % (CADRATIN, DEMI), r"\1", nu)
    n_inc += k

    # reste isolé en fin de ligne (réplique coupée : « Monsieur, ce n'est pas — »)
    # -> conservé tel quel, c'est un effet voulu.

    if ouverture:
        ouverture = "- " if dialogue else ouverture
        if dialogue:
            nu = nu.lstrip()
        else:
            n_dial = 0

    return marge + ouverture + nu, n_inc, n_dial


def main():
    appliquer = "--appliquer" in sys.argv
    dialogue = "--dialogue" in sys.argv
    if dialogue and not appliquer:
        appliquer = True

    fichiers = []
    for motif in CIBLES:
        fichiers += sorted(RACINE.glob(motif))

    tot_inc = tot_dial = 0
    exemples = []

    for f in fichiers:
        texte = f.read_text(encoding="utf-8")
        lignes = texte.split("\n")
        sorties, n_inc, n_dial, bloc = [], 0, 0, False

        for l in lignes:
            if l.strip().startswith("```"):
                bloc = not bloc
                sorties.append(l)
                continue
            # on ne touche ni aux blocs de code, ni aux titres, ni aux métadonnées
            if bloc or l.startswith("#") or l.startswith(">"):
                sorties.append(l)
                continue

            nouv, a, b = traiter_ligne(l, dialogue)
            if a and len(exemples) < 8 and l.strip():
                exemples.append((f.name, l.strip()[:96], nouv.strip()[:96]))
            n_inc += a
            n_dial += b
            sorties.append(nouv)

        tot_inc += n_inc
        tot_dial += n_dial
        etat = "%-40s incises %3d" % (f.name, n_inc)
        if dialogue:
            etat += "   dialogues %4d" % n_dial
        print(etat)

        if appliquer and (n_inc or n_dial):
            f.write_text("\n".join(sorties), encoding="utf-8")

    print("-" * 72)
    print("Incises traitées : %d" % tot_inc)
    if dialogue:
        print("Ouvertures de réplique converties : %d   ⚠ typographie non standard" % tot_dial)

    if exemples:
        print("\nAvant / après :")
        for nom, av, ap in exemples:
            print("\n  %s" % nom)
            print("  av.  %s" % av)
            print("  ap.  %s" % ap)

    if not appliquer:
        print("\n(Rapport seul. Relancer avec --appliquer pour écrire.)")


if __name__ == "__main__":
    main()
