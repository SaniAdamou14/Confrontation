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
| Chapitres écrits | **2 / 120** |
| Date récit | Jour 0, 17 h 26. Les vingt-deux minutes sont terminées. |
| Arbitrages | **Tous tranchés.** Oliver survit, les Guardians survivants sont fixés. Bible corrigée. |
| Point ouvert | ⚠ Le scouteur est détruit au ch. 1. Payoff F10 à re-router avant le ch. 14 — voir `FUSILS_DE_TCHEKHOV.md`. |
| Prochaine action | Dossier préparatoire du **chapitre 3**, focalisation Cecil |

### Décisions canoniques ajoutées à la bible

| # | Décision |
|---|---|
| 1 | Anissa au **jour 13**, avant l'Ozaru. Tome 1 = **vingt jours**. Ce qu'elle rapporte à l'Empire ne contient pas le jour 17. |
| 2 | Lune du jour 0 = **croissant décroissant quasi invisible**. Détection par Végéta au J3 par occultation stellaire. |
| 3 | **Le lac Michigan entre dans le cratère. Chicago devient une baie.** La vapeur explique le délai du premier bilan. |
| 4 | Les dix-neuf minutes de Goku s'achèvent à **17 h 09** : les vingt-deux minutes finissent parce qu'il s'arrête, pas parce que le combat finit. |
| 5 | Caméraman du ch. 2 : **Ray Dombrowski**, vingt-six ans à filmer les Guardians of the Globe. Il survit. **Art Rosenbaum** ajouté au dossier personnages. |
