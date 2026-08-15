# docs/ — le site publié

**Dossier généré. Ne rien y modifier à la main :** tout est réécrit à chaque exécution de
`99_OUTILS/build_site.py`. Seuls `.git`, `.gitignore`, `CNAME` et ce `README.md` survivent.

## Activer GitHub Pages — une seule fois

**Settings → Pages → Source : Deploy from a branch → `main` → dossier `/docs` → Save.**

Le site sort deux minutes plus tard sur :

```
https://saniadamou14.github.io/Confrontation/
```

C'est l'adresse inscrite dans `BASE_URL`, en tête de `build_site.py`. **Si tu renommes le
dépôt, change aussi cette constante**, sinon les URL canoniques, le sitemap et la carte
sociale pointeront à côté.

## Publier un nouveau chapitre

```bash
python 99_OUTILS/build_site.py
git add -A && git commit -m "chapitre 11" && git push
```

## Réglages en tête de build_site.py

| Constante | Rôle |
|---|---|
| `BASE_URL` | Adresse publique. Sert aux URL canoniques, au sitemap, aux cartes de partage. |
| `EMAIL` | Adresse de contact affichée en bas de l'accueil. |
| `CHAPITRES_PREVUS` | Le « 10 / 20 » de l'index. |

## Nom de domaine

1. Créer un fichier `CNAME` ici, contenant seulement le domaine, sans `https://`.
2. Chez le registrar : un enregistrement `CNAME` vers `saniadamou14.github.io`.
3. Mettre `BASE_URL` à jour, régénérer, pousser.

## Contenu

| | |
|---|---|
| `index.html` | Accueil, index, contact, données structurées `schema.org/Book` |
| `chapitres/*.html` | Une page par chapitre, adresse propre, partageable et indexable |
| `css/style.css` · `js/main.js` | Même organisation que le portfolio |
| `assets/og.png` | Carte de partage 1200 × 630, régénérée à chaque build |
| `sitemap.xml` · `robots.txt` · `404.html` · `.nojekyll` | Référencement et service |
| `apercu-fichier-unique.html` | Version autonome en un fichier, pour lire hors ligne |
