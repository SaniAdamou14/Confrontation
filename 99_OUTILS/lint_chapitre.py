#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint_chapitre.py — mesure de style pour « Le Poids des dieux ».

Usage :
    python 99_OUTILS/lint_chapitre.py 04_CHAPITRES/T1/*.md
    python 99_OUTILS/lint_chapitre.py --extrait 04_CHAPITRES/T1/CH07_les-visites.md "chambranle" "escalier"

Ne juge pas la prose. Compte ce qui, mesuré sur les chapitres 1 à 7,
s'est révélé corrélé à la platitude : monotonie d'attaque, débit uniforme,
saturation de chiffres, glose de narrateur.

CONVENTIONS DE COMPTAGE — arrêtées explicitement, parce que le seuil en dépend.
  · « un / une » ne comptent pas : ce sont des articles avant d'être des nombres.
  · Les unités (heures, mètres, secondes…) ne comptent pas comme chiffres.
    La charge est portée par le numéral, pas par l'unité. Elles sont
    rapportées à part, pour information.
  · L'imparfait exclut « avait / était » en auxiliaire de plus-que-parfait :
    un PQP antériorise un événement, il ne fait pas durer une scène.
  · Narration = tout paragraphe qui ne commence pas par un tiret cadratin,
    un intertitre ou une balise Markdown.
"""

import io
import re
import sys
import glob
import unicodedata

# La console Windows est en cp1252 par défaut : on force l'UTF-8 en sortie.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- seuils

SEUILS = {
    # Calibrés sur le corpus, jamais posés au jugé.
    "serie_attaques": 2,             # R9 — max de paragraphes consécutifs ouverts par le même mot
    "familles_par_scene": 5,         # R8 — max de familles d'unités distinctes dans une scène
    "parce_que_narration": 3,        # R7 — outlier net : 3 à 6 sur six chapitres, 16 sur le septième
    "appositions_ce_qui": 0,         # R7
    "para_long_par_scene": 1,        # R9 — au moins un paragraphe > 60 mots par scène
    "mots_min": 5000,
    "mots_max": 8000,
}

# ABANDONNÉS APRÈS CALIBRAGE — ne pas réintroduire sans données.
#   · Plafond de densité de chiffres : le meilleur passage du tome (le chambranle)
#     est PLUS dense que le pire. La densité ne prédit rien. Ce qui compte est
#     l'unité d'échelle — d'où « familles_par_scene ».
#   · Pourcentage global d'attaques identiques : violé par 7 chapitres sur 7,
#     donc c'est le seuil qui était faux. Le lecteur sent une série consécutive,
#     pas une proportion — d'où « serie_attaques ».
#   · Ratio imparfait / passé composé : un ratio de temps n'est pas un signal de
#     qualité. Une scène d'action doit être au PC, une scène d'habitude à
#     l'imparfait. Mesuré en information, sans seuil.

NOMBRES = r"""(?:deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|
quatorze|quinze|seize|vingt|vingts|trente|quarante|cinquante|soixante|cent|cents|
mille|milliers|million|millions|milliard|milliards|demi|demie|premier|première|
deuxième|troisième|quatrième|cinquième|sixième|septième|huitième|neuvième|dixième|
onzième|douzième|centième|millième)"""

UNITES = r"""(?:secondes?|minutes?|heures?|jours?|semaines?|mois|années?|ans?|
millimètres?|centimètres?|mètres?|kilomètres?|grammes?|kilos?|tonnes?|
litres?|degrés?|dollars?|pages?|fois)"""

FAUX_AMIS_IMPARFAIT = {
    "fait", "faits", "jamais", "trait", "traits", "lait", "portrait", "extrait",
    "attrait", "souhait", "parfait", "imparfait", "retrait", "abstrait", "mais",
    "vrais", "frais", "français", "balais", "palais", "relais", "délais", "essais",
}


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


# Un intertitre est un paragraphe d'une seule ligne, en italique ou en citation,
# portant une heure ou une date : *16 h 36.* · *Maison des Grayson. Jour 7, 06 h 40.*
# Il ne faut PAS confondre avec le dialogue en italique du ch. 5, qui commence par un tiret.
INTERTITRE = r"^(?:\*(?!\s*[—–])[^*\n]*\*|>[^\n]*)$"


def est_intertitre(p):
    return bool(re.match(INTERTITRE, p)) and bool(re.search(r"\d", p))


def est_narratif(p):
    return not p.startswith(("—", "–", "*", "**", ">", "#", "|", "-", "["))


def decouper(texte):
    """Renvoie (paragraphes, narratifs, scenes) — scenes = liste de listes."""
    corps = texte
    # On retire l'en-tête, c'est-à-dire tout ce qui précède le PREMIER « --- ».
    # (Un maxsplit=2 jetterait la première scène avec l'en-tête.)
    if re.search(r"^---\s*$", texte, re.M):
        parts = re.split(r"^---\s*$", texte, maxsplit=1, flags=re.M)
        corps = parts[-1] if len(parts) > 1 else texte
    paras = [p.strip() for p in re.split(r"\n\s*\n", corps) if p.strip()]
    scenes, courante = [], []
    for p in paras:
        if est_intertitre(p):
            if courante:
                scenes.append(courante)
            courante = []
        elif est_narratif(p):
            courante.append(p)
    if courante:
        scenes.append(courante)
    if not scenes:
        scenes = [[p for p in paras if est_narratif(p)]]
    narr = [p for s in scenes for p in s]
    return paras, narr, scenes


def premier_mot(p):
    return p.split()[0].strip("«»\"'—,.")


def plus_longue_serie(scenes):
    """Plus longue suite de paragraphes consécutifs ouverts par le même mot."""
    pire, ou = 1, ""
    for i, sc in enumerate(scenes, 1):
        courant, n = None, 0
        for p in sc:
            m = premier_mot(p)
            if m == courant:
                n += 1
            else:
                courant, n = m, 1
            if n > pire:
                pire, ou = n, f"« {m} », scène {i}"
    return pire, ou


def familles_unites(txt):
    """Familles d'unités qui MESURENT. Les horodatages sont neutralisés d'abord.

    « à sept heures dix » date une scène ; « sept heures de route » est une échelle.
    Les compter ensemble faisait dominer « heure » dans les sept chapitres et rendait
    le chiffre muet. Le seuil de R8 a été recalculé sur la référence après ce correctif.
    """
    txt = re.sub(r"\b(?:à|vers|jusqu'à|depuis|avant|après|entre)\s+"
                 r"(?:[\wÀ-ÿ]+[-\s]){0,3}heures?(?:\s+(?:et\s+)?[\wÀ-ÿ]+)?",
                 " ", txt, flags=re.I)
    txt = re.sub(r"\b\d{1,2}\s*h\s*\d{0,2}\b", " ", txt)
    RACINES = ["seconde", "minute", "heure", "jour", "semaine", "mois", "année",
               "an", "millimètre", "centimètre", "mètre", "kilomètre", "gramme",
               "kilo", "tonne", "litre", "degré", "dollar", "page", "fois",
               "marche", "pièce", "taille", "étage", "nœud", "pouce"]
    trouvees = set()
    for mot in re.findall(rf"\b{UNITES}\b", txt, re.I | re.X):
        for r in RACINES:
            if mot.lower().startswith(r):
                trouvees.add(r)
                break
    return trouvees


def compter_imparfaits(txt):
    """Imparfaits nets : on retire les auxiliaires de plus-que-parfait."""
    formes = re.findall(r"\b\w+(?:ait|aient|ais)\b", txt, re.I)
    formes = [f for f in formes if strip_accents(f.lower()) not in FAUX_AMIS_IMPARFAIT]
    pqp = len(re.findall(
        r"\b(?:avait|avaient|était|étaient|étais|avais)\s+(?:\w+\s+){0,2}?"
        r"\w+(?:é|ée|és|ées|i|ie|is|it|u|ue|us|ues|ert|erte|int|eint|is|mis|pris)\b",
        txt, re.I))
    return len(formes), pqp, max(0, len(formes) - pqp)


def analyser(chemin, texte=None, etiquette=None):
    if texte is None:
        texte = open(chemin, encoding="utf-8").read()
    paras, narr, scenes = decouper(texte)
    txt = " ".join(narr)
    mots = re.findall(r"[A-Za-zÀ-ÿ']+", txt)
    mots_total = len(re.findall(r"[A-Za-zÀ-ÿ']+", texte))
    if not mots:
        print(f"  {chemin} : aucun paragraphe narratif détecté.")
        return

    phrases = [s for s in re.split(r"[.!?…]+", txt) if len(s.split()) > 1]
    longueurs = sorted(len(s.split()) for s in phrases)
    med = longueurs[len(longueurs) // 2]

    serie, ou_serie = plus_longue_serie(scenes)
    fam_par_scene = [len(familles_unites(" ".join(sc))) for sc in scenes]
    pire_scene = max(fam_par_scene) if fam_par_scene else 0
    idx_pire = fam_par_scene.index(pire_scene) + 1 if fam_par_scene else 0

    chiffres = re.findall(rf"\b{NOMBRES}\b|(?<![\w-])\d+", txt, re.I | re.X)
    dens = len(mots) // len(chiffres) if chiffres else 999

    pq = len(re.findall(r"\bparce qu", txt, re.I))
    # Apposition = « , ce qui + verbe » qui commente la proposition précédente.
    # « , ce que X avait dit » est une relative objet parfaitement légitime : on ne la compte pas.
    appo = len(re.findall(r",\s*ce qui\b|,\s*ce que\s+(?:font|fait|feraient|ne font)\b", txt, re.I))
    longs = sum(1 for p in narr if len(p.split()) > 60)
    imp_brut, pqp, imp_net = compter_imparfaits(txt)
    pc = len(re.findall(r"\b(?:a|ont|est|sont)\s+(?:\w+\s+){0,2}?"
                        r"\w+(?:é|ée|és|ées|i|ie|is|it|u|ue|us|ues|ert|int|eint)\b", txt))
    ns = len(scenes)

    nom = etiquette or chemin.split("/")[-1].split("\\")[-1]
    print(f"\n  ── {nom}")
    print(f"     mots (fichier)          {mots_total}"
          + ("" if SEUILS['mots_min'] <= mots_total <= SEUILS['mots_max'] else "   ⚠ hors 5 000-8 000"))
    print(f"     mots narratifs          {len(mots)}   ({len(narr)} paragraphes, {ns} scènes)")
    print(f"     phrase : moy / médiane  {len(mots)/len(phrases):.1f} / {med}")
    print(f"  R9 série d'attaques        {serie} d'affilée   {ou_serie}"
          + (f"   ⚠ R9 (max {SEUILS['serie_attaques']})" if serie > SEUILS["serie_attaques"] else ""))
    print(f"  R9 paragraphes > 60 mots   {longs}  (≥ {ns} attendu)"
          + ("   ⚠ R9" if longs < ns else ""))
    print(f"  R8 familles d'unités       {pire_scene} max (scène {idx_pire})   toutes scènes : {fam_par_scene}"
          + (f"   → signal R8 (réf. {SEUILS['familles_par_scene']}) : chercher la porteuse"
             if pire_scene > SEUILS["familles_par_scene"] else ""))
    # LIMITE CONNUE DU COMPTEUR : il confond l'unité qui MESURE et l'unité qui DATE.
    # « sept heures de route » et « sept heures dix » tombent tous deux dans la famille
    # « heure », alors que le second est un repère de scène, pas une échelle concurrente.
    # C'est pourquoi « heure » domine partout. À séparer dans une prochaine version.
    print(f"  R7 « parce que »           {pq}"
          + (f"   ⚠ R7 (max {SEUILS['parce_que_narration']})" if pq > SEUILS["parce_que_narration"] else ""))
    print(f"  R7 « , ce qui / ce que »   {appo}"
          + ("   ⚠ R7 (zéro toléré)" if appo > SEUILS["appositions_ce_qui"] else ""))
    print(f"     info — chiffres         {len(chiffres)}, soit 1 tous les {dens} mots"
          + "   (sans seuil : la densité ne prédit pas la qualité)")
    print(f"     info — imparfait / PC   {imp_net} / {pc}   (PQP retirés : {pqp} ; sans seuil)")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--extrait":
        chemin, debut, fin = args[1], args[2], args[3]
        texte = open(chemin, encoding="utf-8").read()
        i, j = texte.find(debut), texte.find(fin)
        if i < 0 or j < 0:
            sys.exit("Bornes introuvables.")
        analyser(chemin, texte[i:j], etiquette=f"EXTRAIT « {debut} → {fin} »")
        return

    fichiers = []
    for a in args or ["04_CHAPITRES/T1/CH*.md"]:
        fichiers.extend(sorted(glob.glob(a)))
    if not fichiers:
        sys.exit("Aucun fichier.")
    print("LINT — Le Poids des dieux")
    print("  conventions : « un/une » et les unités ne comptent pas comme chiffres ;")
    print("  l'imparfait exclut les auxiliaires de plus-que-parfait.")
    for f in fichiers:
        analyser(f)
    print()


if __name__ == "__main__":
    main()
