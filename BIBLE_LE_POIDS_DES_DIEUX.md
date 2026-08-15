# PROJET « LE POIDS DES DIEUX »
### Light novel — Dragon Ball Z (arc Namek) × Invincible
**Bible narrative v2.0 — Document maître de persistance mémoire**
*Régime de puissance : Saiyans écrasants. Enjeu : que font-ils de cette puissance ?*

---

## 0. PROTOCOLE D'UTILISATION

Ce fichier est la **source de vérité unique**. Tout modèle qui reprend ce projet doit :

1. Lire les sections 1 à 6 avant d'écrire une ligne.
2. Consulter la section 7 (voix) avant tout dialogue.
3. Mettre à jour la section 13 (journal d'état) après chaque chapitre.
4. Ne jamais faire agir un personnage contre son intérêt propre pour arranger l'intrigue.

### La thèse du récit, en une phrase

> **Deux êtres arrivent dans un monde qu'ils peuvent détruire d'un geste, et découvrent que la puissance absolue ne résout aucun des problèmes qui comptent.**

Tout découle de là. Les combats ne sont pas le suspense — ils sont la **démonstration**. Le suspense est ailleurs : dans ce qui reste après.

### Les six règles d'écriture non négociables

**R1 — Personne ne dit ce qu'il veut vraiment.** Sauf Goku, et c'est précisément ce qui met les autres mal à l'aise. Cecil ne dit jamais « nous ne pouvons pas les vaincre » ; il demande le budget d'évacuation de la côte Ouest, et le lecteur comprend seul. Un dialogue qui transmet proprement une information est un dialogue raté.

**R2 — Pas de résumé de fin de chapitre.** Aucun « Fin de l'épisode X. Le monde retient son souffle. » Un chapitre s'achève sur une image, une réplique, ou un geste. Jamais sur un bilan.

**R3 — Aucun chiffre de puissance dans la prose.** Les échelles de la section 4 sont des outils d'arbitrage internes. Le lecteur ressent, il ne calcule pas.

**R4 — Le corps compte, même chez les dieux.** Faim saiyan, épuisement de ki, sang séché qu'on n'a pas nettoyé, combinaison qui gratte à l'épaule. La démesure ne dispense pas du concret.

**R5 — Chaque destruction a un chiffre et un après.** Une ville rasée reste rasée pendant des tomes. Les assurances refusent de payer. Les survivants forment des associations. Le compte s'accumule.

**R6 — La narration est incarnée.** Pas de voix de reportage. Le narrateur adopte la focalisation d'un personnage, déclarée par un intertitre discret (lieu + heure), et ne sait que ce que ce personnage sait.

> **⚠ PORTÉE DE R6 — correction majeure.** R6 gouverne **ce qu'on raconte au lecteur**. Elle ne gouverne pas **ce que le monde fait**. Pendant sept chapitres, la confusion des deux a mis en pause tout personnage non focalisé : le monde n'avait d'état qu'aux instants où un chapitre se terminait, et l'horloge du récit était le compteur de chapitres. **Le monde agit en permanence, qu'on le regarde ou non ; le lecteur ne l'apprend que par le focal, et sous forme de trace.** Voir `02_ETAT_DU_MONDE/AGENDAS.md`, le seul fichier du projet qui soit en amont.

### Les quatre règles de phrase — ajoutées après mesure des chapitres 1 à 7

R1 à R6 prescrivent du **contenu** : mets un corps, mets un chiffre, tiens une focalisation. **Aucune ne prescrit rien au niveau de la phrase**, et c'est à ce niveau-là que la platitude vit. Les quatre suivantes s'appliquent **avant** d'écrire, et se vérifient avec `99_OUTILS/lint_chapitre.py`.

**R7 — Le narrateur ne justifie pas.** Maximum **trois** « parce que » dans la narration par chapitre — illimité en dialogue. **Zéro** apposition « …, ce qui… / …, ce que… ». Si un geste ne se suffit pas à lui-même, c'est le geste qu'il faut changer, pas la subordonnée qu'il faut ajouter. *(Mesuré : ch. 7 en comptait 16 et 7. Le reste du tome tient entre 3 et 6.)*

**R8 — Une échelle porteuse, et toute autre échelle doit entrer en collision avec elle.**

Ce n'est pas un budget de chiffres, et l'idée qu'on pourrait en fixer un est fausse : **le meilleur passage du tome — le chambranle — est plus dense en chiffres que le pire.** Ce qui le sauve, c'est que ses nombres se **soustraient** : un mètre trente-sept hier, un mètre quarante et un aujourd'hui, quatre centimètres en un jour.

**Et ce n'est pas non plus « une seule échelle ».** Le chambranle en porte deux, et il marche **grâce** à la seconde : la hauteur se heurte à l'âge. *Neuf ans, dix ans* ne sont pas des centimètres — c'est la collision, des centimètres qui mesurent les années d'un enfant mort, qui fait la scène. Une règle d'échelle unique supprimerait exactement cet effet.

Donc : **une échelle porte la scène ; une seconde est autorisée si elle percute la première ; toute échelle qui ne fait ni l'un ni l'autre est du bruit.** Onze pages, vingt-neuf fois, quatre secondes et neuf mois dans la même scène ne se comparent à rien, donc aucun ne pèse.

*(Le compteur du lint mesure les familles d'unités : le chambranle en tient **cinq**, le tome tourne entre sept et dix. **Le nombre est la conséquence de la règle, pas la règle.** Un dépassement est un signal à examiner, pas une faute automatique.)*

**R9 — Variation.** Jamais plus de **deux paragraphes consécutifs** ouverts par le même mot — **sauf si la série est une progression**, et alors elle est une figure et non un tic. *« À neuf heures dix. À dix kilomètres. À douze. »* converge sur quelque chose ; *« Il a élargi. Il a trouvé. Il a continué. »* ne converge sur rien. **Le test : retirer le troisième paragraphe. Si la série perd son sens, c'est une figure. Si elle n'y perd rien, c'est un tic.**

> **Garde-fou sur l'exemption.** Une clause de ce genre avale sa règle, parce que tout auteur croit que sa série converge. **Contrôle : le taux de séries exemptées reste sous 40 %.** Ligne de base établie sur les chapitres 1 à 7 — seize séries relevées, **trois gardées, soit 19 %**. Au-dessus de 40 %, l'exemption est devenue une porte de sortie et il faut la resserrer. Au moins **un paragraphe de plus de soixante mots par scène**. Au moins un passage en discours indirect libre par chapitre. *(Le pourcentage global a été abandonné : posé à 15 %, il était enfreint par sept chapitres sur sept, donc c'était le seuil qui était faux. Ce que le lecteur sent est une **série**, pas une proportion : cinq paragraphes d'affilée en « Il » s'entendent, les mêmes cinq répartis sur une scène de vingt ne s'entendent pas. Seuil calibré : le chambranle plafonne à **deux**. Le tome monte à cinq.)*

**R10 — Realia américaine.** Le décor est américain, les procédures aussi. Une table de correspondance est tenue dans `00_CANON/LEXIQUE_ET_ORTHOGRAPHES.md`, alimentée à chaque métier qui entre dans le récit. *Lycée*, *commissariat*, *service des sinistres* sont du français de traduction normal. **Un compromis de vente et un diagnostic obligatoire n'existent pas aux États-Unis** — et une scène bâtie dessus est fausse dans sa mécanique, pas seulement dans son vocabulaire.

> **Ce qui n'est PAS une règle, et pourquoi.** Un ratio imparfait / passé composé a été envisagé puis abandonné. D'abord parce que deux compteurs honnêtes ne convergent pas dessus — selon qu'on traite *avait* comme auxiliaire ou comme verbe plein, le chapitre 7 donne 118 ou 186. Ensuite et surtout parce qu'**un ratio de temps verbaux n'est pas un signal de qualité** : une scène d'action doit être au passé composé, une scène d'habitude à l'imparfait, et un imparfait ajouté pour atteindre un nombre est exactement la phrase morte qu'on cherche à supprimer. Le lint le mesure en information, sans seuil. Le constat reste vrai — le tome a trop de premier plan — mais il se corrige à la lecture, pas au compteur.

> **La méthode qui a produit R7 à R10, et qui vaut plus qu'elles.** Chaque seuil a d'abord été posé au jugé, puis mesuré sur le corpus, puis **jeté quand la mesure le contredisait**. Un plafond de densité de chiffres et un pourcentage d'attaques identiques sont morts comme ça. Le test est simple : *une règle enfreinte par sept chapitres sur sept ne décrit pas un corpus malade, elle décrit un seuil inventé.* Un seuil se calibre sur un passage dont on sait qu'il fonctionne — ici le chambranle — et il doit laisser passer ce passage tout en attrapant les autres. Appliquer ça à toute règle future.

**Longueur cible :** 5 000 à 8 000 mots par chapitre.

---

## 1. LE POINT DE BASCULE

### 1.1 État exact des Saiyans au départ

**Namek, jour 8 de l'invasion.** Le Commando Ginyu est défait. Ginyu est une grenouille.

**Goku / Kakarotte.** Sorti de la capsule médicale depuis quarante minutes. Le zenkai post-guérison est actif. Gi orange, ceinture bleue, kanji 亀 dans le dos. Aucun haricot magique. **Queue intacte.** Il vient de choisir de rester du côté de Végéta — non par loyauté, mais parce que Freezer a détruit sa race et tué son père, et qu'il a décidé que ça, ça le regarde.

**Végéta.** Armure prise dans la réserve du vaisseau de Freezer après le combat contre Recoome : **plastron blanc, plaques ventrales brunes, simples bretelles blanches — aucune épaulette** — sur combinaison bleu marine. **Fissure à l'omoplate gauche, faite quelques heures plus tôt contre Ginyu.** Il vient de dormir — l'unique sommeil de tout l'arc. **Queue intacte.**

**Le scouteur.** Il a écrasé le sien sur Namek, bien avant, le jour où il a déclaré qu'il n'en avait plus besoin. Celui qu'il porte au jour 0 est **ramassé sur un cadavre du Commando Ginyu quelques heures avant la faille.** Objet de pillage. Il ne s'en sert pas pour mesurer — il sent le ki — mais pour lire ce que l'Empire écrivait dessus. C'est pour ça qu'il le lâchera sans regret. Voir `00_CANON/ARBITRAGE_CANON_V3.md` §5.

> **LES DIVERGENCES CANONIQUES DÉCLARÉES.** La queue, structurelle — voir section 5.4. Et une compression : dans le canon, Goku reste bien plus longtemps dans la capsule médicale. Le récit l'en fait sortir au jour 8. C'est la seule entorse à la ligne DBZ, elle est nécessaire à la prémisse, et elle est déclarée.

### 1.2 La faille — mécanique et non-destin

Le noyau de Namek est percé. Les Dragon Balls concentrent une densité d'énergie non-thermodynamique. Et Guldo, décapité par Végéta, a laissé son pouvoir de gel temporel s'effondrer sans point d'ancrage : un pouvoir qui arrête le temps localement crée une **dette causale** que son porteur rembourse en respirant. Guldo ne respire plus.

Simultanément, **Angstrom Levy** teste ses premiers sauts inter-réalités. Il ne cherche pas des Saiyans. Il cherche des versions de lui-même. L'une de ses perforations s'accroche à la seule chose qui, dans l'univers voisin, émet une signature causale comparable : la dette de Guldo.

**La faille ne les a pas choisis. Elle a pris les deux corps les plus proches du point d'effondrement.** Aucun personnage ne doit jamais suggérer un destin. S'il le fait, il a tort, et le récit lui donnera tort.

**Transit :** onze secondes pour Goku, quatre pour Végéta. Sept secondes de matière-temps manquent quelque part. Angstrom les a. Il ne sait pas encore quoi en faire.

### 1.3 Le point d'arrivée

**Chicago, jour 0, 16 h 47.** Conquest est là depuis dix-neuf minutes. Quarante-trois morts. Mark Grayson se bat depuis onze minutes : bras gauche cassé en deux endroits, trois côtes enfoncées, hémorragie interne. Atom Eve est au sol, réserve vidée, inconsciente à cent mètres. **Oliver est venu seul aider son frère et Conquest l'a mis à terre avant 16 h 47.**

> **CE QUI VIENT DE SE PASSER, ET QUI CHANGE TOUT.** Quelques jours plus tôt, la Terre a subi la **Guerre Invincible** : des dizaines de doubles de Mark Grayson venus d'autres réalités. Des centaines de milliers de morts. L'équipe des Gardiens du Globe en sort démolie — Rex Splode tué, Darkwing perdu, Monster Girl en réanimation, Black Samson blessé, Shapesmith coupé en deux, Immortal décapité puis régénéré, avec une cicatrice fraîche tout autour du cou. **Au jour 0, la Terre n'a plus d'équipe : elle a trois personnes debout et une agence qui compte encore ses morts de la semaine précédente.**

> **NOLAN GRAYSON N'EST PAS LÀ.** Il est détenu par l'Empire viltrumite, hors de la Terre, depuis des mois. **Vivant.** Il ignore tout de ce qui suit, et rien ne garantit qu'il l'apprenne un jour. Voir `00_CANON/ARBITRAGE_CANON_V3.md`.

Conquest **marche** vers Mark. Pas vol. Marche. C'est du mépris, et c'est important.

Le ciel se déchire au-dessus de State Street.

---

## 2. LES SEPT SECONDES

Scène fondatrice. Elle fixe tous les alignements.

**Seconde 0.** Végéta traverse une façade vitrée, se rétablit à quinze mètres du sol. Il voit un vieillard immense à moustache, en uniforme viltrumite blanc et rouge — **du tissu, jamais de plaque** —, une masse dans une main droite en métal, debout sur un cratère. Un gamin en bleu et jaune qui crache du sang.

Végéta ne cherche pas à comprendre. Il **évalue**. Un dominant, un dominé. Sa lecture est immédiate et juste.

**Secondes 1-3.** Conquest lève les yeux. Une race qu'il ne connaît pas. Une queue. Il sourit — **le premier vrai sourire depuis deux mille ans.** *(Conquest a environ cinq mille ans. Toute durée le concernant se compte en siècles ou en millénaires, jamais en décennies.)*

**Seconde 4.** Conquest, sans hausser le ton : « Tu voles. Tu n'as pas peur. Et tu n'es pas d'ici. » Un geste du menton vers Mark. « Attends ton tour, ou prends le sien. »

**Secondes 5-6.** Végéta rit. Court, sec, sans joie. Il ne répond pas à Conquest ; il parle à personne, ou à Freezer qu'il croit encore derrière lui : *« Encore un. Toujours le même modèle. Toujours la même phrase. »*

Puis il frappe.

**Seconde 7.** Goku arrive, désorienté, encaisse le contrecoup de l'onde de choc — et son premier geste n'est pas de frapper. Il vole vers Eve, la ramasse, la dépose derrière une ligne de béton à deux cents mètres.

**Le monde se divise en deux camps sur eux à cet instant précis.** Il y a des caméras. Un hélicoptère de chaîne d'info. Deux images tournent en boucle pendant six semaines : l'homme en orange qui sauve la fille, et l'homme en armure qui rit avant de frapper.

Ces sept secondes définissent tout le reste.

---

## 3. LE JOUR 0 — LA DÉMONSTRATION

**16 h 47 → 17 h 09. Vingt-deux minutes.**

Ce n'est pas un combat. C'est une leçon d'anatomie donnée à une planète.

**Végéta contre Conquest.** Quatre-vingt-dix secondes de domination totale. Végéta *sait* qu'il domine, s'en délecte, et laisse Conquest se relever pour prolonger. Conquest apprend pendant ces secondes-là — c'est ce qui le rend précieux. À trois minutes, il a cessé de reculer. À onze minutes, il rit encore avec la mâchoire enfoncée. À dix-sept, Végéta cesse de s'amuser.

Une sphère de la taille d'une voiture. Lâchée sans un mot. Conquest est traversé, désintégré, et le souffle emporte le centre-ville jusqu'aux banlieues.

**Goku contre les frères Grayson.** Mark et Oliver. Aucun des deux ne comprend ce qui les tue. Goku non plus, d'ailleurs : il frappe avec la retenue qu'il appliquerait à un Saibaman, et les corps ne tiennent pas.

Oliver perd un bras sur un coup de pied qui n'était pas destiné à le blesser gravement — **il survit, et il est le seul.** Mark est enfoncé dans le sol jusqu'aux épaules.

> **RÈGLE ABSOLUE POUR CETTE SÉQUENCE.** Goku n'est pas cruel. Il est **calibré pour un autre univers**. Il ne comprend pas encore qu'il tue. Quand il le comprend, dix-neuf minutes plus tard — c'est-à-dire à 17 h 09 précises, et c'est pour cela que les vingt-deux minutes s'arrêtent là : non parce que le combat finit, mais parce que Goku s'arrête —, il n'a aucun cadre mental pour traiter l'information — parce que dans son monde, on ressuscite. **C'est ça qui est terrifiant, et c'est ça qu'il faut écrire.** Pas de remords immédiat. Une incompréhension.

**Les Gardiens du Globe.** Ils arrivent à 16 h 54, et ils ne sont que trois — c'est tout ce que la Guerre a laissé de disponible.

**Immortal**, qui porte encore la cicatrice de sa propre décapitation, tient une seconde le poing de Goku dans sa main, puis part en deux morceaux sur une ligne blanche de quatre cents mètres. **L'homme qui revient toujours ne revient pas.** — **Black Samson**, descendu par au-dessus, laisse un cratère de trente mètres et rien dedans. — **Shapesmith**, effacé d'un revers de main par Végéta ; ce qui tombe à l'image, c'est son vrai visage, pour la première fois et la dernière. — **Eve**, réveillée, tuée en tentant un bouclier.

**Bilan à 17 h 09 :** Chicago n'existe plus. Cratère de neuf kilomètres. 2,4 millions de morts, point central établi au jour 2. **Révision à 3,1 millions rendue au jour 10**, classée sans être lue. *(La v2 datait cette révision du jour 4 : incompatible avec le ch. 3, où Ilana Voss annonce qu'il lui faut trois semaines pour resserrer sa marge. Corrigé le 15 août 2026. `CHRONOLOGIE_MAITRESSE.md` §3 fait foi.)*

**Et le lac entre.** Le cratère est centré sur State Street, à un kilomètre du rivage : sa lèvre est orientale est dans le lac Michigan, sur plus de trois kilomètres, et il n'y a pas de paroi. L'eau s'engouffre dans un bassin encore incandescent. Une colonne de vapeur visible à cent kilomètres masque le site pendant des jours et rend toute reconnaissance aérienne impossible — c'est pour cela que le premier chiffre met deux jours à venir. En une semaine, le cratère est plein. **Chicago n'est pas une ville rasée : c'est une baie.** On ne reconstruira pas, parce qu'il n'y a plus de sol. La question ne sera jamais « faut-il rebâtir ? », elle sera « comment appelle-t-on ça sur les cartes ? ».

---

## 4. RÉGIME DE PUISSANCE

### 4.1 Le principe directeur

**Les Saiyans arrivent avec une puissance déjà écrasante. Ils ne sont pas invincibles. Ils sont hors catégorie.**

La nuance est décisive et doit être tenue partout : ils **peuvent** être blessés, épuisés, piégés, contraints, brisés moralement, manipulés. Ils ne peuvent simplement pas être vaincus au poing par ce monde.

### 4.2 Échelle interne (jamais énoncée dans le texte)

| Rang | Entités |
|---|---|
| **Hors échelle** | Freezer forme finale (absent, hors d'atteinte du récit avant tome 5) |
| **Ω** | Végéta Ozaru (~2 500 000) |
| **Ω-** | Goku Ozaru (~1 800 000), Goku Kaio-Ken ×4 (~720 000) |
| **S** | **Végéta (250 000)**, **Goku (180 000)** |
| **A** | Thragg (mur relatif : il ne gagne pas, mais il coûte) |
| **B+** | Conquest, Omni-Man à son apogée, Battle Beast |
| **B** | Anissa, Lucan, Vidor, Viltrumites d'élite |
| **C** | Mark, Immortal, Viltrumites standards |
| **D** | Atom Eve (bridée), Gardiens, Allen (avant boost) |

**Écart Végéta / Conquest : environ ×40.** Ce n'est pas un combat. C'est une exécution ralentie par l'ennui.

### 4.3 Ce que les Saiyans ne peuvent PAS faire

C'est cette liste qui fabrique le récit. Elle doit être respectée avec rigueur.

0. **RAPPEL DE CANON VILTRUMITE.** Corps biologiquement indiscernables de l'humain, bâtis sur des atomes à propriétés variables ; ils captent l'énergie ambiante. **Ils se renforcent avec l'âge et surtout avec l'adversité — chaque blessure grave dont ils réchappent les rend plus forts.** Espérance de vie de plusieurs millénaires, le vieillissement ralentissant avec le temps. Uniformes de tissu, individualisés, **jamais de plaque**. Faiblesse connue : **les sons de très haute fréquence**, qui provoquent douleur, désorientation, perte d'équilibre, et à forte intensité des lésions neurologiques mortelles. Voir `00_CANON/LEXIQUE_ET_ORTHOGRAPHES.md`.

1. **Sentir un Viltrumite.** Aucun ki. Pour un Saiyan, un Viltrumite est un **trou dans la perception**. Ils sont donc surprenables — la seule chose qui les a jamais rendus surprenables de leur vie. Un scouteur affiche 0 face à Thragg ; Végéta croira d'abord à une panne, et c'est comme ça qu'il comprend.
2. **Être partout.** La Terre a 510 millions de km². Deux êtres, aussi puissants soient-ils, ne couvrent pas une planète. **C'est la faille que l'Empire va exploiter.**
3. **Frapper ce qu'ils ne peuvent pas atteindre.** On ne tue pas une politique. On ne détruit pas un embargo. On ne met pas KO le deuil de Debbie Grayson.
4. **Ne pas manger.** 15 000 à 25 000 kcal/jour en activité de combat. Pas de Bulma, pas de capsules, pas d'argent.
5. **Guérir vite.** Aucune capsule médicale, aucun senzu. Une blessure grave = des semaines. Chaque zenkai obtenu dans ce monde est un événement rare, payé par une convalescence racontée.
6. **Rentrer chez eux.** Aucun combat ne résout ça. Jamais.
7. **Comprendre ce monde.** Ils ne savent ni lire l'anglais, ni ce qu'est une devise, une élection, une assurance, un procès.

> **LINGUA FRANCA — à poser une fois, au chapitre 3, puis ne plus y revenir.** Les Saiyans parlent la langue commerciale imposée par l'Empire de Freezer à des milliers de mondes. Robot établit en dix jours que sa structure phonémique recoupe partiellement les langues indo-européennes — statistiquement improbable, ce qui *l'intéresse énormément*. En pratique, la communication passe par un interprète GDA les six premiers jours, puis Goku apprend l'anglais avec une vitesse anormale (mémoire musculaire saiyan appliquée au langage). **Il ne sait toujours pas le lire au tome 2.** C'est pour ça que Debbie lui lit la lettre.

### 4.4 Ce qui peut réellement les blesser

**Aucun Viltrumite isolé.** Pas même Thragg. Mais :

- **L'Empire coordonné.** Trente Viltrumites simultanés sur trente continents, chacun tenant une ville en otage. Les Saiyans peuvent en tuer trente. Ils ne peuvent pas en tuer trente *en même temps*. Chaque minute de trajet coûte deux cent mille vies. **C'est ça, l'impasse du tome 2, et aucune puissance ne la résout.**
- **L'épuisement.** Kaio-Ken soutenu, Ozaru prolongé, combats en chaîne sur plusieurs jours. Un Saiyan à sec est plus faible qu'un humain entraîné pendant plusieurs heures : température corporelle en chute, vision rétrécie, vomissements. Cet état est une vraie fenêtre de vulnérabilité, et l'Empire finira par le comprendre.
- **Les otages.** Sur Goku, ça marche immédiatement. Sur Végéta, ça ne marche pas — **et c'est pire**, parce que l'Empire va tester, et le test coûtera une ville.
- **Les armes conçues pour eux.** Voir section 6.3 : l'inhibiteur métabolique des Mauler, le matériel génétique du congélateur, les recherches de Robot sur la radiation Sigma.
- **Eux-mêmes.** Végéta contre Goku est, physiquement, le seul vrai combat du récit. Il arrive au tome 3.
  > **⚠ Précisé après le chapitre 11.** Le J11 les met face à face et **ce n'est pas ce combat** : Végéta vient corriger, pas savoir ; Kakarotte ne rend pas un coup et passe deux minutes à se placer devant des maisons. **Ce que le J11 démontre, c'est qu'ils ne peuvent pas s'affronter sur cette planète** — ce qui rend le tome 3 nécessaire au lieu de le remplacer. Ne jamais écrire, dans aucun tome, que le premier affrontement a eu lieu au tome 1.

### 4.5 Règles de mort

1. **Aucune résurrection. Jamais.** Pas de Dragon Balls, pas de Kaio, pas d'au-delà accessible. Goku ne le sait pas et agira longtemps avec l'insouciance de quelqu'un qui est déjà mort une fois et revenu. **Sa découverte de cette règle est le sommet émotionnel du tome 2, et elle vaut dix combats.**
2. **Toute blessure laisse une trace.** Registre en section 13.
3. **Décapitation, écrasement du crâne, destruction du cœur : irréversible pour tous, Saiyans compris.**
4. **Les civils meurent, et on les compte.** La GDA publie. La presse commente. Le chiffre devient un argument politique.

---

## 5. LES MOTEURS NARRATIFS

### 5.1 Moteur central — Que font-ils de cette puissance ?

Chaque tome pose la question sous un angle différent :

| Tome | La question |
|---|---|
| 1 | *Qu'est-ce qu'on vient de faire ?* — découverte, sidération, premier contact |
| 2 | *Qu'est-ce qu'on est prêts à faire ?* — l'Empire, la Coalition, l'impasse des otages |
| 3 | *Pourquoi est-ce qu'on se bat encore ?* — Végéta/Anissa, Goku/Debbie, le vide après la victoire |
| 4 | *Qu'est-ce qui reste quand on gagne tout ?* — le deuil, l'attachement, Mars |
| 5 | *Est-ce qu'on peut appartenir à un monde qu'on pourrait détruire ?* — l'intégration |

### 5.2 Moteur — L'ignorance *(remplace « la faim », v2.1)*

> **CORRECTION STRUCTURELLE.** La version 2.0 faisait de la faim le moteur du tome 1 : Goku chassant dans les Rocheuses, Végéta volant un restaurant. **C'est incompatible avec le régime de puissance.** Deux êtres qui rasent une ville ne chapardent pas, et ils sont l'un comme l'autre trop orgueilleux pour se limiter à ça. Rien ne les empêche d'entrer dans une ville et de prendre ce qu'ils veulent.

**La faim est rétrogradée au rang de physiologie** (R4), pas de moteur. Elle existe, elle est énorme, elle ne pose aucun problème : **personne ne leur refuse rien.** Ce n'est pas du vol, c'est **du tribut**, et un restaurant qui sert sans oser présenter l'addition est infiniment plus glaçant qu'un vol filmé.

**L'épuisement reste réel** (§4.4) mais change d'échelle : ce n'est pas une contrainte quotidienne, c'est la séquelle d'un engagement soutenu sur plusieurs jours. Leur endurance est vaste. Elle est finie. L'Empire finira par trouver ce plancher ; personne ne le trouve au tome 1.

**Le vrai moteur est l'ignorance.** Ils ne savent ni lire, ni où ils sont, ni ce qu'est ce monde, ni ce qu'est une devise, une élection, un procès — ni surtout s'il existe une voie de retour. **C'est la seule chose qu'ils ne peuvent pas prendre par la force.**

- **Goku** a besoin de savoir s'il existe une porte. C'est tout ce qui l'intéresse, et il ne sait pas encore que c'est urgent.
- **Végéta** a besoin de savoir ce que vaut ce monde, qui le dirige, et ce qu'on peut y conquérir. Et il refuse d'apprendre la langue — faire parler la langue de l'autre, c'est déjà céder.
- **La GDA est le seul fournisseur possible.** **C'est la première laisse de Cecil, et elle est faite d'information.**

### 5.3 Moteur — Le vide de Végéta

Végéta n'est pas motivé par la puissance. Il est motivé par **l'annulation de son humiliation**. Vendu enfant, il a servi le meurtrier de son père pendant vingt-cinq ans en souriant.

**Sa tragédie dans ce récit :** il obtient enfin ce qu'il a toujours voulu — être le plus fort de l'univers où il se trouve — et découvre que ça ne le remplit pas. Parce que Freezer est hors d'atteinte. Parce que sa vengeance lui a été volée par une porte dans le ciel. Parce que dans ce monde, **personne ne sait qu'il est un prince**, et il réalise que son identité entière reposait sur le regard d'un empire qui n'existe plus pour lui.

Sa réaction : reconstruire la peur à partir de zéro, par la démonstration. D'où Chicago. D'où Mars. D'où l'Ozaru.

> **Règle de caractérisation.** Végéta doit **se tromper**. Son orgueil l'aveugle. Il doit mépriser les Viltrumites, refuser d'apprendre d'eux, et se faire surprendre au moins une fois de façon coûteuse — pas physiquement, mais stratégiquement. Un Végéta qui analyse tout correctement en temps réel n'est plus Végéta.

### 5.4 Moteur — L'Ozaru

**Les deux le contrôlent.** Végéta parce qu'il l'a toujours maîtrisé. Goku parce que Végéta le lui enseigne — c'est un des rares moments de transmission entre eux, et c'est un moment glaçant, pas chaleureux.

**C'est donc une arme stratégique assumée, pas un accident.** Ce qui la rend mille fois plus effrayante pour le monde.

**Chronologie de la bombe :**
- **Jour 0** — La lune est un croissant décroissant si fin qu'elle est invisible. Personne n'y pense. C'est voulu.
- **Jour 3** — Végéta réalise que cette planète a une lune. La lune est nouvelle, donc invisible : **il ne la voit pas, il la lit** — un disque noir qui occulte les étoiles en dérivant, repéré de nuit et en altitude. Il ne dit rien. Il calcule la période. Il attend.
- **Jour 9** — Goku réalise aussi, avec horreur, parce qu'il se souvient d'avoir tué son grand-père. Il envisage de se raser la queue.
- **Jour 17** — Pleine lune.

**Le jour 17.** Végéta se transforme volontairement, en pleine bataille, au-dessus d'une agglomération. Conscient, maître de lui, méthodique. Le bilan est catastrophique. Ce n'est pas un accident : c'est un choix tactique froid, et il gagne.

**À partir de ce jour, Végéta n'est plus jamais un allié acceptable pour la Terre.** La GDA a la vidéo. Le monde a la vidéo.

**Contre-mesure inévitable :** détruire la Lune. Débat de conseil de sécurité entier — marées, agriculture, stabilité de l'axe terrestre, effondrement des écosystèmes côtiers. Deux chapitres du tome 2, chiffrés, sérieux. **Ils n'oseront pas.** Et ne pas oser est une décision qui les hantera.

### 5.5 Moteur — Mars

**Tome 4, moment pivot du récit entier.**

Végéta détruit Mars. D'un doigt. Devant les caméras de la Coalition des Planètes réunie en session, devant les télescopes du monde entier, devant Anissa.

**Pourquoi.** Ce n'est ni de la folie ni du caprice. C'est un **argument diplomatique**. La Coalition débattait de savoir s'il fallait classer les Saiyans comme espèce protégée, alliée, ou menace de niveau Viltrumite. Végéta a estimé que le débat prenait trop de temps.

**Conséquences, à tenir sur tout le tome 5 :**
- Perturbation orbitale mesurable ; le champ d'astéroïdes est déstabilisé, la NASA calcule des trajectoires d'impact sur Terre à horizon 40 ans.
- La Coalition suspend ses négociations avec la Terre et place le système solaire en quarantaine.
- Aux Nations Unies, le terme « génocide potentiel » est employé pour la première fois à propos d'un individu.
- **Anissa ne le condamne pas.** C'est ça qui les rapproche. Et c'est ça qui sépare définitivement Végéta de Goku.
- Goku ne parle plus à Végéta pendant onze semaines.

### 5.6 Moteur — Le silence sur Namek

Ni l'un ni l'autre ne sait ce qu'il est advenu de Namek, de Gohan, de Krillin, de Piccolo, de Bulma, de Dendé. Ils ont disparu au milieu d'une guerre.

**Goku porte ça comme une culpabilité.** Il a laissé son fils de cinq ans sur une planète avec Freezer. Ce n'est pas dit toutes les cinq pages : trois fois en dix chapitres, amené par un détail concret — un enfant dans une rue, une odeur, un ton de voix.

**Végéta porte ça comme une frustration.** Le seul objectif de sa vie entière lui a été arraché. Sa rage n'est pas contre ce monde. Elle est contre le vide.

**Le retour reste possible et non résolu jusqu'au tome 5.** Angstrom, Robot, la technologie de la Coalition : trois pistes, toutes réelles, toutes à un prix. Ne jamais fermer la porte, ne jamais l'ouvrir complètement.

---

## 6. GÉOPOLITIQUE

### 6.1 La GDA — Cecil Stedman

**Ce que Cecil comprend en quarante-huit heures :** il n'a pas d'arme, pas de prison, pas de levier familial. Il a trois choses, et il les note dans un mémorandum classé OMEGA au jour 4 :

> « Un : ils ne comprennent rien à ce monde, et ils ont besoin de quelqu'un qui le comprenne. Deux : l'un des deux se soucie de ce que les gens pensent de lui. Trois : ils se détestent mutuellement plus qu'ils ne nous détestent. Nous travaillerons sur les trois. »

**Sa ligne, à placer textuellement au tome 2 :** « Je ne vous demande pas d'être des héros. Je vous demande d'être prévisibles. »

**Directive de style interne, jour 19 :** « Et qu'on arrête de les appeler *les Saiyans* dans les rapports, comme s'ils étaient une seule entité. Ils sont deux. Ils ne pensent pas pareil. C'est peut-être la seule chose qui nous sauvera. »

### 6.2 Actifs mobilisés

- **Donald Ferguson** — liaison assignée à Goku. Sa décence est réelle, et c'est exactement ce qui rend la manipulation efficace. Il devient l'ami de Goku *et* il rapporte tout. Les deux sont vrais en même temps.
- **Robot / Rudolph Conners** — théorise correctement le ki en trois semaines, ce qui devrait inquiéter tout le monde. Il commence secrètement à modéliser comment le reproduire artificiellement. **Il a démissionné des Gardiens en mars, contre Cecil et contre la réhabilitation de Sinclair.** Il est dans le bâtiment au jour 1 sans y être obligé, et personne ne lui a demandé pourquoi — voir `00_CANON/ARBITRAGE_CANON_V3.md` §8.
- **Les Mauler Twins** — sous contrat, chargés de perturber la production de ki. Ils échouent, mais produisent un **inhibiteur métabolique** qui prive un Saiyan de la capacité à digérer. Une arme de famine. Cecil la stocke sans l'utiliser.
- **Sinclair et le programme Reanimen** — la GDA récupère sang, fragments d'armure et cheveux sur le champ de bataille du jour 0. **Il y a du matériel génétique saiyan dans un congélateur à partir du jour 6.** Le plus gros fusil de Tchekhov du récit ; il tire au tome 4.

### 6.3 L'Empire Viltrumite

**Moins de cinquante Viltrumites purs vivants** après le fléau. L'Empire est un colosse creux qui survit par la terreur et par le secret absolu de sa faiblesse démographique. Chaque individu est irremplaçable.

C'est pourquoi la mort de Conquest n'est pas une nouvelle militaire. C'est une **crise existentielle**.

**Phases :**
- **Phase 1 (jours 0-13)** — Rapport de Conquest transmis in extremis, puis silence radio. L'Empire apprend l'existence d'une race inconnue disposant d'une arme à énergie projetée qui perce le tissu viltrumite.
- **Phase 2 (jour 13)** — **Anissa.** Envoyée seule, en évaluation, pas en assaut. Elle vient **avant** l'Ozaru, et c'est capital : l'Empire construira toute sa doctrine sur une évaluation incomplète. Ce qu'elle rapporte au jour 13 ne contient pas le jour 17. Elle teste, encaisse, comprend en quatre-vingts secondes qu'elle ne peut pas gagner — et **choisit de se retirer**. C'est parfaitement cohérent avec l'espèce : ils sont trop peu nombreux pour mourir bêtement. Elle repart avec une ligne de sang séché sur la tempe qu'elle ne nettoie pas.
- **Phase 3 (tome 2)** — Observation prolongée. Un vaisseau furtif en orbite haute, ordre de non-intervention. Des centaines d'heures de combat filmé, analysées image par image.
- **Phase 4 (tome 2, fin)** — **La stratégie des trente.** L'Empire renonce définitivement à vaincre les Saiyans au combat et bascule sur la seule doctrine viable : la saturation. Trente Viltrumites, trente continents, trente villes en otage. C'est l'impasse qui clôt le tome 2.

**Thragg** n'apparaît physiquement qu'au tome 3. Sa présence se construit d'abord par les silences des autres Viltrumites. Quand il arrive, **il perd** — mais il coûte à Végéta un œil, un bras et quatre mois de convalescence, et il repart vivant.

### 6.4 La Coalition des Planètes — Allen l'Alien

Allen évalue les mondes par *Level Threat Assessment*. L'arrivée des Saiyans fait passer la Terre du Niveau 5 à un statut que son système ne sait pas coter. Il vient voir. En personne.

**Ce qu'il apporte au récit :** sa respiration. Chaleureux, drôle, désarmant, et parfaitement sérieux sur le fond. Il glisse des informations catastrophiques dans des phrases légères.

- **Sa rencontre avec Goku** est un sommet du tome 2 : deux êtres fondamentalement bienveillants dans un univers qui ne l'est pas.
- **Sa rencontre avec Végéta** est glaciale. Allen le classe, à voix haute, dans la même catégorie que les Viltrumites. Végéta ne trouve rien à répondre, et il y repense pendant deux tomes.

**Ce qu'il veut :** recruter. Une flotte, des ressources, une guerre à mener. C'est l'offre concurrente de celle de Cecil et de celle de l'Empire. Trois laisses différentes.

**Après Mars :** la Coalition suspend tout et met le système solaire en quarantaine. Allen est le seul à voter contre, et il perd.

### 6.5 Le monde civil

Ce monde a des journaux, des marchés, des élections, des réseaux sociaux, des assurances. Ne jamais l'oublier.

- Le marché immobilier du Midwest s'effondre de 34 % en trois semaines. Les compagnies d'assurance invoquent la clause d'acte de guerre extraterrestre et refusent de payer.
- Le mot **« saiyan »** entre dans le langage courant, mal orthographié, comme adjectif péjoratif.
- Une secte se forme autour de Goku — **Les Témoins de l'Orange**. Il ne comprend pas pourquoi et ça le met profondément mal à l'aise.
- Auditions au Congrès. Cecil ment sous serment.
- L'**Association des Familles de State Street**, présidée par une survivante de trente-quatre ans qui a perdu ses deux enfants, poursuit la GDA. Elle deviendra une voix importante du tome 5.
- Une fillette de neuf ans écrit une lettre à Goku. Elle est publiée. **Il ne sait pas la lire.** Debbie la lui lit.

---

## 7. FICHES DE VOIX

Format : noyau / fracture / voix / interdits / calibrage.

---

### 7.1 SON GOKU — KAKAROTTE

**Noyau.** Ce n'est pas un idiot. C'est une intelligence exclusivement appliquée au combat et à la lecture des gens, doublée d'une ignorance totale du reste. Il ne raisonne pas en bien et mal. Il raisonne en **ce qui doit être arrêté** et **ce qui peut encore grandir**.

**Fracture.** Il a abandonné son fils de cinq ans sur une planète en guerre. Il n'a aucun moyen de rentrer. Et il ignore encore que dans ce monde, personne ne revient. Goku a toujours combattu avec un filet de sécurité métaphysique. Il n'en a plus, et il ne le sait pas.

**Voix.**
- Phrases courtes, syntaxe simple, **jamais bête**. Il va droit à l'os.
- Questions directes qui mettent les gens mal à l'aise parce qu'elles sont trop honnêtes : « Pourquoi tu mens à ton chef ? », « Il te fait peur, hein ? »
- Il tutoie tout le monde, présidents compris.
- Il rit dans les mauvais moments, par excitation nerveuse, et ça choque.
- **Il ne dit jamais « je vais te tuer ».** Il dit « je vais t'arrêter ». Quand il finit par dire l'autre phrase, au tome 4, le sol doit se dérober sous le lecteur.
- Registre alimentaire permanent, **jamais gag** : c'est un problème logistique réel.

**Interdits.** Pas de niaiserie. Pas d'onomatopée écrite. Pas de leçon de morale — Goku n'en donne jamais, il agit et laisse les autres conclure. Il ne pleure pas facilement ; quand il pleure, décrire ses mains, pas ses larmes.

**Calibrage temporel — critique.** Au jour 0, Goku ne ressent **aucune culpabilité**. Il ressent de la **confusion**. Ces gens auraient dû se relever. La culpabilité met des semaines à se former, par accumulation de détails concrets, pas par révélation. **L'excuse à Debbie n'arrive pas au jour 2. Elle arrive au jour 40 environ**, et elle arrive parce qu'il a enfin compris que Mark ne reviendra pas.

**Voix juste :**
> — Ton ami là-bas, le grand. Il a arrêté de respirer il y a dix secondes.
> Cecil a levé les yeux du dossier.
> — Vous ne pouvez pas savoir ça.
> — Si. Je le sentais, et maintenant je le sens plus. (Un temps.) C'est comme une lumière dans une pièce. Quand elle s'éteint, on le remarque.
> — Et vous n'allez rien faire ?
> — Il est mort.
> Il a haussé une épaule, sans dureté, comme on constate la météo.
> — Y'a rien à faire pour les morts. C'est pour ça que je préfère arriver avant.

**Voix ratée (à ne jamais écrire) :**
> — Je suis vraiment désolé pour ce que j'ai fait. Je réalise maintenant l'ampleur de mes actes et je vais tout faire pour me racheter.

*Pourquoi c'est raté : Goku ne parle pas en abstractions morales, et à ce stade il ne « réalise » rien du tout.*

---

### 7.2 VÉGÉTA, PRINCE DES SAIYANS

**Noyau.** L'annulation de l'humiliation. Chaque acte de cruauté est une tentative de prouver qu'il n'a jamais été une victime.

**Fracture.** Personne ici ne sait qu'il est un prince. Son titre ne vaut rien. Il découvre que son identité entière reposait sur le regard de Freezer.

**Voix.**
- Registre **soutenu, précis, cinglant**. Vocabulaire plus riche que celui de Goku. Il utilise des mots exacts.
- **Il jure.** Sec, court, jamais gratuit. Ce n'est pas de la vulgarité, c'est du mépris condensé.
- Il ne crie presque jamais. Sa colère est **froide et articulée**. Le lecteur doit sentir la température baisser, pas monter.
- Il appelle Goku **« Kakarotte »**, toujours, sans exception. Presque personne d'autre n'a de nom pour lui.
- Il compare tout à Freezer, et **tout est en dessous**. C'est sa façon de rester le protagoniste de sa propre tragédie.
- **Il ne ment jamais.** C'est en dessous de lui. C'est aussi ce qui le rend exploitable.

**Interdits.** Pas de tsundere. Pas de « je le fais pour vous mais je ne l'admettrai pas ». Pas d'auto-analyse lucide — Végéta ne se comprend pas lui-même, c'est le lecteur qui doit le comprendre à travers ses actes. À ce point de l'arc Namek, c'est **un criminel de guerre non repenti** qui a personnellement éradiqué des populations entières. S'il devient intéressant, c'est par lucidité sur les autres, jamais par gentillesse.

**Voix juste :**
> — Vous avez tué onze mille personnes.
> — Non.
> Végéta n'a pas relevé la tête. Il finissait son assiette.
> — J'en ai tué onze mille *ici*. Ne confondez pas votre comptabilité avec l'histoire. Sur Shikk, j'ai stérilisé un continent en quarante minutes pour respecter un calendrier de livraison. On m'a félicité. On m'a donné une nouvelle armure.
> Il a reposé sa fourchette avec un soin d'orfèvre.
> — Ce qui vous dérange, ce n'est pas le nombre. C'est que pour la première fois, vous ayez eu à le regarder.

**Voix ratée :**
> — Elle avait peur à la fin. Elle le cachait bien, mais elle a choisi de partir plutôt que de mourir. C'est la première de cette race qui a montré un minimum de cervelle.

*Pourquoi c'est raté : c'est un rapport d'analyse, pas une réplique. Végéta ne fait pas de synthèse tactique à voix haute pour informer le lecteur. Il dirait plutôt : « Elle est partie. » Puis, dix minutes plus tard, sans transition : « Kakarotte. Combien tu crois qu'ils sont ? »*

---

### 7.3 ANISSA

**Noyau.** Une Viltrumite qui croit sincèrement que l'Empire apporte l'ordre. Elle n'est ni sadique ni menteuse. Elle est **convaincue**, et c'est infiniment plus dérangeant.

**Voix.** Économe. Descriptive. Elle décrit ce qu'elle voit sans le colorer. Elle pose des questions courtes et attend vraiment la réponse. Elle ne se vante pas et ne menace pas — elle **constate**, ce qui produit le même effet.

**Ce qui la relie à Végéta.** Fascination guerrière mutuelle. Elle voit en lui le seul être qu'elle a rencontré qui ne rampe pas et qui ne se justifie pas. Il voit en elle la première personne de ce monde qui ne le regarde ni avec terreur ni avec dégoût, mais avec **évaluation** — exactement comme lui regarde les autres.

**Progression sur les tomes 3-4 :**
1. Elle revient pour le tuer. Elle échoue. Il la laisse partir — pas par pitié, par curiosité.
2. Elle revient pour comprendre. Ils parlent. Ils ne sont d'accord sur rien sauf sur l'essentiel : que les faibles n'ont aucun droit particulier.
3. **Mars.** Elle assiste à la destruction d'une planète et ne le condamne pas. C'est le point de bascule.
4. Elle trahit l'Empire — non par amour, mais parce qu'elle conclut que l'Empire s'est trompé sur la nature de la force.

**Interdit absolu.** Aucune scène où Anissa « adoucit » Végéta. Ils ne se rendent pas meilleurs. Ils se **confirment** l'un l'autre, et c'est terrifiant. Debbie le comprendra la première, et le dira à Goku.

---

### 7.4 DEBBIE GRAYSON

Le personnage le plus humain du récit et le seul qui ne se batte jamais. Alcoolique en devenir.

**Sa position exacte, corrigée au canon.** Elle n'est pas veuve : **Nolan est vivant**, détenu par l'Empire viltrumite hors de la Terre. Il n'existe aucun moyen de le joindre, aucun moyen de lui apprendre que Mark est mort, et aucune certitude qu'il l'apprenne un jour. Et elle n'est pas mère de rien : **elle a Oliver**, belle-mère légale et mère de fait depuis la mort d'Andressa.

Ce qui lui reste, au jour 7 : un fils mort sans corps, un mari vivant sans adresse, et dans sa maison **un enfant de deux ans dans un corps de neuf, amputé du bras gauche, qui l'appelle par son prénom.**

**Sa force.** Elle refuse à la fois le pardon et la haine. Elle choisit une troisième chose que personne d'autre ne sait faire : **l'exigence**. « Ne deviens pas pire que ce que tu as déjà fait. Prouve-le. Pas avec des mots. »

**Voix.** Basse, usée, précise. Elle ne fait pas de discours. Elle pose des questions qu'on ne peut pas esquiver. Elle jure quand elle est fatiguée.

**Trajectoire Debbie / Goku — lien maternel, jamais autre chose.**
- **Tome 1** — la confrontation, puis la journée chez elle : il vient demander des vêtements à la mère du garçon qu'il a tué. C'est monstrueux et humain en même temps, et c'est la meilleure idée du récit. Elle lui donne les combinaisons de Nolan — **les affaires d'un homme vivant**, qu'elle a gardées pliées pendant des mois pour le jour où il rentrerait. Elle sait exactement ce qu'elle fait, et elle s'en veut.
- **Tome 2** — c'est elle qui lui apprend que Mark ne reviendra pas. Pas Cecil. Pas Végéta. Elle. Et il s'effondre dans sa cuisine, et elle ne le console pas.
- **Tome 3** — elle est la seule personne au monde dont Goku accepte un ordre.
- **Tome 4** — après Mars, c'est elle qui lui dit ce que Végéta est devenu et ce qu'il risque de devenir.
- **Tome 5** — elle refuse publiquement de témoigner contre lui devant la commission. Ça lui coûte tout.

**Interdit.** Aucune ambiguïté romantique. Aucune scène de réconfort facile. Elle ne le pardonne jamais complètement, et le récit ne doit jamais suggérer qu'elle le devrait.

**Elle ne rencontre jamais Végéta.** Ne pas céder à la tentation de cette scène avant le tome 5. Son absence vaut mieux, et quand elle arrive enfin, elle doit tenir en quatre répliques.

---

### 7.5 CECIL STEDMAN

**Noyau.** Un homme qui a calculé, il y a très longtemps, que sa propre damnation était un prix acceptable. Il ne se ment pas. Il ne demande pas d'absolution.

**Voix.** Sec, rapide, sarcasme utilitaire. **Il ne finit pas ses phrases quand la conclusion est évidente.** Il dit « fiston » aux gens qu'il s'apprête à sacrifier.

**Application de la règle R1 :** Cecil n'annonce jamais ses stratégies. Il demande un budget. Il commande un rapport. Il change de sujet. Le lecteur déduit.

**Sa meilleure scène possible :** Cecil face à Végéta, seul, sans arme, sans transporteur d'urgence activé — et il gagne l'échange. Pas par la force. Parce qu'il a compris quelque chose sur Végéta que Végéta ne s'est jamais dit à lui-même.

---

### 7.6 SECONDAIRES

- **Amber Bennett.** Colère nette, pas de filtre. **Canon : elle a rompu avec Mark bien avant, elle est en couple avec quelqu'un d'autre, et elle est restée proche de Mark et d'Eve.** Elle n'est donc pas l'ex jalouse : c'est l'amie qui porte le deuil, et elle est dans cette maison pour Mark. Elle est la seule à dire à Debbie ce que tout le monde pense : que donner les affaires de Nolan au meurtrier de Mark, c'est une folie. Elle a raison, et elle a tort.
- **William Clockwell.** Il fume trop. Il fait les cent pas. Il représente les gens qui n'ont aucun pouvoir et qui doivent quand même vivre à côté de ça.
- **Donald Ferguson.** Loyauté sincère, doutes croissants. Ami de Goku et informateur de Cecil, simultanément et sincèrement.
- **Robot.** Purement analytique. Le seul qui comprenne le ki. Il commence à le modéliser. Fusil de Tchekhov n°2.
- **Allen l'Alien.** Voir 6.4.
- **Battle Beast.** Cherche une mort au combat. Il apprend l'existence de Végéta et traverse la galaxie. Leur duel au tome 3 est un morceau de bravoure sans aucun enjeu politique : deux orgueils purs, de la viande et de la fierté. **Végéta lui accorde la mort qu'il voulait, et c'est la seule chose gentille qu'il fera de tout le récit** — sauf que ce n'est pas de la gentillesse, c'est du respect professionnel.
- **Angstrom Levy.** Il a les sept secondes. Il cherche les Saiyans non pour les combattre mais parce qu'ils prouvent que sa méthode fonctionne — et parce qu'il veut refermer la brèche avant que quelque chose de pire ne la trouve. *Quelque chose de pire l'a déjà trouvée.*

---

## 8. GRAMMAIRE DES COMBATS

Le combat n'est jamais le suspense. Il est la **démonstration**. Il faut donc l'écrire autrement qu'un shōnen.

1. **Ancrer géographiquement.** Nom de rue, nom d'immeuble, altitude. Le lecteur doit pouvoir dessiner.
2. **Le point de vue est celui du plus faible.** Un combat vu depuis Végéta est ennuyeux, parce que Végéta s'ennuie. Vu depuis Conquest, depuis Mark, depuis un caméraman d'hélicoptère à deux kilomètres, il devient insoutenable. **C'est la technique principale du récit.**
3. **Trois phases** : la lecture (évaluation mutuelle), l'escalade (chacun découvre une capacité de l'autre), la résolution (quelqu'un exploite une erreur précise et nommable).
4. **Décrire les effets, pas les techniques.** Pas « il tira un Kamehameha ». La posture, la charge, la lumière sur les surfaces autour, ce que ça fait à l'air, et surtout le **bruit d'après**.
5. **La douleur a une texture.** Une côte cassée n'est pas « une douleur vive » : c'est une gêne à l'inspiration profonde qui devient un couteau à la torsion.
6. **Bilan chiffré en fin de séquence**, en un paragraphe court, presque administratif. C'est ce qui sépare ce récit d'un shōnen.
7. **Le silence est une arme.** Un combat sur trois se termine sans un mot.

> **⚠ CETTE §8 NE COUVRE QUE LES COMBATS — et c'est un trou.** Un dieu qui frappe est un événement ; **un dieu assis est une menace permanente.** La grammaire du corps au repos est dans `99_OUTILS/LE_POIDS_DES_CORPS.md` : disproportion **plus** indifférence, quatre registres, deux ou trois effets par scène sur une seule échelle, et **le Saiyan ne remarque jamais ce qu'il produit.**
8. **Ne jamais faire durer artificiellement.** Si Végéta peut finir en quatre secondes, il finit en quatre secondes — sauf s'il choisit de ne pas le faire, et alors ce choix est **le sujet de la scène**.

---

## 9. GRAMMAIRE DES DIALOGUES

- **Écrire le désir avant la réplique.** Chaque personnage veut quelque chose de précis dans chaque scène.
- **Personne ne dit ce qu'il pense en premier.** Sauf Goku.
- **Répliques d'exposition interdites.** L'information passe par le conflit ou ne passe pas.
- **Test de retrait des incises** : sans « dit-il », on doit reconnaître qui parle.
- **Incises sobres** : « dit », « a répondu », ou rien. Jamais « rétorqua-t-il sardoniquement ».
- **Les silences se mesurent.** « Trois secondes. » vaut mieux que « un long silence ».
- **Le sous-texte porte les scènes politiques.** Cecil et Allen négocient six pages sans jamais nommer l'objet de la négociation.
- **Les Viltrumites ne récitent pas de rapports.** Anissa ne dit pas « évaluation terminée, les sujets sont supérieurs à Conquest ». Elle dit, à quelqu'un qu'elle respecte : « Je n'ai pas pu. » Et le silence qui suit dit tout le reste.

---

## 10. STRUCTURE EN CINQ TOMES

### TOME 1 — « VINGT-DEUX MINUTES » (ch. 1-20)
*Découverte, sidération, premier contact. Vingt jours.*

La question : **qu'est-ce qu'on vient de faire ?**

| Ch. | Contenu |
|---|---|
| 1-2 | Les sept secondes. Les vingt-deux minutes. Focalisation Conquest, puis un caméraman. |
| 3 | Le silence d'après. Cecil arrive sur le cratère. Le premier chiffre. |
| 4-5 | **Les retrouvailles.** Ils s'évaluent. Végéta comprend que Freezer n'est pas derrière lui. **Le pacte : une prémisse commune, deux buts incompatibles** — il veut un siège, Goku veut une porte. Premier contact radio. |
| 6 | Doctrine OMEGA. Le congélateur. |
| 7-8 | Debbie exige de parler à celui qui a tué son fils. La confrontation dans le désert. **Il ne s'excuse pas.** Il ne comprend pas encore ce qu'on lui reproche. |
| 9-11 | Végéta réalise pour la Lune. Il ne dit rien. **J11 : il vient corriger Kakarotte au-dessus d'une banlieue de Chicago. Deux minutes. Kakarotte ne rend pas un coup.** *(L'entraînement au-dessus du Pacifique est abandonné — voir `03_PLAN/TOME_1.md`.)* |
| **11** | **Végéta vient corriger Kakarotte au-dessus d'une banlieue de Chicago. Le mot entre dans la langue, crié trois fois.** |
| 12-13 | Auditions au Congrès. Cecil ment. **Le monde évite le mot ; le vocabulaire de l'agence gagne.** |
| 14-15 | **Jour 13.** Anissa. Haute orbite. Le monde regarde en direct. Elle se retire. Elle repart sans avoir vu l'Ozaru. |
| 16 | Chapitre entier en focalisation Végéta. Il décide. |
| 17-18 | **Ozaru.** Pleine lune. Le bilan. |
| 19-20 | La journée chez les Grayson. Il vient demander des vêtements. Elle les lui donne. Fin de tome sur une porte qui se referme. |

### TOME 2 — « TRENTE CONTINENTS » (ch. 21-45)
*L'Empire, la Coalition, l'impasse.*

La question : **qu'est-ce qu'on est prêts à faire ?**

- **Protocole d'accès GDA.** Cartes, archives, interprète, et l'accès aux travaux sur le retour. Goku signe sans pouvoir le lire. **La laisse est faite d'information.**
- Allen l'Alien. Deux rencontres miroir.
- Le débat sur la Lune. Deux chapitres de conseil de sécurité, chiffrés. Ils n'osent pas.
- **Debbie apprend à Goku que Mark ne reviendra pas.** Il s'effondre dans sa cuisine. Elle ne le console pas. C'est le sommet du tome.
- Traque de Végéta. Il gagne militairement chaque affrontement et perd du terrain à chaque fois.
- **La stratégie des trente.** L'Empire renonce à vaincre et bascule sur la saturation. Trente Viltrumites, trente villes en otage. Les Saiyans peuvent en tuer trente ; ils ne peuvent pas en tuer trente en même temps.
- Fin de tome : ils choisissent. Le choix coûte deux cent mille vies, et il n'existait pas de meilleure option.

### TOME 3 — « CE QUI RESTE APRÈS LA VICTOIRE » (ch. 46-70)
*Thragg, Battle Beast, le vide.*

La question : **pourquoi est-ce qu'on se bat encore ?**

- **Thragg.** Il perd. Il coûte à Végéta un œil, un bras et quatre mois de convalescence racontée. Il repart vivant, et c'est pire.
- Battle Beast vs Végéta.
- **Végéta contre Goku.** Le seul vrai combat du récit. Il ne se conclut pas.
- Anissa revient pour tuer. Elle échoue. Elle revient pour comprendre.
- Le premier zenkai de Goku, payé par six semaines de lit.
- Angstrom Levy et les sept secondes.

### TOME 4 — « MARS » (ch. 71-95)
*Attachements, conséquences, rupture.*

La question : **qu'est-ce qui reste quand on gagne tout ?**

- Végéta / Anissa : la fascination devient autre chose. Ils ne s'adoucissent pas mutuellement. Ils se confirment.
- Goku / Debbie : le lien maternel se scelle. Amber, William, la maison.
- **Le clone.** Ce qui était dans le congélateur au chapitre 6 sort ici.
- **Mars.** Détruite d'un doigt, devant la Coalition. Quarantaine du système solaire. Goku ne parle plus à Végéta pendant onze semaines.
- Anissa trahit l'Empire.

### TOME 5 — « APPARTENIR » (ch. 96-120)
*L'intégration.*

La question : **peut-on appartenir à un monde qu'on pourrait détruire ?**

- Commission internationale sur le statut des Saiyans. Debbie refuse de témoigner contre Goku. Ça lui coûte tout.
- L'Association des Familles de State Street.
- Végéta et Anissa hors de toute juridiction. Une principauté de fait.
- **Le retour vers Namek devient possible.** Trois voies, trois prix. Le choix final n'est pas un combat.
- Debbie rencontre enfin Végéta. Quatre répliques. Pas une de plus.

---

## 11. THÈMES

1. **La puissance ne résout rien de ce qui compte.**
2. **La miséricorde comme luxe.** Goku épargne parce qu'il a toujours pu se le permettre. Ici, épargner tue des gens.
3. **Ce que vaut un titre là où personne ne le reconnaît.**
4. **Le prix comptable de tout ça.** Quelqu'un tient toujours la liste. Le plus souvent, c'est une femme que personne n'écoute.
5. **La conquête vue de l'intérieur.** Végéta et les Viltrumites ne sont pas des monstres exotiques. Ce sont des fonctionnaires d'un système qui a normalisé le génocide. C'est plus effrayant.
6. **Deux réponses au même vide.** Goku cherche un lien. Végéta cherche un trône. Aucun des deux ne trouve ce qu'il cherche, et ils s'en aperçoivent au même moment.

---

## 12. RÉCAPITULATIF DES ERREURS À NE PLUS COMMETTRE

*Liste dérivée des premières versions. À relire avant chaque chapitre.*

- ❌ Terminer un chapitre par un résumé de ce qui vient de se passer.
- ❌ Faire dire à un personnage l'analyse que le lecteur devrait faire seul.
- ❌ Donner à Végéta une lucidité totale sur sa propre psychologie.
- ❌ Faire ressentir à Goku de la culpabilité avant qu'il ait compris que la mort est définitive ici.
- ❌ Écrire les Viltrumites comme des transmetteurs de rapports.
- ❌ Adoucir un personnage pour le rendre sympathique.
- ❌ Oublier que Goku ne sait pas lire.
- ❌ Oublier que la Terre a une lune et que Végéta a une queue.
- ❌ Faire durer un combat que le vainqueur pourrait finir immédiatement, sans que ce choix soit le sujet.
- ❌ Écrire une scène de combat depuis le point de vue du plus fort.

---

## 13. JOURNAL D'ÉTAT DU MONDE

*À mettre à jour après chaque chapitre. Le modèle qui reprend le projet lit cette section en priorité.*

**Date récit :** Jour 0, 16 h 47 (pré-chapitre 1)

| Item | État |
|---|---|
| Morts cumulés | 43 (Conquest, avant l'arrivée) |
| Localisation Goku | en transit |
| Localisation Végéta | en transit |
| Queue Goku | intacte |
| Queue Végéta | intacte |
| Ki Goku | plein (post-capsule, zenkai actif) |
| Ki Végéta | plein (post-sommeil) |
| Blessures Goku | aucune |
| Blessures Végéta | armure fissurée omoplate gauche |
| Phase lunaire | croissant décroissant très fin, quasi invisible — **pleine lune à J+17** |
| Ce que sait Goku de la mort définitive | rien |
| Ce que sait la GDA | rien |
| Ce que sait l'Empire | rien |
| Ce que sait la Coalition | rien |
| Statut Namek | inconnu des deux |
| Chapitres écrits | 0 |
| Promesses posées non tenues | — |

---

## 14. CHECKLIST AVANT PUBLICATION D'UN CHAPITRE

- [ ] Aucune phrase ne pourrait apparaître dans un autre roman.
- [ ] Chaque personnage voulait quelque chose de précis dans chaque scène.
- [ ] Personne n'a dit ce qu'il pensait vraiment (sauf Goku).
- [ ] Le chapitre ne se termine pas par un résumé.
- [ ] La faim, la fatigue ou une blessure ancienne apparaît au moins une fois.
- [ ] Aucun chiffre de puissance dans la prose.
- [ ] Les dialogues sont identifiables sans incises.
- [ ] Toute destruction a un chiffre et une conséquence différée.
- [ ] Aucun personnage n'a agi contre son intérêt pour arranger l'intrigue.
- [ ] Le journal section 13 est à jour.
- [ ] Rien ne contredit les sections 1 à 6.
