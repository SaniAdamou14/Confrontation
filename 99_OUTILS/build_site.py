#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site de lecture — Le Poids des dieux.

    python 99_OUTILS/build_site.py              site statique dans site/
    python 99_OUTILS/build_site.py --artifact   + un fichier unique autonome

Le site statique est prêt pour GitHub Pages : chemins relatifs, .nojekyll,
sitemap, carte sociale. Une URL par chapitre.

Avant la première mise en ligne, régler BASE_URL ci-dessous.
"""

import base64
import html
import json
import re
import shutil
import sys
import unicodedata
from datetime import date
from pathlib import Path

import planches

sys.path.insert(0, str(Path(__file__).resolve().parent))
RACINE = Path(__file__).resolve().parent.parent
CHAPITRES = RACINE / "04_CHAPITRES" / "T1"
SORTIE = RACINE / "docs"

BASE_URL = "https://saniadamou14.github.io/Confrontation"
# Adresse de contact affichee sur le site. A changer si besoin.
EMAIL = "saniadamou778@gmail.com"

TITRE = "Le Poids des dieux"
SOUS_TITRE = "Dragon Ball Z × Invincible"
TOME = "Tome 1 — « Vingt-deux minutes »"
CHAPITRES_PREVUS = 20
DESCRIPTION = ("Light novel. Le ciel s'ouvre au-dessus de Chicago à 16 h 47. "
               "Vingt-deux minutes plus tard, il n'y a plus de ville.")

# ---------------------------------------------------------------- emblèmes

E = {}
E[1] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<rect x="46" y="12" width="28" height="66" rx="4"/><line x1="60" y1="0" x2="60" y2="12"/>
<circle cx="60" cy="28" r="6" fill="currentColor" stroke="none" opacity=".9"/>
<circle cx="60" cy="45" r="6" opacity=".35"/><circle cx="60" cy="62" r="6" opacity=".35"/>
<g opacity=".55"><line x1="20" y1="96" x2="20" y2="108"/><line x1="33" y1="96" x2="33" y2="108"/>
<line x1="46" y1="96" x2="46" y2="108"/><line x1="59" y1="96" x2="59" y2="108"/>
<line x1="72" y1="96" x2="72" y2="108"/><line x1="85" y1="96" x2="85" y2="108"/></g>
<line x1="98" y1="92" x2="98" y2="112" stroke-width="2.5"/></svg>"""
E[2] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<circle cx="60" cy="60" r="42"/><circle cx="60" cy="60" r="27" opacity=".5"/>
<line x1="60" y1="8" x2="60" y2="26"/><line x1="60" y1="94" x2="60" y2="112"/>
<line x1="8" y1="60" x2="26" y2="60"/><line x1="94" y1="60" x2="112" y2="60"/>
<path d="M30 30 L44 30 M30 30 L30 44 M90 30 L76 30 M90 30 L90 44" opacity=".7"/>
<path d="M30 90 L44 90 M30 90 L30 76 M90 90 L76 90 M90 90 L90 76" opacity=".7"/>
<circle cx="60" cy="60" r="3" fill="currentColor" stroke="none"/></svg>"""
E[3] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<line x1="24" y1="60" x2="96" y2="60" stroke-width="2"/>
<g opacity=".8"><line x1="34" y1="34" x2="52" y2="34"/><line x1="58" y1="34" x2="86" y2="34"/>
<line x1="34" y1="44" x2="72" y2="44"/></g>
<g opacity=".8"><line x1="48" y1="76" x2="72" y2="76"/></g>
<ellipse cx="60" cy="94" rx="26" ry="9" opacity=".55"/><ellipse cx="60" cy="94" rx="16" ry="5" opacity=".3"/></svg>"""
E[4] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<g opacity=".65"><line x1="14" y1="46" x2="14" y2="74"/><line x1="27" y1="46" x2="27" y2="74"/>
<line x1="40" y1="46" x2="40" y2="74"/><line x1="53" y1="46" x2="53" y2="74"/>
<line x1="66" y1="46" x2="66" y2="74"/></g>
<line x1="79" y1="38" x2="79" y2="82" stroke-width="2.5"/>
<g opacity=".65"><line x1="92" y1="46" x2="92" y2="74"/><line x1="105" y1="46" x2="105" y2="74"/></g>
<line x1="8" y1="98" x2="112" y2="98" opacity=".4"/></svg>"""
E[5] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">
<g opacity=".7">
<line x1="22" y1="30" x2="52" y2="30"/><line x1="68" y1="30" x2="98" y2="30"/>
<line x1="22" y1="46" x2="52" y2="46"/><line x1="68" y1="46" x2="98" y2="46"/>
<line x1="22" y1="62" x2="52" y2="62"/><line x1="68" y1="62" x2="98" y2="62"/>
<line x1="22" y1="78" x2="52" y2="78"/></g>
<g><line x1="68" y1="78" x2="98" y2="78" opacity=".25"/><line x1="66" y1="78" x2="100" y2="78" stroke-width="2"/></g>
<line x1="22" y1="98" x2="52" y2="98" stroke-width="2"/><circle cx="60" cy="98" r="2.5" fill="currentColor" stroke="none"/></svg>"""
E[6] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<rect x="26" y="18" width="68" height="84" rx="3" opacity=".55"/>
<line x1="38" y1="40" x2="82" y2="40"/><line x1="38" y1="54" x2="82" y2="54"/>
<line x1="38" y1="68" x2="82" y2="68"/><line x1="38" y1="74" x2="82" y2="74" stroke-width="2.5"/>
<path d="M62 88 q10 6 20 0" opacity=".6"/></svg>"""
E[7] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<line x1="42" y1="6" x2="42" y2="114" stroke-width="2"/>
<g opacity=".75"><line x1="42" y1="94" x2="66" y2="94"/><line x1="42" y1="80" x2="64" y2="80"/>
<line x1="42" y1="66" x2="68" y2="66"/><line x1="42" y1="52" x2="65" y2="52"/>
<line x1="42" y1="38" x2="70" y2="38"/></g>
<line x1="42" y1="24" x2="78" y2="24" stroke-width="2.5"/>
<g opacity=".45"><line x1="42" y1="72" x2="58" y2="72"/><line x1="42" y1="60" x2="58" y2="60"/></g></svg>"""
E[8] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<line x1="34" y1="52" x2="34" y2="88"/><circle cx="34" cy="42" r="8"/>
<line x1="86" y1="56" x2="86" y2="88"/><circle cx="86" cy="46" r="7"/>
<line x1="46" y1="98" x2="74" y2="98" opacity=".7"/>
<line x1="46" y1="94" x2="46" y2="102" opacity=".7"/><line x1="74" y1="94" x2="74" y2="102" opacity=".7"/>
<line x1="8" y1="110" x2="112" y2="110" opacity=".35"/></svg>"""
E[9] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<circle cx="60" cy="42" r="26"/><path d="M60 16 a26 26 0 0 1 0 52 z" fill="currentColor" stroke="none" opacity=".85"/>
<ellipse cx="44" cy="98" rx="7" ry="4" fill="currentColor" stroke="none" opacity=".8"/>
<ellipse cx="72" cy="98" rx="7" ry="4" fill="currentColor" stroke="none" opacity=".8"/>
<line x1="14" y1="110" x2="106" y2="110" opacity=".3"/></svg>"""
E[10] = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<rect x="22" y="22" width="76" height="76" rx="3" opacity=".55"/>
<line x1="34" y1="42" x2="60" y2="42" opacity=".8"/><line x1="68" y1="42" x2="86" y2="42" opacity=".35"/>
<line x1="34" y1="58" x2="56" y2="58" opacity=".8"/><line x1="64" y1="58" x2="86" y2="58" opacity=".35"/>
<line x1="34" y1="74" x2="86" y2="74" opacity=".35"/>
<rect x="60" y="66" width="26" height="16" opacity=".9"/></svg>"""
EMB_DEFAUT = """<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<rect x="30" y="30" width="60" height="60" rx="3" opacity=".5"/></svg>"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="10" fill="#0E1418"/>
<circle cx="32" cy="28" r="14" fill="none" stroke="#E0682C" stroke-width="2.5"/>
<path d="M32 14 a14 14 0 0 1 0 28 z" fill="#E0682C"/>
<rect x="18" y="50" width="28" height="2.5" fill="#7C8A96"/></svg>"""

# ---------------------------------------------------------------- parsing

def ardoise(t):
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^\w\s-]", "", t.lower())
    return re.sub(r"[\s_]+", "-", t).strip("-")


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
    return t


def lire(chemin):
    brut = chemin.read_text(encoding="utf-8")
    lignes = brut.split("\n")
    numero, titre, focal, situation, i = 0, "", "", "", 0
    while i < len(lignes):
        l = lignes[i].strip()
        m = re.match(r"^#\s+Chapitre\s+(\d+)\s+[—-]\s+(.+)$", l)
        if m:
            numero, titre = int(m.group(1)), m.group(2).strip()
        elif l.startswith("> Focalisation"):
            focal = l.split(":", 1)[1].strip()
        elif l.startswith("> Jour"):
            situation = l[1:].strip()
        elif l == "---" and numero:
            i += 1
            break
        i += 1

    # Un intertitre suit toujours une rupture. Sans cette condition, toute
    # ligne en italique passe pour une scène — et au chapitre 5 la langue
    # saiyenne est en italique, ce qui y faisait détecter 36 scènes pour 6.
    corps, bloc, tampon, apres_rupture = [], False, [], True
    for l in lignes[i:]:
        s = l.strip()
        if s.startswith("```"):
            if bloc:
                corps.append(("document", "\n".join(tampon)))
                tampon, bloc = [], False
            else:
                bloc = True
            continue
        if bloc:
            tampon.append(l)
            continue
        if not s:
            continue
        if s == "---":
            corps.append(("rupture", ""))
            apres_rupture = True
            continue
        if apres_rupture and re.fullmatch(r"\*[^*].*[^*]\*", s) and len(s) < 120:
            corps.append(("situation", s[1:-1]))
        elif apres_rupture and re.match(r"^>\s*(Jour|Focalisation)", s):
            corps.append(("situation", s.lstrip("> ").strip()))
        elif s.startswith("> "):
            corps.append(("note", s[2:].strip()))
        elif s.startswith("—") or s.startswith("–"):
            corps.append(("replique", s))
        else:
            corps.append(("texte", s))
        apres_rupture = False

    mots = len(re.findall(r"\S+", brut))
    amorce = next((t for g, t in corps if g == "texte"), "")
    amorce = re.sub(r"[*_]", "", amorce)
    if len(amorce) > 155:
        amorce = amorce[:152].rsplit(" ", 1)[0] + "…"

    return {"numero": numero, "titre": titre, "focal": focal, "situation": situation,
            "corps": corps, "mots": mots, "lecture": max(1, round(mots / 200)),
            "amorce": amorce, "fichier": "%02d-%s.html" % (numero, ardoise(titre)),
            "embleme": E.get(numero, EMB_DEFAUT)}


def rendre(corps, interieure=None):
    """interieure = (fragment_d_intertitre, svg).

    La planche s'ancre sur le TEXTE de l'intertitre, jamais sur son rang :
    un rang se decale des qu'on retouche le chapitre, et la planche part
    silencieusement dans la mauvaise scene."""
    restantes = list(interieure or [])
    out = []
    for genre, t in corps:
        if genre == "situation" and restantes:
            for k, (ancre, svg) in enumerate(restantes):
                if ancre.lower() in t.lower():
                    out.append('<div class="planche planche-interieure">%s</div>' % svg)
                    restantes.pop(k)
                    break
        if genre == "rupture":
            out.append('<div class="rupture" aria-hidden="true">◆</div>')
        elif genre == "situation":
            out.append('<p class="situation">%s</p>' % html.escape(t, quote=False))
        elif genre == "note":
            out.append('<aside class="note">%s</aside>' % inline(t))
        elif genre == "replique":
            out.append('<p class="replique">%s</p>' % inline(t))
        elif genre == "document":
            out.append('<div class="doc-enveloppe"><pre class="document">%s</pre></div>'
                       % html.escape(t, quote=False))
        else:
            out.append("<p>%s</p>" % inline(t))
    return "\n".join(out)


# ---------------------------------------------------------------- styles

CSS = r"""
*,*::before,*::after{box-sizing:border-box}

:root{
  --ground:#0E1418; --raised:#141C22; --line:#243039;
  --text:#DCE3E7; --dim:#8D9BA6; --faint:#5E6C77;
  --accent:#E0682C; --signal:#3FA96A; --amber:#D9A02B; --stop:#C1443B;
  --halo:rgba(224,104,44,.16);
  --pl-ink:#DCE3E7; --pl-paper:#0E1418;
  --shadow:0 1px 0 rgba(255,255,255,.03), 0 18px 44px -28px rgba(0,0,0,.9);
  --mesure:34rem;
  --pas:clamp(1.1rem,4vw,2.6rem);
}
@media (prefers-color-scheme:light){
  :root:not([data-theme="dark"]){
    --ground:#E9ECEE; --raised:#F6F7F8; --line:#D2D8DC;
    --text:#182027; --dim:#5A6771; --faint:#8794A0;
    --accent:#B4491A; --signal:#2E8654; --amber:#B07C12; --stop:#A83A31;
    --halo:rgba(180,73,26,.12);
    --pl-ink:#141C22; --pl-paper:#E9ECEE;
    --shadow:0 1px 0 rgba(255,255,255,.7), 0 16px 40px -30px rgba(20,32,40,.45);
  }
}
:root[data-theme="light"]{
  --ground:#E9ECEE; --raised:#F6F7F8; --line:#D2D8DC;
  --text:#182027; --dim:#5A6771; --faint:#8794A0;
  --accent:#B4491A; --signal:#2E8654; --amber:#B07C12; --stop:#A83A31;
  --halo:rgba(180,73,26,.12);
  --pl-ink:#141C22; --pl-paper:#E9ECEE;
  --shadow:0 1px 0 rgba(255,255,255,.7), 0 16px 40px -30px rgba(20,32,40,.45);
}

/* Encre. Le noir et blanc d'impression : aucune couleur, aucune ombre,
   et les planches passent en noir pur sur papier pur. */
:root[data-theme="encre"]{
  --ground:#FFFFFF; --raised:#FFFFFF; --line:#000000;
  --text:#000000; --dim:#000000; --faint:#000000;
  --accent:#000000; --signal:#000000; --amber:#8A8A8A; --stop:#FFFFFF;
  --halo:rgba(0,0,0,.08);
  --pl-ink:#000000; --pl-paper:#FFFFFF;
  --shadow:none;
}
:root[data-theme="encre"] .compteur dd,
:root[data-theme="encre"] .carte h3{font-weight:600}
:root[data-theme="encre"] .prose .situation{font-weight:600}

html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{
  margin:0;background:var(--ground);color:var(--text);
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
  font-size:clamp(16px,.95rem + .25vw,18px);line-height:1.7;overflow-x:hidden;
  text-rendering:optimizeLegibility;
}
.mono{font-family:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,"Liberation Mono",monospace}
a{color:inherit}
img,svg{max-width:100%}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

.evite{position:absolute;left:-9999px;top:0;background:var(--raised);color:var(--text);
  padding:.8rem 1.2rem;border:1px solid var(--accent);z-index:99}
.evite:focus{left:.6rem;top:.6rem}

.enveloppe{max-width:72rem;margin:0 auto;padding:0 var(--pas)}
.colonne{max-width:var(--mesure);margin:0 auto}

/* ---------------- barre ---------------- */
.barre{position:sticky;top:0;z-index:40;background:color-mix(in srgb,var(--ground) 88%,transparent);
  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.barre-i{display:flex;align-items:center;gap:1rem;min-height:3.4rem}
.marque{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--dim);
  text-decoration:none;padding:.7rem 0;transition:color .16s}
.marque:hover{color:var(--text)}
.theme{background:none;border:1px solid var(--line);color:var(--dim);font:inherit;
  font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;padding:.42rem .6rem;
  cursor:pointer;flex:none;min-width:4.4rem;transition:color .16s,border-color .16s}
.theme:hover{color:var(--accent);border-color:var(--accent)}
.barre-titre{flex:1;min-width:0;font-size:.74rem;color:var(--faint);white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis;text-align:right}
.lampe{width:9px;height:9px;border-radius:50%;flex:none;background:var(--signal);
  box-shadow:0 0 0 1px var(--line),0 0 0 3px color-mix(in srgb,var(--signal) 18%,transparent);
  animation:cycle 64s steps(1,end) infinite}
@keyframes cycle{
  0%,43.74%{background:var(--signal);box-shadow:0 0 0 1px var(--line),0 0 0 3px color-mix(in srgb,var(--signal) 18%,transparent)}
  43.75%,49.99%{background:var(--amber);box-shadow:0 0 0 1px var(--line),0 0 0 3px color-mix(in srgb,var(--amber) 18%,transparent)}
  50%,100%{background:var(--stop);box-shadow:0 0 0 1px var(--line),0 0 0 3px color-mix(in srgb,var(--stop) 18%,transparent)}}
@media (prefers-reduced-motion:reduce){.lampe{animation:none}}
.jauge{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--accent);
  transition:width .1s linear;will-change:width}

/* ---------------- accueil ---------------- */
.masthead{padding:clamp(2.6rem,9vw,6rem) 0 clamp(2rem,5vw,3.4rem);border-bottom:1px solid var(--line)}
.eyebrow{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin:0 0 1.4rem}
h1{font-size:clamp(2.6rem,10vw,5.6rem);line-height:.95;margin:0;font-weight:400;
  letter-spacing:-.022em;text-wrap:balance}
.tome{font-size:clamp(.95rem,2.6vw,1.2rem);color:var(--dim);margin:1.2rem 0 0;font-style:italic}
.pitch{max-width:34rem;margin:2.4rem 0 0;font-size:1.1rem}
.pitch strong{color:var(--accent);font-weight:400}
.these{max-width:34rem;margin:1.8rem 0 0;padding-left:1.1rem;border-left:2px solid var(--accent);
  color:var(--dim);font-style:italic}
.compteurs{display:grid;grid-template-columns:repeat(auto-fit,minmax(7.5rem,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);margin:2.8rem 0 0}
.compteur{background:var(--ground);padding:1rem 1.1rem}
.compteur dt{font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:0}
.compteur dd{margin:.4rem 0 0;font-size:clamp(1.15rem,3.4vw,1.5rem);
  font-variant-numeric:tabular-nums;letter-spacing:-.01em}

.section-titre{display:flex;align-items:baseline;gap:1rem;margin:clamp(2.6rem,7vw,4.5rem) 0 1.6rem}
.section-titre h2{font-size:1.05rem;font-weight:400;margin:0}
.section-titre .fil{flex:1;height:1px;background:var(--line)}
.section-titre .compte{font-size:.7rem;color:var(--faint);letter-spacing:.1em;white-space:nowrap}

.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line)}
.carte{background:var(--ground);padding:1.4rem 1.5rem 1.5rem;text-decoration:none;color:inherit;
  display:flex;gap:1.2rem;align-items:flex-start;transition:background .16s}
.carte:hover,.carte:focus-visible{background:var(--raised)}
.carte .num{font-size:2rem;line-height:1;color:var(--faint);font-variant-numeric:tabular-nums;
  flex:none;width:2.1rem;transition:color .16s}
.carte:hover .num{color:var(--accent)}
.carte .corps{min-width:0;flex:1}
.carte h3{margin:.1rem 0 .5rem;font-size:1.2rem;font-weight:400;line-height:1.25;text-wrap:balance}
.carte .meta{font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--faint);
  display:flex;flex-wrap:wrap;gap:.3rem .9rem}
.carte .focal{color:var(--dim)}
.carte .embleme{width:2.5rem;height:2.5rem;flex:none;color:var(--faint);opacity:.85;
  margin-top:.15rem;transition:color .16s}
.carte:hover .embleme{color:var(--accent)}
.carte .embleme svg{width:100%;height:100%;display:block}

.avenir{margin:2.2rem 0 0;padding:1.2rem 1.4rem;border:1px dashed var(--line);
  color:var(--dim);font-size:.92rem}
.avenir .mono{color:var(--faint);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;
  display:block;margin-bottom:.5rem}
a.avenir{display:block;text-decoration:none;border-style:solid;transition:border-color .16s,color .16s}
a.avenir:hover{border-color:var(--accent);color:var(--text)}
a.avenir .rep-titre{color:var(--accent);font-style:italic}

.pied{margin:clamp(3rem,8vw,6rem) 0 0;padding:2rem 0 3.5rem;border-top:1px solid var(--line);
  color:var(--faint);font-size:.78rem;display:flex;flex-wrap:wrap;gap:.6rem 1.6rem}
.pied a{color:var(--dim)}

/* ---------------- chapitre ---------------- */
.chap-tete{padding:clamp(2.4rem,8vw,5rem) 0 0;text-align:center}
.chap-tete .embleme{width:clamp(3.4rem,10vw,4.4rem);height:clamp(3.4rem,10vw,4.4rem);
  margin:0 auto 1.6rem;color:var(--accent);opacity:.9}
.chap-tete .embleme svg{width:100%;height:100%;display:block}
.chap-tete .num{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--faint);margin:0 0 .9rem}
.chap-tete h1{font-size:clamp(1.9rem,6.5vw,2.9rem);line-height:1.1;letter-spacing:-.015em}
.chap-tete .sit{margin:1.5rem 0 0;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;
  color:var(--dim);line-height:1.9}
.chap-tete .filet{width:2.2rem;height:1px;background:var(--accent);margin:2.4rem auto 0}

.prose{padding:2.6rem 0 0;font-size:1.06rem;line-height:1.82;hyphens:auto}
.prose p{margin:0 0 1.35em}
.prose .situation{font-family:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,monospace;
  font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);
  margin:2.6em 0 1.6em;padding-bottom:.7em;border-bottom:1px solid var(--line);hyphens:none}
.prose .replique{margin:0 0 1.1em}
.prose .note{border-left:2px solid var(--line);padding-left:1.1rem;color:var(--dim);
  font-size:.97rem;margin:0 0 1.35em;display:block}
.prose .rupture{margin:2.6em 0;text-align:center;color:var(--faint);
  font-size:.62rem;letter-spacing:.6em;line-height:1}
.doc-enveloppe{overflow-x:auto;margin:2.4em 0;background:var(--raised);
  border:1px solid var(--line);box-shadow:var(--shadow)}
.prose .document{font-family:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,monospace;
  font-size:.76rem;line-height:1.65;white-space:pre;margin:0;padding:1.4rem 1.5rem;color:var(--text)}
.prose strong{font-weight:600}

.chap-pied{padding:3rem 0 4.5rem}
.nav-chap{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}
.nav-chap a,.nav-chap span{background:var(--ground);padding:1.15rem 1.3rem;text-decoration:none;
  color:var(--text);display:block;min-height:4.2rem;transition:background .16s}
.nav-chap a:hover{background:var(--raised)}
.nav-chap span{color:var(--faint)}
.nav-chap .sens{display:block;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--faint);margin-bottom:.4rem;padding:0;background:none;min-height:0}
.nav-chap .suiv{text-align:right}
.retour{display:block;margin-top:1px;background:var(--ground);border:1px solid var(--line);
  padding:1rem;text-align:center;color:var(--dim);font-size:.76rem;letter-spacing:.08em;
  text-transform:uppercase;text-decoration:none;transition:color .16s}
.retour:hover{color:var(--accent)}


.planche{display:block;width:100%;line-height:0;border:1px solid var(--line);
  background:var(--pl-paper);overflow:hidden}
.planche svg{display:block;width:100%;height:auto}
.planche-hero{margin:0 0 clamp(2rem,5vw,3rem);border:0;border-bottom:1px solid var(--line)}
.planche-chap{margin:0 0 clamp(1.8rem,4vw,2.6rem)}
.planche-interieure{margin:clamp(2.4rem,6vw,3.6rem) 0;
  width:min(52rem,92vw);margin-left:50%;transform:translateX(-50%)}

.contact{margin:clamp(2.6rem,7vw,4rem) 0 0}
.contact-txt{max-width:34rem;color:var(--dim);margin:0}
.contact-lien{display:inline-block;margin-top:1.4rem;padding:.85rem 1.4rem;
  border:1px solid var(--line);text-decoration:none;color:var(--accent);
  font-size:.85rem;letter-spacing:.04em;transition:border-color .16s,background .16s}
.contact-lien:hover{border-color:var(--accent);background:var(--raised)}

@media (max-width:38rem){
  .carte{padding:1.15rem 1.2rem;gap:.9rem}
  .carte .embleme{display:none}
  .carte .num{font-size:1.7rem;width:1.8rem}
  .nav-chap{grid-template-columns:1fr}
  .nav-chap .suiv{text-align:left}
  .prose .document{font-size:.7rem}
}
@media print{
  .barre,.chap-pied,.evite{display:none}
  body{background:#fff;color:#000;font-size:11pt}
  .prose .situation{color:#000}
}
"""

JS = r"""
(function(){
  var jauge = document.getElementById('jauge');
  var art   = document.querySelector('[data-chapitre]');

  if(art){
    try{ localStorage.setItem('pdd:reprise', JSON.stringify({
      url:art.dataset.url, titre:art.dataset.titre, num:art.dataset.chapitre })); }catch(e){}

    addEventListener('scroll', function(){
      var h = document.documentElement.scrollHeight - innerHeight;
      jauge.style.width = (h>0 ? Math.min(100, scrollY/h*100) : 0) + '%';
    }, {passive:true});

    addEventListener('keydown', function(e){
      if(e.metaKey||e.ctrlKey||e.altKey) return;
      var t=(e.target.tagName||'').toLowerCase();
      if(t==='input'||t==='textarea') return;
      var p=document.getElementById('lien-prec'), s=document.getElementById('lien-suiv');
      if(e.key==='ArrowLeft'  && p) location.href=p.href;
      if(e.key==='ArrowRight' && s) location.href=s.href;
    });
  }

  var m = document.getElementById('courriel');
  if(m){
    var adr = atob(m.dataset.c);
    m.href = 'mailto:' + adr + '?subject=' + encodeURIComponent('Le Poids des dieux');
    m.textContent = adr;
  }

  var bt = document.getElementById('theme');
  if(bt){
    var modes = ['auto','light','dark','encre'];
    var noms  = {auto:'Auto', light:'Clair', dark:'Sombre', encre:'Encre'};
    var cur;
    try{ cur = localStorage.getItem('pdd:theme') || 'auto'; }catch(e){ cur = 'auto'; }
    if(modes.indexOf(cur) < 0) cur = 'auto';
    function pose(m){
      cur = m;
      if(m === 'auto') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', m);
      bt.textContent = noms[m];
      try{ localStorage.setItem('pdd:theme', m); }catch(e){}
    }
    pose(cur);
    bt.addEventListener('click', function(){
      pose(modes[(modes.indexOf(cur) + 1) % modes.length]);
    });
  }

  var rep = document.getElementById('reprise');
  if(rep){
    try{
      var v = JSON.parse(localStorage.getItem('pdd:reprise')||'null');
      if(v && v.url){
        rep.href = v.url;
        rep.querySelector('.rep-titre').textContent = v.titre;
        rep.hidden = false;
      }
    }catch(e){}
  }
})();
"""


# ---------------------------------------------------------------- gabarits

def tete(titre_page, description, chemin_rel, prefixe, og_type="website"):
    base = BASE_URL.rstrip("/")
    url = base + "/" if chemin_rel == "index.html" else base + "/" + chemin_rel.lstrip("/")
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{t}</title>
<meta name="description" content="{d}"/>
<link rel="canonical" href="{u}"/>
<link rel="icon" type="image/svg+xml" href="{p}assets/favicon.svg"/>
<meta property="og:type" content="{ot}"/>
<meta property="og:site_name" content="{site}"/>
<meta property="og:locale" content="fr_FR"/>
<meta property="og:title" content="{t}"/>
<meta property="og:description" content="{d}"/>
<meta property="og:url" content="{u}"/>
<meta property="og:image" content="{base}/assets/og.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{t}"/>
<meta name="twitter:description" content="{d}"/>
<meta name="twitter:image" content="{base}/assets/og.png"/>
<meta name="theme-color" content="#0E1418" media="(prefers-color-scheme:dark)"/>
<meta name="theme-color" content="#E9ECEE" media="(prefers-color-scheme:light)"/>
<script>try{{var t=localStorage.getItem('pdd:theme');
if(t&&t!=='auto')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<link rel="stylesheet" href="{p}css/style.css"/>
</head>
<body>
<a class="evite" href="#contenu">Aller au contenu</a>
""".format(t=html.escape(titre_page), d=html.escape(description), u=html.escape(url),
           p=prefixe, ot=og_type, site=html.escape(TITRE),
           base=html.escape(BASE_URL.rstrip("/")))


def barre(prefixe, titre_courant=""):
    return """<div class="barre"><div class="enveloppe barre-i">
<a class="marque mono" href="{p}index.html">{titre}</a>
<span class="barre-titre mono">{c}</span>
<button class="theme mono" id="theme" type="button"
  aria-label="Changer de thème">Auto</button>
<span class="lampe" title="State &amp; Madison — cycle de 64 secondes"></span>
</div><div class="jauge" id="jauge"></div></div>
""".format(p=prefixe, titre=html.escape(TITRE), c=html.escape(titre_courant))


def pied(prefixe, n, mots):
    return """<footer class="pied mono">
<span>{n} chapitres · {m} mots</span>
<span><a href="{p}index.html#contact">Contact</a></span>
<span>Récit de fan non officiel. Dragon Ball Z appartient à Akira Toriyama et Shueisha ;
Invincible à Robert Kirkman et Image Comics.</span>
</footer>
""".format(n=n, m=mots, p=prefixe)


# ---------------------------------------------------------------- carte OG

def carte_sociale(chemin, n_chap, mots):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("  (Pillow absent — carte sociale ignorée)")
        return

    def police(noms, taille):
        for n in noms:
            for base in (r"C:\Windows\Fonts", "/System/Library/Fonts",
                         "/usr/share/fonts/truetype/dejavu", "/Library/Fonts"):
                p = Path(base) / n
                if p.exists():
                    try:
                        return ImageFont.truetype(str(p), taille)
                    except Exception:
                        pass
        return ImageFont.load_default()

    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (14, 20, 24))
    d = ImageDraw.Draw(im)

    d.rectangle([0, 0, W, 6], fill=(224, 104, 44))
    for i, y in enumerate(range(0, H, 3)):
        d.line([(0, y), (W, y)], fill=(17, 24, 29), width=1)

    f_sur = police(["georgiab.ttf", "Georgia Bold.ttf", "DejaVuSerif-Bold.ttf"], 30)
    f_tit = police(["georgia.ttf", "Georgia.ttf", "DejaVuSerif.ttf"], 108)
    f_sub = police(["georgiai.ttf", "Georgia Italic.ttf", "DejaVuSerif-Italic.ttf"], 34)
    f_mon = police(["consola.ttf", "Menlo.ttc", "DejaVuSansMono.ttf"], 24)

    d.text((80, 92), "DRAGON BALL Z  ×  INVINCIBLE", font=f_sur, fill=(224, 104, 44))
    d.text((80, 168), "Le Poids", font=f_tit, fill=(220, 227, 231))
    d.text((80, 286), "des dieux", font=f_tit, fill=(220, 227, 231))
    d.text((80, 424), "Tome 1 — « Vingt-deux minutes »", font=f_sub, fill=(141, 155, 166))

    d.line([(80, 500), (1120, 500)], fill=(36, 48, 57), width=1)
    cols = [("22 MIN", 80), ("2 400 000 MORTS", 300), ("109 000 / MINUTE", 640),
            ("%d CHAPITRES" % n_chap, 980)]
    for txt, x in cols:
        d.text((x, 530), txt, font=f_mon, fill=(94, 108, 119))

    d.ellipse([1112, 86, 1128, 102], fill=(63, 169, 106))

    chemin.parent.mkdir(parents=True, exist_ok=True)
    im.save(chemin, "PNG", optimize=True)


# ------------------------------------------------- version en fichier unique

JS_UNIQUE = r"""
(function(){
  var CH=window.__CH__, i=-1;
  var acc=document.getElementById('accueil'), lec=document.getElementById('lecteur');
  var jau=document.getElementById('jauge'), bt=document.querySelector('.barre-titre');

  function ouvrir(n){
    if(n<0||n>=CH.length) return;
    i=n; var c=CH[n];
    lec.innerHTML='<div class="enveloppe"><article class="colonne">'
      +'<header class="chap-tete"><div class="embleme">'+c.embleme+'</div>'
      +'<p class="num mono">Chapitre '+c.numero+'</p><h1>'+c.titre+'</h1>'
      +'<p class="sit mono">'+c.focal+'<br/>'+c.situation+'</p><div class="filet"></div></header>'
      +'<div class="prose">'+c.corps+'</div></article>'
      +'<footer class="chap-pied colonne"><nav class="nav-chap">'
      +(n>0?'<a href="#" data-va="'+(n-1)+'"><span class="sens mono">Précédent</span>'+CH[n-1].titre+'</a>'
           :'<span><span class="sens mono">Précédent</span>—</span>')
      +(n<CH.length-1?'<a class="suiv" href="#" data-va="'+(n+1)+'"><span class="sens mono">Suivant</span>'+CH[n+1].titre+'</a>'
           :'<span class="suiv"><span class="sens mono">Suivant</span>—</span>')
      +'</nav><a class="retour mono" href="#" data-va="-1">Retour aux chapitres</a></footer></div>';
    acc.style.display='none'; lec.style.display='block';
    bt.textContent='Chapitre '+c.numero+' — '+c.titre;
    document.title='Chapitre '+c.numero+' — '+c.titre;
    scrollTo(0,0);
    try{ localStorage.setItem('pdd:u', String(n)); }catch(e){}
  }
  function fermer(){ i=-1; lec.style.display='none'; acc.style.display='block';
    bt.textContent=''; document.title=window.__T__; jau.style.width='0'; scrollTo(0,0); }

  document.addEventListener('click', function(e){
    var a=e.target.closest('[data-va]'); if(a){ e.preventDefault();
      var v=+a.dataset.va; v<0?fermer():ouvrir(v); return; }
    var k=e.target.closest('[data-ouvre]'); if(k){ e.preventDefault(); ouvrir(+k.dataset.ouvre); }
  });
  var m=document.querySelector('.marque'); if(m) m.addEventListener('click',function(e){e.preventDefault();fermer();});

  var rep=document.getElementById('reprise');
  try{ var v=localStorage.getItem('pdd:u');
    if(rep&&v!==null&&CH[+v]){ rep.hidden=false;
      rep.querySelector('.rep-titre').textContent=CH[+v].titre;
      rep.setAttribute('data-ouvre',v); } }catch(e){}

  addEventListener('scroll',function(){ if(i<0)return;
    var h=document.documentElement.scrollHeight-innerHeight;
    jau.style.width=(h>0?Math.min(100,scrollY/h*100):0)+'%'; },{passive:true});
  addEventListener('keydown',function(e){ if(e.metaKey||e.ctrlKey||e.altKey||i<0)return;
    if(e.key==='Escape')fermer();
    if(e.key==='ArrowLeft'&&i>0)ouvrir(i-1);
    if(e.key==='ArrowRight'&&i<CH.length-1)ouvrir(i+1); });
})();
"""


def page_unique(chaps, cartes, n, mots_fmt):
    donnees = [{"numero": c["numero"], "titre": html.escape(c["titre"], quote=False),
                "focal": html.escape(c["focal"], quote=False),
                "situation": html.escape(c["situation"], quote=False),
                "embleme": c["embleme"], "corps": rendre(c["corps"])} for c in chaps]

    liens = [re.sub(r'href="chapitres/[^"]+"', 'href="#" data-ouvre="%d"' % k, c)
             for k, c in enumerate(cartes)]

    p = """<meta charset="utf-8"/>
<title>Le Poids des dieux</title>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>{css}</style>
<a class="evite" href="#contenu">Aller au contenu</a>
<div class="barre"><div class="enveloppe barre-i">
<a class="marque mono" href="#">{titre}</a>
<span class="barre-titre mono"></span>
<button class="theme mono" id="theme" type="button"
  aria-label="Changer de thème">Auto</button>
<span class="lampe" title="State &amp; Madison — cycle de 64 secondes"></span>
</div><div class="jauge" id="jauge"></div></div>

<main id="contenu"><div id="accueil"><div class="enveloppe">
<header class="masthead">
<p class="eyebrow mono">{sub}</p>
<h1>Le Poids<br/>des dieux</h1>
<p class="tome">{tome}</p>
<p class="pitch">Le ciel s'ouvre au-dessus de State Street à <strong>16 h 47</strong>.
Vingt-deux minutes plus tard, Chicago est une baie.</p>
<p class="these">Deux êtres arrivent dans un monde qu'ils peuvent détruire d'un geste,
et découvrent que la puissance absolue ne résout aucun des problèmes qui comptent.</p>
<dl class="compteurs">
<div class="compteur"><dt class="mono">Durée</dt><dd class="mono">22 min</dd></div>
<div class="compteur"><dt class="mono">Morts</dt><dd class="mono">2 400 000</dd></div>
<div class="compteur"><dt class="mono">Par minute</dt><dd class="mono">109 000</dd></div>
<div class="compteur"><dt class="mono">Corps rendus</dt><dd class="mono">0</dd></div>
</dl></header>

<a class="avenir" id="reprise" href="#" hidden>
<span class="mono">Reprendre la lecture</span><span class="rep-titre"></span></a>

<div class="section-titre"><h2>Les chapitres</h2><span class="fil"></span>
<span class="compte mono">{n} / {prevus}</span></div>
<div class="grille">{cartes}</div>

<div class="avenir"><span class="mono">À paraître</span>
Chapitre 11 — l'entraînement au-dessus du Pacifique, une flotte qui n'a pas le droit de tirer.
Puis les auditions au Capitole, la descente d'Anissa, et la pleine lune du dix-huit.</div>
{pied}
</div></div>
<div id="lecteur" style="display:none"></div></main>

<script>window.__T__="Le Poids des dieux";window.__CH__={data};</script>
<script>{js}</script>
""".format(css=CSS, js=JS_UNIQUE, titre=html.escape(TITRE), sub=SOUS_TITRE, tome=TOME,
           n=n, prevus=CHAPITRES_PREVUS, cartes="\n".join(liens),
           pied=pied("", n, mots_fmt), data=json.dumps(donnees, ensure_ascii=False))
    (SORTIE / "apercu-fichier-unique.html").write_text(p, encoding="utf-8")


# ---------------------------------------------------------------- build

def construire(avec_artifact=False):
    fichiers = sorted(CHAPITRES.glob("CH*.md"))
    chaps = [lire(f) for f in fichiers]
    chaps = [c for c in chaps if c["numero"]]
    chaps.sort(key=lambda c: c["numero"])
    if not chaps:
        sys.exit("Aucun chapitre trouvé dans %s" % CHAPITRES)

    total = sum(c["mots"] for c in chaps)
    mots_fmt = "{:,}".format(total).replace(",", " ")

    # On nettoie le contenu généré SANS toucher à .git — le dossier site/
    # est lui-même un dépôt une fois la mise en ligne configurée.
    PRESERVE = {".git", ".gitignore", "CNAME", "README.md"}
    if SORTIE.exists():
        for e in SORTIE.iterdir():
            if e.name in PRESERVE:
                continue
            shutil.rmtree(e) if e.is_dir() else e.unlink()
    (SORTIE / "chapitres").mkdir(parents=True, exist_ok=True)
    (SORTIE / "assets").mkdir(parents=True, exist_ok=True)
    (SORTIE / "css").mkdir(parents=True, exist_ok=True)
    (SORTIE / "js").mkdir(parents=True, exist_ok=True)

    (SORTIE / "css" / "style.css").write_text(CSS, encoding="utf-8")
    (SORTIE / "js" / "main.js").write_text(JS, encoding="utf-8")
    (SORTIE / "assets" / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (SORTIE / ".nojekyll").write_text("", encoding="utf-8")

    carte_sociale(SORTIE / "assets" / "og.png", len(chaps), total)

    (SORTIE / "planches").mkdir(parents=True, exist_ok=True)
    tout = {"%02d" % n: f for n, f in planches.PLANCHES.items()}
    for n, liste in planches.PLANCHES_INTERIEURES.items():
        for k, (_, f) in enumerate(liste):
            tout["%02d%s" % (n, "bcd"[k])] = f
    for nom, f in tout.items():
        (SORTIE / "planches" / (nom + ".svg")).write_text(
            f().replace(planches.INK, "#141C22").replace(planches.PAP, "#E9ECEE"),
            encoding="utf-8")

    # ---- index
    cartes = []
    for c in chaps:
        cartes.append(
            '<a class="carte" href="chapitres/{f}">'
            '<span class="num mono">{n:02d}</span>'
            '<span class="corps"><h3>{t}</h3>'
            '<span class="meta mono"><span class="focal">{fo}</span>'
            '<span>{j}</span><span>{l} min</span></span></span>'
            '<span class="embleme">{e}</span></a>'.format(
                f=c["fichier"], n=c["numero"], t=html.escape(c["titre"], quote=False),
                fo=html.escape(c["focal"], quote=False),
                j=html.escape(c["situation"].split("·")[0].strip(), quote=False),
                l=c["lecture"], e=c["embleme"]))

    schema = {
        "@context": "https://schema.org", "@type": "Book",
        "name": TITRE, "inLanguage": "fr", "description": DESCRIPTION,
        "url": BASE_URL.rstrip("/") + "/",
        "numberOfPages": len(chaps), "genre": ["Light novel", "Science-fiction", "Fan fiction"],
        "hasPart": [{"@type": "Chapter", "name": c["titre"], "position": c["numero"],
                     "url": BASE_URL.rstrip("/") + "/chapitres/" + c["fichier"]} for c in chaps],
    }

    index = tete(TITRE + " — Tome 1", DESCRIPTION, "index.html", "", "book")
    index += barre("")
    index += """<main id="contenu">
<div class="planche planche-hero">{front}</div>
<div class="enveloppe">
<header class="masthead">
<p class="eyebrow mono">{sub}</p>
<h1>Le Poids<br/>des dieux</h1>
<p class="tome">{tome}</p>
<p class="pitch">Le ciel s'ouvre au-dessus de State Street à <strong>16 h 47</strong>.
Vingt-deux minutes plus tard, Chicago est une baie.</p>
<p class="these">Deux êtres arrivent dans un monde qu'ils peuvent détruire d'un geste,
et découvrent que la puissance absolue ne résout aucun des problèmes qui comptent.</p>
<dl class="compteurs">
<div class="compteur"><dt class="mono">Durée</dt><dd class="mono">22 min</dd></div>
<div class="compteur"><dt class="mono">Morts</dt><dd class="mono">2 400 000</dd></div>
<div class="compteur"><dt class="mono">Par minute</dt><dd class="mono">109 000</dd></div>
<div class="compteur"><dt class="mono">Corps rendus</dt><dd class="mono">0</dd></div>
</dl>
</header>

<a class="avenir" id="reprise" href="#" hidden>
<span class="mono">Reprendre la lecture</span><span class="rep-titre"></span></a>

<div class="section-titre"><h2>Les chapitres</h2><span class="fil"></span>
<span class="compte mono">{n} / {prevus}</span></div>

<div class="grille">{cartes}</div>

<div class="avenir"><span class="mono">À paraître</span>
Chapitre 11 — l'entraînement au-dessus du Pacifique, une flotte qui n'a pas le droit de tirer.
Puis les auditions au Capitole, la descente d'Anissa, et la pleine lune du dix-huit.</div>

<section id="contact" class="contact">
<div class="section-titre"><h2>Écrire à l'auteur</h2><span class="fil"></span></div>
<p class="contact-txt">Une remarque sur un chapitre, une incohérence relevée, une envie de
lire la suite avant tout le monde : le courrier arrive et il est lu.</p>
<a class="contact-lien mono" id="courriel" href="#" data-c="{c}"
   rel="nofollow">écrire à l'auteur</a>
</section>

{pied}
</div></main>
<script type="application/ld+json">{schema}</script>
<script src="js/main.js" defer></script>
</body></html>
""".format(sub=SOUS_TITRE, tome=TOME, n=len(chaps), prevus=CHAPITRES_PREVUS,
           cartes="\n".join(cartes), pied=pied("", len(chaps), mots_fmt),
           front=planches.planche(0) or "",
           c=base64.b64encode(EMAIL.encode()).decode(),
           schema=json.dumps(schema, ensure_ascii=False))
    (SORTIE / "index.html").write_text(index, encoding="utf-8")

    # ---- chapitres
    for i, c in enumerate(chaps):
        pi = planches.planche_interieure(c["numero"])
        titres = [t for g, t in c["corps"] if g == "situation"]
        for ancre, _ in (pi or []):
            if not any(ancre.lower() in t.lower() for t in titres):
                sys.exit("Planche du ch. %d : aucun intertitre ne contient %r.\n"
                         "  Intertitres disponibles : %s" % (c["numero"], ancre, titres))
        prec = chaps[i - 1] if i > 0 else None
        suiv = chaps[i + 1] if i < len(chaps) - 1 else None
        t_page = "Chapitre %d — %s | %s" % (c["numero"], c["titre"], TITRE)

        p = tete(t_page, c["amorce"] or DESCRIPTION,
                 "chapitres/" + c["fichier"], "../", "article")
        p += barre("../", "Chapitre %d — %s" % (c["numero"], c["titre"]))
        p += """<main id="contenu"><div class="enveloppe">
<article data-chapitre="{n}" data-url="chapitres/{f}" data-titre="{t}">
<div class="planche planche-chap">{pl}</div>
<div class="colonne">
<header class="chap-tete">
<div class="embleme">{e}</div>
<p class="num mono">Chapitre {n}</p>
<h1>{t}</h1>
<p class="sit mono">{fo}<br/>{s}</p>
<div class="filet"></div>
</header>
<div class="prose">{corps}</div>
</div>
</article>

<footer class="chap-pied colonne"><nav class="nav-chap">{nav}</nav>
<a class="retour mono" href="../index.html">Retour aux chapitres</a></footer>
</div></main>
<script src="../js/main.js" defer></script>
</body></html>
""".format(n=c["numero"], f=c["fichier"], t=html.escape(c["titre"], quote=True),
           e=c["embleme"], fo=html.escape(c["focal"], quote=False),
           pl=planches.planche(c["numero"]) or "",
           s=html.escape(c["situation"], quote=False), corps=rendre(c["corps"], pi),
           nav=(('<a id="lien-prec" href="%s"><span class="sens mono">Précédent</span>%s</a>'
                 % (prec["fichier"], html.escape(prec["titre"], quote=False)))
                if prec else '<span><span class="sens mono">Précédent</span>—</span>')
               + (('<a id="lien-suiv" class="suiv" href="%s"><span class="sens mono">Suivant</span>%s</a>'
                   % (suiv["fichier"], html.escape(suiv["titre"], quote=False)))
                  if suiv else '<span class="suiv"><span class="sens mono">Suivant</span>—</span>'))
        (SORTIE / "chapitres" / c["fichier"]).write_text(p, encoding="utf-8")

    # ---- 404
    q404 = tete("Page introuvable | " + TITRE, "Cette page n'existe pas.", "404.html", "")
    q404 += barre("")
    q404 += """<main id="contenu"><div class="enveloppe"><div class="colonne" style="padding:6rem 0">
<p class="eyebrow mono">Erreur 404</p>
<h1 style="font-size:clamp(2rem,7vw,3.2rem)">Rien à signaler.</h1>
<p class="pitch">Cette page n'existe pas — ou plus.</p>
<p style="margin-top:2rem"><a class="retour mono" href="index.html">Retour aux chapitres</a></p>
</div></div></main></body></html>"""
    (SORTIE / "404.html").write_text(q404, encoding="utf-8")

    # ---- robots + sitemap
    base = BASE_URL.rstrip("/")
    (SORTIE / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % base, encoding="utf-8")

    aujourd = date.today().isoformat()
    urls = ['<url><loc>%s/</loc><lastmod>%s</lastmod><priority>1.0</priority></url>' % (base, aujourd)]
    for c in chaps:
        urls.append('<url><loc>%s/chapitres/%s</loc><lastmod>%s</lastmod><priority>0.8</priority></url>'
                    % (base, c["fichier"], aujourd))
    (SORTIE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
        % "\n".join(urls), encoding="utf-8")

    # ---- version fichier unique, pour aperçu hors ligne
    if avec_artifact:
        page_unique(chaps, cartes, len(chaps), mots_fmt)

    poids = sum(f.stat().st_size for f in SORTIE.rglob("*") if f.is_file())
    print("Écrit : %s" % SORTIE)
    print("  %d chapitres · %s mots · %d fichiers · %.0f Ko"
          % (len(chaps), mots_fmt, sum(1 for f in SORTIE.rglob("*") if f.is_file()), poids / 1024))
    print("  URL de base : %s" % BASE_URL)


if __name__ == "__main__":
    construire("--artifact" in sys.argv)
