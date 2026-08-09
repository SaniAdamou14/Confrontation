# LE POIDS DES DIEUX — Poste de travail

Light novel — Dragon Ball Z (arc Namek) × Invincible.
Cinq tomes, 120 chapitres, 5 000 à 8 000 mots par chapitre.

> **Deux êtres arrivent dans un monde qu'ils peuvent détruire d'un geste, et découvrent que la puissance absolue ne résout aucun des problèmes qui comptent.**

---

## Hiérarchie d'autorité

En cas de contradiction entre deux fichiers, l'ordre suivant tranche :

1. **`BIBLE_LE_POIDS_DES_DIEUX.md`** — source de vérité unique. Tout le reste en dérive.
2. **`02_ETAT_DU_MONDE/JOURNAL_ETAT.md`** — l'état du monde *maintenant*. Prime sur la bible pour tout ce qui évolue (morts, blessures, ki, savoirs).
3. **`00_CANON/`** — chronologie, géographie, lexique. Dérivés fixes.
4. **`03_PLAN/`** — plans de tome. Modifiables librement tant qu'un chapitre n'est pas écrit.
5. **Chapitres publiés** (`04_CHAPITRES/`) — une fois écrit, un chapitre devient du canon. On ne le contredit pas, on compose avec.

Un dérivé ne réécrit jamais la bible. S'il la contredit, c'est le dérivé qui a tort — sauf si le point est listé dans `00_CANON/POINTS_A_ARBITRER.md` et tranché.

---

## Carte des dossiers

```
BIBLE_LE_POIDS_DES_DIEUX.md      Source de vérité. Ne pas fragmenter.
README.md                        Ce fichier.

00_CANON/                        Ce qui est fixe.
  CHRONOLOGIE_MAITRESSE.md       J-8 → J+20, minute par minute au jour 0. Calendrier lunaire.
  CARTE_ET_LIEUX.md              Chicago, le cratère, les lieux récurrents.
  LEXIQUE_ET_ORTHOGRAPHES.md     Noms propres, typographie, unités, conventions FR.
  POINTS_A_ARBITRER.md           Contradictions relevées + propositions. À trancher avant le ch. 1.

01_PERSONNAGES/                  Complète la §7 de la bible, ne la duplique pas.
  INDEX.md                       Qui est où, et quelle fiche fait autorité.
  CONQUEST.md                    Focalisation du chapitre 1. Fiche complète.
  MARK_GRAYSON.md                Présent au ch. 1-2, mort au jour 0.
  PERSONNAGES_ORIGINAUX.md       Créations nécessaires au récit (caméraman, survivants, GDA).

02_ETAT_DU_MONDE/                Ce qui bouge. À tenir à jour après chaque chapitre.
  JOURNAL_ETAT.md                Version vivante de la §13.
  REGISTRE_MORTS.md              Nommés + compteurs.
  REGISTRE_BLESSURES.md          R4 : le corps compte. Chaque trace, sa durée.
  REGISTRE_DESTRUCTIONS.md       R5 : chaque destruction a un chiffre et un après.
  FUSILS_DE_TCHEKHOV.md          Ce qui est planté, quand ça tire.
  QUI_SAIT_QUOI.md               Matrice d'information par faction. Indispensable pour R6.

03_PLAN/
  TOME_1.md                      Plan détaillé, chapitre par chapitre.
  TOMES_2_A_5.md                 Esquisses.

04_CHAPITRES/
  T1/                            Les chapitres écrits.

05_ATELIER/
  CH01_DOSSIER_PREPARATOIRE.md   Tout ce qu'il faut pour écrire le chapitre 1.

99_OUTILS/
  CHECKLIST_CHAPITRE.md          Avant / pendant / après.
  PROMPT_DE_REPRISE.md           Ordre de lecture pour un modèle qui reprend le projet à froid.
```

---

## Boucle de travail d'un chapitre

1. Lire `99_OUTILS/PROMPT_DE_REPRISE.md`.
2. Lire `02_ETAT_DU_MONDE/JOURNAL_ETAT.md` — d'abord. C'est l'état réel du monde.
3. Lire le dossier préparatoire du chapitre dans `05_ATELIER/`. S'il n'existe pas, l'écrire avant la prose.
4. Écrire dans `04_CHAPITRES/T1/CHxx_titre.md`.
5. Passer `99_OUTILS/CHECKLIST_CHAPITRE.md`.
6. Mettre à jour : `JOURNAL_ETAT.md`, les registres touchés, `QUI_SAIT_QUOI.md`, `FUSILS_DE_TCHEKHOV.md`.

Étape 6 non négociable. Un chapitre écrit sans mise à jour des registres est un chapitre qui rendra le suivant faux.

---

## État actuel

| | |
|---|---|
| Chapitres écrits | **6 / 120** |
| Date récit | Jour 6, 23 h 40 |
| Arbitrages | **Tous tranchés.** Bible corrigée (v2.1). |
| Point ouvert | ⚠ Le scouteur est détruit au ch. 1. Payoff F10 à re-router avant le ch. 14 — voir `FUSILS_DE_TCHEKHOV.md`. |
| Prochaine action | Dossier préparatoire du **chapitre 7** — Debbie exige de parler à celui qui a tué son fils |
| Passes de style | ✔ Tic n°2 (`comme on…`) rattrapé sur les ch. 1-6 : **32 → 10, deux par chapitre.** Aucune dette restante. |

### Révisions de la bible (v2.1)

| Point | Changement |
|---|---|
| **§5.2** | « La faim » remplacée par **« L'ignorance »**. Deux êtres qui rasent une ville ne chapardent pas : ce n'est pas du vol, c'est **du tribut**. La faim redescend au rang de physiologie (R4). L'épuisement reste réel mais devient la séquelle d'un engagement de plusieurs jours, pas une contrainte quotidienne. |
| **§6.1** | Levier n°1 du mémorandum OMEGA : **l'information, pas les calories.** « Ils ne comprennent rien à ce monde, et ils ont besoin de quelqu'un qui le comprenne. » |
| **§2, §5.4, §13** | Conquest : ~5 000 ans, uniforme de tissu sans plaque, main droite cybernétique. Lune du J0 corrigée. |
| **§3, §6.3, §10** | Le lac, Anissa au J13, les dix-neuf minutes à 17 h 09, tome 1 sur vingt jours. |
| **Lexique** | **Règle de nomination Nolan / Omni-Man.** « Grayson » ne sort d'aucune bouche. |

### Calibrage du registre

Le bloc §0 de `05_ATELIER/CH03_DOSSIER_PREPARATOIRE.md` codifie la technique narrative visée, dérivée de Togashi : **l'interrogatoire plutôt que le processus, l'exposition portée par quelqu'un qui a quelque chose à perdre, le calcul comme scène d'action, la révélation stratégique tardive.** Il vaut pour tous les chapitres suivants et se lit avec la passe de style de `99_OUTILS/CHECKLIST_CHAPITRE.md`.

### Décisions canoniques ajoutées à la bible

| # | Décision |
|---|---|
| 1 | Anissa au **jour 13**, avant l'Ozaru. Tome 1 = **vingt jours**. Ce qu'elle rapporte à l'Empire ne contient pas le jour 17. |
| 2 | Lune du jour 0 = **croissant décroissant quasi invisible**. Détection par Végéta au J3 par occultation stellaire. |
| 3 | **Le lac Michigan entre dans le cratère. Chicago devient une baie.** La vapeur explique le délai du premier bilan. |
| 4 | Les dix-neuf minutes de Goku s'achèvent à **17 h 09** : les vingt-deux minutes finissent parce qu'il s'arrête, pas parce que le combat finit. |
| 5 | Caméraman du ch. 2 : **Ray Dombrowski**, vingt-six ans à filmer les Gardiens du Globe. Il survit. **Art Rosenbaum** ajouté au dossier personnages. |
