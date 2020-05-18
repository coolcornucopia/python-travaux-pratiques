```
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
```
from [asciiart.eu](https://www.asciiart.eu/animals/reptiles/snakes)

Travaux pratiques sur Python :snake: Première partie
====================================================
[Python](https://fr.wikipedia.org/wiki/Python_(langage)) est le nom d'un **langage de programmation**, très utilisé dans beaucoup de domaines: internet, intelligence artificielle, analyse de données, électronique[^1]... et MineCraft[^2]!
[^1]: Python pour l'électronique avec [MicroPython](https://micropython.org).
[^2]: Exemples de [Python avec MineCraft ](https://www.instructables.com/id/Python-coding-for-Minecraft/).

Le but de ces travaux pratiques ("TP") est que tu apprennes **quelques notions de programmation** comme les chaînes de caractères, les variables, les listes, les conditions, les boucles, les classes... et cela, **tout en t'amusant et en découvrant le formidable langage Python** :smile:

Il n'y a aucune urgence à tout faire, **prends le temps qu'il faut** pour découvrir ce formidable langage, modifie les exemples pour les rendre plus jolis et surtout **amuse toi**!

Commençons...  :smile:

> Sommaire
== INSERER LE SOMMAIRE ICI ==



# Découvre les mots clés de Python
## Ton premier programme dans un éditeur de texte
Afin d'écrire tes premiers programmes, tu vas utiliser l'éditeur de texte **"IDLE"**, celui par défaut en Python.
- [ ] Ouvre le menu **"démarrer"** en bas à gauche de l'écran, recherche et lance l'application **"IDLE (using Python-3.x)"**. Une fenêtre s'ouvre à l'écran.

Tu vas écrire ton 1er programme Python avec la fonction `print()` qui permet d'afficher un message.
- [ ] Entre le texte de la ligne suivante (tu peux le copier/coller ou le saisir au clavier):
```python
print('Bonjour Python!')
```
- [ ] Va dans le menu **"Run"** et choisis **"Run Module"** (ou bien appuie simplement sur la **touche F5**): l'éditeur de texte te demande de sauvegarder ton premier programme, réponds **"OK"** et enregistre le dans le répertoire **"Documents"** avec le nom **"tp1.py"**. Une seconde **fenêtre "Python 3.x.y Shell"** s'est ouverte: c'est elle qui affichera le résultat de ton premier programme. Tu peux d'ailleurs retrouver le message **"Bonjour Python!"** dedans. :clap: Bravo, tu as réussi(e), tu es une star :star:!
- [ ] Avant d'aller plus loin, organisons ton espace de travail en plaçant ces deux fenêtres comme il faut sur l'écran. Pour cela:
    - [ ] Clique dans la **fenêtre "Python 3.6.8 Shell"**, ensuite, appuie sur la **touche "windows"** de ton clavier et sans la relâcher appuie sur la **flèche de droite du clavier  :arrow_right:**: la fenêtre va automatiquement se mettre sur la moitié droite de l'écran.
    - [ ] Clique ensuite dans la première fenêtre qui doit maintenant s'appeler "tp1.py", ensuite appuie sur la **touche "windows"** et sans la relâcher appuie sur la **flèche de gauche du clavier :arrow_left:**: la fenêtre va automatiquement se mettre sur la moitié gauche de l'écran. :tada: Bravo :tada: Tu peux ainsi voir en même temps ton programme à gauche et son résultat à droite, c'est pratique! :smile:!
    - [ ] Clique enfin dans cette fenêtre que tu es en train de lire, on va la positionner aussi à droite comme cela tu pourras la lire en même temps que tu codes (**touche "windows"** et sans la relâcher appuie sur la **flèche de droite du clavier :arrow_right:**).

Nous venons de découvrir la fonction `print()`, qui permet d'afficher un message: une fonction commence toujours par son nom (`print` ici). Ensuite, elle contient un ou plusieurs paramètres entre parenthèses. Le message est ici l'unique paramètre, on appelle d'ailleurs ce message **"une chaîne de caractères"** car elle commence et se termine par des guillemets simples `'` ou double `"`, mais moi je préfère les guillemets simples :smile:.

- [ ] Tu peux d'ailleurs t'amuser à modifier ce message, ajouter d'autres lignes `print()` et appuyer sur **F5** pour voir le résultat. Par exemple, copie/colle le programme ci-dessous qui te montre comment afficher un **message de plusieurs lignes** avec `'''`, des **caractères spéciaux** comme les guillemets simples `\'` ou doubles `\"` ou le caractère `\\` et à changer de lignes avec `\n`. Appuie sur **F5** pour voir le résultat:
```Python
print('Bonjour Python!')
print('''
                           ____
  ________________________/ O  \___/
 <888888888888888888888888_____/   \
''')
print('Je n\'ai même pas peur de toi :-)...')
print('car je sais afficher les caractères spéciaux')
print('comme \', \" et \\ et même changer de ligne\nTrop fort!')
```
C'est super le langage :star: Python :star: !


- [ ] Au fait, je dois t'avouer quelque chose :stuck_out_tongue_winking_eye:... en écrivant toutes ces lignes pour toi, j'ai découvert un bug dans mon programme qui m'a donné du fil à retordre (ça veut dire que j'ai eu du mal à le corriger): Je pensais que `'''` était suffisant pour afficher des grands dessins... mais non... en fait, pour pouvoir afficher vraiment tous les dessins, même ceux qui contiennent `'''` ou avec des lignes se terminant par `\` (comme pour la bouche du python de tout à l'heure), et bien il faut ajouter un petit `r` juste devant les 3 premiers guillemets qui deviennent donc `r'''`, regarde dans les 3 exemples ci-dessous pour mieux comprendre:

```Python
# Exemple sans le 'r', la phrase "coucou..." n'est pas
# sous le python alors que c'est ce qu'on veut faire...
print('''
                           ____
  ________________________/ O  \___/
 <888888888888888888888888_____/   \
coucou le beau Python
''')

# Exemple avec le 'r' juste avant les 3 premiers guillemets,
# et là, c'est OK
print(r'''
                           ____
  ________________________/ O  \___/
 <888888888888888888888888_____/   \
coucou le beau Python
''')
```

Donc, et bien toi et moi savons maintenant que pour afficher correctement les dessins en **Ascii Art**, il faut utiliser `r'''`, c'est cool d'apprendre :smile:.

:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: pourrais-tu s'il te plaît, créer un programme qui affiche ton prénom et ton sport préféré sur deux lignes différentes puis qui affiche le dessin du grand python tout en haut de cette page. J'aimerais trop que tu me montres ta super création! Et donc, il faut que tu l'enregistres pour pouvoir me la montrer plus tard. Pour cela, rien de plus simple, va dans le menu **File** et choisis **Save As...** et enregistre ta création dans le répertoire **"Documents"** avec le nom  **"premier_programme.py"**. Si tu as besoin d'aide, demande moi :smile:.


## Les variables pour stocker et combiner les données
Les variables sont des sortes de *boites contenant des choses* :package: (nombres, chaînes de caractères, listes...) et ayant un nom, qu'on peut utiliser plusieurs fois dans son programme et ainsi on peut utiliser plusieurs fois le contenu de la boite, on peut même "combiner" les contenus des boites pour faire d'autres boites... bon, si je ne suis pas clair, poursuivons avec un exemple ;-).
- [ ] Essaye le programme suivant (couper/coller puis **F5**, tu connais maintenant!):
```Python
nom = 'Missy'
photo = '~~(__^·>'
print('Bonjour ' + nom)
print(photo)

nom2 = 'Puffy'
photo2 = '_ _ __/°°¬'
phrase = photo + ' est le copain de ' + photo2
print(phrase)
```


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît créer un programme qui affiche de jolis **Ascii Arts** avec au moins une voiture avec un beau texte (à toi d'ajouter en plus tout ce qui te fait plaisir et autant que tu veux :smile:). Tu peux en trouver dans les sites de la rubrique ["Ascii Art"](#ascii-art) à la fin de cette page. :warning: N'oublie pas d'utiliser `\` devant les caractères spéciaux ou `r'''` pour afficher de grands dessins. :warning: :warning: :warning: Pour ce petit défi, il faut que les dessins soient dans des variables avant que tu les affiches :smile:. Je te propose de sauver ta création avec le nom **"ascii_arts.py"**. Je suis certain que ton programme est trop classe :sunglasses:.

> :bulb: Avec l'Ascii Art, tu auras parfois besoin d'agrandir la fenêtre d'affichage. Tu peux le faire à la souris avec les icônes dans le coin en haut à droite de la fenêtre ou avec le clavier: appuie sur la **touche "windows"** de ton clavier et sans la relâcher appuie sur la **flèche du haut du clavier :arrow_up:** (il faut parfois le faire plusieurs fois).

Prends le temps de t'amuser avec **l'Ascii Art** ou avec les messages et les variables, sauve tes créations et quand tu es prêt, poursuis avec la suite ci-dessous :smile:.


- [ ] Les variables sont utiles aussi pour les calculs, essaye le programme suivant et amuse toi à ajouter d'autres calculs plus complexes (multiplications, divisions, soustractions, parenthèses...):
```Python
bonbons = 10
sucettes = 5
total = bonbons + sucettes
print('total sucreries = ' + str(total))

largeur = 10.5
longueur = 12.84
surface = longueur * largeur
surface_sans_virgule = round(surface)
print('Surface = ' + str(surface))
print('  soit environ ' + str(surface_sans_virgule))
```

> :heavy_plus_sign: Tu noteras qu'on ne peut pas afficher un nombre sans le convertir avant en chaîne de caractères avec la fonction `str()`. De plus, dans le programme ci-dessus, on utilise la fonction `round()` pour arrondir le résultat, c'est pratique les fonctions :smile:.

Les variables ont toujours un nom, mais pas n'importe lequel, il faut que tu choisisses un nom qui t'aide à comprendre ton programme. Par exemple, si tu appelles ta variable `nombre` pour compter tes bonbons, ce n'est pas aussi clair que si tu l'appelles `nombre_bonbons`.

Le nom d'une variable doit respecter les règles suivantes (rien de compliqué, ne t'inquiète pas :smile:):
- Être composé uniquement des caractères `A-Z`, `a-z`, `0-9` et `_`, donc pas d'accents: `nombres_2_lettres`:thumbsup: est correct, mais pas `élèves`:no_entry: à cause des accents.
- Ne pas commencer par un chiffre: `Somme`:thumbsup: et `_compteur`:thumbsup: sont corrects, mais pas `2bonbons`:no_entry:.
- Sensible aux majuscules et minuscules: `total` et `Total` et `ToTaL` sont 3 variables différentes! :bulb: moi, je te conseille de ne jamais mettre de majuscule dans les noms de variables pour éviter les problèmes ;-)


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: pourrais-tu s'il te plaît, créer un programme (**"variables.py"**) qui contient 3 variables avec les valeurs `'Bon'`, `'jour'` et `'soir'` et tu affiches ces variables pour obtenir `Bonjour` et `Bonsoir`.


## Les commentaires pour documenter ton code
Il est très utile d'ajouter des **commentaires** (les lignes de codes commençant par `#`) dans tes supers programmes pour documenter ton code. Tu pourras alors plus facilement te souvenir de "comment ils marchent". Et quand tu échangeras tes programmes avec tes copains, vous pourrez plus facilement comprendre ce que vous avez codé. Tu verras, c'est pratique les commentaires :smile:.
- [ ] Voici un programme qui montre des exemples de commentaires, n'hésite pas à le modifier:
```Python
# Ceci est une ligne de commentaire

message = 'Coucou'
print(message) # Ceci est un commentaire au bout d'une ligne

# Et voici maintenant
# un commentaire sur
# plusieurs lignes

# On peut commenter une ligne de code pour éviter
# qu'elle soit exécutée, par exemple pour 'tracer & debugger'
# ton code, comme dans la ligne ci-dessous
#print('longueur de messages =', len(message), 'caractères')
```


## Les chaînes de caractères et la fonction `print()`
Les chaînes de caractères et la fonction `print()` sont souvent utilisées dans les programmes... et ils existent d'ailleurs plusieurs manières de les utiliser, en voici quelques exemples, mais ce n'est pas très graves si tu ne comprends pas tout, c'était surtout pour te montrer qu'ils existent souvent plusieurs manières de faire et cela te permettra de lire plus facilement les programmes des autres copains :smile:.  
- [ ] Copie le bout de code suivant, prends le temps de le lire, et amuse toi à le modifier:
```Python
print('Voici un message entouré de guillemets simples')
print("Les doubles guillemets marchent aussi :-) ")
print('''Les messages sur plusieurs
lignes sont entourés
de 3 guillemets simples''')
print("""ou de 3 guillemets doubles
et oui, les deux sont
possibles comme je l'ai écris plus haut ;-)""")
print('Petit rappel sur les caractères spéciaux: \' \\ \"')

# On utilise la fonction len() pour connaître le nombre
# de caractères d'une chaîne
mon_message = 'Coucou Python'
nombre_caractères = len(mon_message)
print('Le message \"' + mon_message + '\" fait',
      nombre_caractères, 'caractères.')

# On peut afficher une lettre d'un message par sa position
# qui commence à 0 et se termine à "len(chaine) - 1"
print('Lettre à la position 0 (1ère):', mon_message[0],
      ', dernière lettre:', mon_message[nombre_caractères - 1])

# Il y a une autre manière plus simple de connaître
# la dernière lettre d'une chaîne avec l'index "-1",
# et "-2" sera l'avant dernière...
print('Lettre à la dernière position (-1):', mon_message[-1],
      ', avant dernière lettre (-2):', mon_message[-2])

# On peut afficher une partie de chaîne entre 2 positions
print('De la position 3 à la position 6 non inclus:',
      mon_message[3:6])

# On peut mettre en majuscules ou minuscules
print('En majuscules', mon_message.upper())
print('En minuscules', mon_message.lower())

# On peut remplacer des caractères par d'autres (rigolo le ö)
print('Remplacement \'o\':', mon_message.replace('o', 'ö'))

# On peut découper une chaîne en plusieurs chaînes, ci-dessous
# on découpe les mots en utilisant l'espace ' '
print('Découpage:', mon_message.split(' '))
```

Ça va, ce n'était pas trop compliqué? Bon, tu as mérité(e) une pause :tropical_drink: et un petit cadeau :gift: ... un :saxophone: :notes: en ascii art:

```Python
print(r'''
______
| ___ \
| |_/ /_ __ __ ___   _____
| ___ \ '__/ _` \ \ / / _ \
| |_/ / | | (_| |\ V / (_) |
\____/|_|  \__,_| \_/ \___/

_,-----,____g===;,
<'.._____,-------g  ;
                 \   \,
                   q   q,
                    q    q,
                   [='     q
                     `;  O  p
                       k  O  p -{0
                        l  O  p -o
                        ,i     p
                         P  O   |
                       q:|   O| |BD
                          [   | P b
                          |   |  |____________
                        [ |   |  |\         /
                        | '   |  P :       ;
                        | [   0   Q:  ( )  ;
                         [ P  ( )  |;  ( ) ;
                         :Q  ( )  V        p
                          \   [           ;
                           \',     O    /
                             ' ; _ . '
''')
```
J'ai trouvé le saxophone sur le site [asciiart.eu](https://asciiart.website/index.php?art=music/musical%20instruments)


- [ ] Continuons sur les chaînes de caractères avec l'utilisation très pratique de la fonction `.format()` et des accolades `{}` pour les paramètres. En fait, si l'accolade est vide, on utilise le paramètre qui suit, si l'accolade contient un numéro ou un nom (comme dans `{2}` ou `voiture`), on utilise le paramètre avec ce numéro ou ce nom, et on peut alors utiliser plusieurs fois le même paramètre dans la chaîne. Bon, avec un exemple, ça sera plus clair:
```Python
nb_bonbons = 3
prix_unitaire_bonbon = 0.20
prix_total = nb_bonbons * prix_unitaire_bonbon

# Exemple avec des accolades sans numéro
ma_commande = 'Je voudrais {} bonbons à {}€ l\'unité, svp.'
print(ma_commande.format(nb_bonbons, prix_unitaire_bonbon))

# Exemple avec des accolades avec numéros dans l'ordre
# et on utilise plusieurs fois un paramètre (le '0' ici)
ma_commande = 'Je voudrais {0} bonbons à {1}€ l\'unité, svp.'
ma_commande = 'Hum, c\'est cool d\'avoir {0} bonbons.'
print(ma_commande.format(nb_bonbons, prix_unitaire_bonbon))

# Exemple avec des noms pour les paramètres, c'est pratique
# car le code est alors plus "lisible".
ma_voiture = 'J\'adore {marque} surtout le modèle {modele}!'
print(ma_voiture.format(marque='Bugatti', modele='Chiron'))
```

> :heavy_plus_sign: Si tu veux en savoir plus sur **les chaînes de caractères** ("string" en anglais), tu peux lire la documentation officielle Python sur [Les chaînes de caractères](https://docs.python.org/fr/3/tutorial/introduction.html#strings)... mais ce n'est pas obligatoire et tu peux aussi passer à la suite directement sans lire tout cela :smile:.

> :bulb: j'ai regroupé [en bas de ce document](#liens-utiles-pour-python-snake) les différents liens pour que tu puisses facilement les retrouver dans le futur.

:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: à partir du programme précédent, pourrais-tu s'il te plaît, créer un programme (**"chaines.py"**) qui affiche au moins 3 modèles de voitures Bugatti et 3 modèles de voitures Renault, tout en utilisant la même variable `ma_voiture` du programme précédent.


## Les tests ou conditions avec `if elif else`
Les mots clés `if condition :`, `elif condition :` et `else:` permettent de tester des variables dans tes programmes. C'est de l'anglais: `if` veut dire "si", `else` veut dire "sinon" et `elif` n'existe pas mais on pourrait dire que c'est "sinon si".

- [ ] Bon, le plus simple est que tu lises et essayes le code suivant :smile::
```Python
bonbons_ethan = 33
bonbons_anna = 200   # oh la gourmande ;-)

# Un simple test, remarque les ":" en bout de ligne du "if"
# ainsi que les 4 espaces devant chaque ligne du bloc de
# code du "if"
if bonbons_anna > bonbons_ethan:
    ecart = bonbons_anna - bonbons_ethan
    print('Anna a', ecart, 'bonbons de plus qu\'Ethan!')

# Un autre exemple avec "else:"
if bonbons_anna > bonbons_ethan:
    print('Anna a plus de bonbons qu\'Ethan!')
else:
    print('Anna a moins ou autant de bonbons qu\'Ethan!')

# Un autre exemple avec "elif ... :"
if bonbons_anna > bonbons_ethan:
    print('Anna a plus de bonbons qu\'Ethan!')
elif bonbons_anna < bonbons_ethan:
    print('Anna a moins de bonbons qu\'Ethan!')
else:
    print('Anna a autant de bonbons qu\'Ethan!')


chocos_ethan = 12
chocos_anna = 12
age_ethan = 10
age_anna = 7

# Un exemple avec deux conditions de tests, ici avec "and" (et)
# mais on peut aussi faire avec "or" (ou)
# Pour tester l'égalité, il faut "==".
if chocos_anna == chocos_ethan and age_anna < age_ethan:
    print('Anna a autant de chocos qu\'Ethan alors \n'
          'qu\'elle est plus jeune que lui!')

# Un exemple de tests "imbriqués"
if age_anna < age_ethan:
    print('Anna est plus jeune qu\'Ethan')
    if chocos_anna == chocos_ethan:
        print('et a le même nombre de chocos!')
    elif chocos_anna > chocos_ethan:
        print('et a plus de chocos!')
    else:
        print('et a moins de chocos!')

# N'hésite pas à changer les valeurs des variables pour voir
# comment les "if" fonctionnent (ou pour avoir plus de bonbons
# que Anna ;-)
```

> :heavy_plus_sign: Tu as peut être remarqué qu'il y avait **4 espaces** au début des lignes qui se trouvent "dessous un" `if ... :` / `elif ... :` / `else:`. On appelle cela **l'indentation**, cela rend le programme plus lisible mais c'est aussi obligatoire pour distinguer les **blocs de codes** qui vont ensemble... si tu les oublies, ton code n'a plus le même sens, par exemple:
```Python
a = 12
b = 10

if a < b:
    print('a est plus petit que b de ')
    ecart = b - a
print(ecart) # erreur ici, il faut 4 espaces au début

if a > b:
    print('a est plus grand que b')

# tu peux essayer d'autres valeurs de a et b si tu veux
```

> :heavy_plus_sign: Si tu veux en savoir plus sur les instructions `if elif else`, tu peux lire la documentation officielle Python sur [les tests if elif else](https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements)... mais ce n'est pas obligatoire et tu peux aussi passer à la suite directement sans lire tout cela :smile:.


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"tests.py"**) qui va te permettre de comparer une taille en mètres (par exemple celle de ton animal préféré) avec les tailles d'un lion (1,2 mètres), d'un éléphant d'Afrique (3.2 mètres) et d'une girafe (6.1 mètres). Toutes ces tailles seront stockées dans des variables différentes et la comparaison utilisera ces variables. Ton programme affichera alors les phrases exactes suivantes en fonction de la taille de ton animal préféré:
```Python
Mon animal préféré (0.5m) est plus petit qu'un lion (1.2m).
Mon animal préféré (1.2m) est aussi grand qu'un lion (1.2m).
Mon animal préféré (1.5m) est plus grand qu'un lion (1.2m) mais plus petit qu'un éléphant (3.2m).
Mon animal préféré (3.2m) est plus grand qu'un lion (1.2m) mais aussi grand qu'un éléphant (3.2m).
Mon animal préféré (4.0m) est plus grand qu'un éléphant (3.2m) mais plus petit qu'une girafe (6.1m).
Mon animal préféré (6.1m) est plus grand qu'un éléphant (3.2m) mais aussi grand qu'une girafe (6.1m).
Mon animal préféré (6.4m) est plus grand qu'une girafe (6.1m).
```
  N'oublie pas de mettre des lignes commentaires afin que je comprenne mieux ton programme, que je testerai avec plusieurs tailles. Amuse toi bien :smile:.


## Les fonctions pour automatiser des actions avec `def`
Savais-tu que les programmeurs étaient des fainéants ;-) Et donc, afin de répéter des actions, ils ont inventé **les fonctions**. En Python, elles sont repérables par le mot clé `def` suivi par le nom de la fonction suivi de parenthèses contenant de 0 à plusieurs paramètres et pour finir `:`, par exemple `def ma_fonction(prenom, age):` et pour *l'appeler*, dans son programme on écrit simplement `ma_fonction('Ethan', 10)` ou même `ma_fonction(prenom = 'Ethan', age = 10)`... On n'oubliera pas **d'indenter avec 4 espaces** le bloc de code de la fonction afin de ne pas confondre avec le reste du programme :smile:.
- [ ] Essaye le bout de code suivant:
```Python
# Voici une petite fonction, comme tu le vois, le bloc de
# code de cette fonction est "indenté" avec 4 espaces.
def dit_bonjour(prenom, age):
    print('Bonjour ' + prenom + ', tu as', age, 'ans!')

# ici, on va appeler la fonction plusieurs fois
# mais avec des paramètres différents
dit_bonjour('Ethan', 10)
dit_bonjour('Anna', 7)

# ici, on utilise les noms des paramètres,
# c'est plus long à écrire, mais un peu plus clair à lire
# et on peut même les mettre dans le désordre!
dit_bonjour(age=44, prenom='Philippe')
```

Il est possible d'avoir des paramètres avec des valeurs par défaut, cela permet ensuite de ne pas forcément appeler une fonction avec tous les paramètres, c'est parfois pratique. De plus une fonction peut retourner un résultat avec le mot clé `return`, c'est très souvent utilisé :smile:.

- [ ] Si dessous, quelques exemples complémentaires sur les fonctions qui retournent un résultat, et les paramètres par défaut:
```Python
# La fonction ci-dessous utilise le paramètre "majorité" avec
# la valeur "18" par défaut (majorité pour la France). Cette
# fonction retourne un nombre d'années.
def nb_années_avant_majorite(age, majorite = 18):
    if age < majorite:
        return majorite - age
    else:
        return 0

# Exemple d'appel avec un seul paramètre
# l'autre est par défaut.
print('Ethan a 10 ans donc il est à ' +
      str(nb_années_avant_majorite(10)) +
      ' années de la majorité française.')

# Exemple avec deux paramètres (la majorité en
# Angleterre est à 17 ans.
print('Andy a 15 ans donc il est à ' +
      str(nb_années_avant_majorite(15, 17)) +
      ' années de la majorité anglaise.')
```

> :heavy_plus_sign: Si tu veux en savoir plus sur les fonctions, tu peux lire la documentation officielle Python sur [les fonctions](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)... mais ce n'est pas obligatoire et tu peux aussi passer à la suite directement sans lire tout cela :smile:.


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"fonctions.py"**) qui va te permettre de savoir si tu as de la fièvre :face_with_thermometer: en fonction de ta température :thermometer:, c'est important dans cette période de coronavirus :mask:! Ce programme contiendra une fonction avec deux paramètres: le premier est la température, le second est le seuil pour la fièvre et **par défaut** la valeur de ce seuil sera à 38.5°C (pour une personne de plus de 1 an). Dans ton programme, tu vas appeler 3 fois ta fonction avec:
  - un seul paramètre: une température de 39.1°C, alors la fonction affiche `tu as de la fièvre :-(`.
  - un seul paramètre: une température de 37.2°C, alors la fonction affiche `tu n'as pas de fièvre :-)`
  - deux paramètres: une température de 38.4°C et un seuil de fièvre de 38.1°C (pour les personnes de moins de 1 an), alors la fonction affiche `tu as de la fièvre :-(`.
  J'ai hâte de tester ton programme pour savoir si je suis malade :face_with_thermometer:!


## La mise en page de mon programme
Pour que ton programme soit plus facile à lire et qu'il fonctionne correctement, il faut respecter des **règles de mise en page simples**, comme:
- :thumbsup: **Il ne faut pas avoir des lignes de plus de 79 caractères**: comme tout le monde suit cette règle, on peut facilement lire les programmes des autres sans changer tout le temps la taille du texte ou de la fenêtre où on code, c'est important :smile:. Tu peux retrouver le numéro de la ligne et de la colonne dans la fenêtre d'édition en bas à droite. J'ai mis une police de caractères de taille 12 (menu "Options/Configure IDLE puis Size") mais tu peux mettre plus petit ou plus gros, c'est toi qui voit, mais ne dépasse pas 79 caractères par ligne.
- :thumbsup: **Quand une ligne est trop longue, coupe là en plusieurs morceaux sur plusieurs lignes**. Ajoute le caractère `\` en fin de ligne qui veut dire "suite à la ligne suivante" et aligne les lignes suivantes sur la parenthèse `(` ou le signe `=`. Voici des exemples:
```Python
# utilisation de "\" en fin de ligne pour dire
# que la ligne se poursuit à la suivante.
# Tu remarqueras qu'on aligne la seconde ligne juste
# au dessous de la suivante mais après le " = "
ma_variable_tres_longue = 1275.8786 + 7678766.9876 + \
                          1766448.9866 # alignement sur "="

# Pour du texte, on n'est pas obligé d'utiliser "\",
# c'est comme on veut, mais c'est mieux que non en fait.
print('voici un texte beaucoup trop long pour '
      'tenir sur un seule ligne dans l\'éditeur donc on '
      'aligne sur la parenthèse ouvrante de la 1ère ligne.')
```
- :thumbsup: Pour avoir un code plus lisible et compréhensible, il est important **d'aérer son code et de le commenter** en mettant des lignes vides et des lignes de commentaires.
- :thumbsup: Quand on écrit des opérations, c'est bien de mettre des espaces, par exemple `a=b+12` est moins lisible que `a = b + 12`.
- :thumbsup: En Python, l'indentation est de **4 espaces**... bon, ça, on l'a vu tout à l'heure: le **contenu d'un bloc de code**, comme le contenu d'une fonction ou d'un test, est facilement repérable car il est décalé de 4 espaces.

> :heavy_plus_sign: Pour en savoir plus, tu peux lire [Le style de codage Python](https://docs.python.org/fr/3/tutorial/controlflow.html#intermezzo-coding-style), mais ce n'est pas obligatoire. Savais-tu que "ceux qui adorent le langage Python" et qui veulent partager la même mise en page pour faciliter les échanges, ont écrit un document très célèbre, le [PEP8](https://www.python.org/dev/peps/pep-0008), qui explique en anglais toutes les règles de présentation.

- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"boucles.py"**) qui contient des fonctions pour **écrire du texte en couleurs** :rainbow:. La première fonction affiche un texte en couleur, elle a deux paramètres: le premier est la couleur, le second est le texte à écrire. La seconde fonction affiche un texte avec les couleurs de l'arc en ciel, elle a un seul paramètre (le texte à afficher) et elle appelle l'autre fonction pour afficher chaque caractère avec une couleur de l'arc en ciel (sans prendre en compte les espaces si possible pour que l'arc en ciel soit joli). Note: Pour l'arc en ciel, je te propose de créer une liste des 5 couleurs suivantes (rouge, orange, vert, bleu, mauve), mais tu peux aussi faire autrement, c'est toi qui voit. Je suis certain que ça va être très joli :smile: ! Tu trouveras ci-dessous un bout de code te permettant d'écrire en couleurs, à toi d'écrire les 2 fonctions avec quelques exemples d'utilisation :smile::
```Python
# Le shell de l'éditeur de texte IDLE ne supporte pas
# vraiment la couleur comme le fond les autres shells
# et donc il faut utiliser une astuce... qui ne fonctionne
# qu'avec IDLE :-(  Ce n'est pas grave, on va quand même
# s'amuser un peu avec :-)  Les couleurs utilisées par
# le shell IDLE sont définies dans le menu
# Options/Configure IDLE dans l'onglet Highlights.
# /!\ Ici, on utilise les couleurs du theme DARK.
# On trouve plus de détails à l'adresse ci-dessous
# https://stackoverflow.com/questions/42472958/how-do-i-print-colored-text-in-idles-terminal
import sys

# Si on n'utilise pas IDLE alors on arrête le programme
# car on aura des choses bizarres à l'écran
try: idle = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

# Dictionnaire des couleurs
couleurs = { "blanc" : "SYNC", "rouge" : "COMMENT",
             "orange" : "KEYWORD", "vert" : "STRING",
             "bleu" : "DEFINITION", "mauve" : "BUILTIN"}

# Petite boucle pour debugger rapidement
#for x, y in couleurs.items():
#    idle.write("Couleur " + x + "\n", y)

idle.write("texte en blanc\n", couleurs["blanc"])
idle.write("texte en rouge\n", couleurs["rouge"])
idle.write("texte en orange\n", couleurs["orange"])
idle.write("texte en vert\n", couleurs["vert"])
idle.write("texte en bleu\n", couleurs["bleu"])
idle.write("texte en mauve\n", couleurs["mauve"])

### AJOUTE TES 2 FONCTIONS ICI

### AJOUTE TES EXEMPLES D'UTILISATION DE TES FONCTIONS ICI

```

Bravo, tu mérites une médaille :medal_sports: !


## Le debug de mon programme
En essayant de programmer, tu as sans doute déjà rencontré les messages suivants:
- une fenêtre appelée **SyntaxError** et qui contient le message:
  - **:no_entry: invalid syntax**: en général, c'est que tu as oublié `:` à la fin d'une ligne, ou le signe `=` dans un paramètre par défaut, ou tu as mal orthographié un mot clé comme `def, if, elif, else, return...`, ou tu n'as pas refermé une parenthèse ou une chaîne de caractères (avec `'` ou `"`) ou peut être que la chaîne de caractères à des caractères spéciaux et tu as oublié de mettre devant eux `\`... quand cela arrive, l'éditeur IDLE positionne le curseur dans la zone où il a détectée l'erreur...
  - **:no_entry: EOL while scanning string literal**: en général, c'est très très grave... non, je plaisante, tu as simplement oublié de mettre `'` ou `"` à la fin de ta chaîne de caractères :smile:.
  - **:no_entry: EOL while scanning string literal**: en général, c'est très très grave... non, je plaisante, tu as simplement oublié de mettre `'` ou `"` à la fin de ta chaîne de caractères :smile:.
  - **:no_entry: expected an indented block**: en général, un bloc de code n'est pas correctement *indenté*, il lui manque 4 espaces ou il en a en trop :smile:.

- dans la fenêtre de résultats, tu as pu lire parfois le message d'erreur ci-dessous:
  - car il manquait la fonction `str()` pour le nombre que tu voulais afficher:
```
Traceback (most recent call last):
  File "/home/cobra/Documents/tp1.py", line 7, in <module>
    dit_bonjour('Ethan', 10)
  File "/home/cobra/Documents/tp1.py", line 4, in dit_bonjour
    print('Bonjour ' + prenom + ', tu as' + age + ' ans!')
TypeError: must be str, not int
```
  - car ton code essayait d'afficher une variable qui n'avait jamais été utilisée avant et donc il ne la connaît pas:
```
Traceback (most recent call last):
  File "/home/cobra/Documents/tp1.py", line 7, in <module>
    print(ecart)
NameError: name 'ecart' is not defined
```

Bon, tu rencontras évidemment d'autres erreurs, pas d'inquiétude, en général, on arrive à trouver rapidement d'où vient le problème et on peut toujours demander de l'aide aux copains si besoin :smile:. De plus, tu apprendras tout à l'heure comment gérer certaines de ces erreurs directement dans ton programme dans le chapitre sur [les exceptions ou comment mieux gérer les erreurs](#les-exceptions-ou-comment-mieux-g%C3%A9rer-les-erreurs-avec-try-except).


## Les listes pour grouper, trier, compter des ensembles de données
Les **listes** permettent de grouper un ensemble de données comme des chaînes de caractères (une liste de courses, de cadeaux, de prénoms...), des nombres (une liste d'ages, de tailles, de poids...). On utilise en Python des **crochets pour les listes**, voici un exemple: `ma_liste_de_cadeaux = ['monopoly', 'ballon', 'poster']`.

- [ ] Essaye maintenant le programme suivant qui te présente les listes. Prends le temps qu'il faut pour bien le lire, modifie le, tu verras, les listes, c'est très pratique :smile::
```Python
# Créons notre première liste et affichons la
liste_maman = ['farine blanche', 'oeufs frais',
               'poudre de perlinpinpin']
print('La liste de maman est:\n', liste_maman, '\n')

# La fonction "len()" retourne le nombre d'éléments
# de la liste
nombre_articles = len(liste_maman)
print('Maman a', nombre_articles,
      'articles dans sa liste de courses.\n')

# On peut accéder à chaque élément avec son "index"
# (sa "position" dans la liste). Cette index est entre
# 0 et "len(liste) - 1"
print('Le 1er élément de la liste de maman est:',
      liste_maman[0], '\n')
print('Le dernier élément de la liste de maman est:',
      liste_maman[nombre_articles - 1], '\n')

# Il y a une autre manière plus simple de connaitre
# le dernier élément d'une liste avec l'index "-1",
# et "-2" sera l'avant dernier...
print('Le dernier élément de la liste de maman [-1] est:',
      liste_maman[-1], '\n')
print('L\'avant dernier élément de la liste de maman est:',
      liste_maman[-2], '\n')

# On peut sélectionner une partie de la liste entre 2
# index avec "index1:index2" où l'élément à l'index1 sera
# inclus mais pas l'élément à l'index2. Attention, je
# redis le petit piège: l'élément à l'index2 n'est pas
# inclus (on peut dire qu'on va de index1 à index2 - 1)
print('Les 2 premiers éléments de la liste de maman sont:',
      liste_maman[0:2], '\n')
# Dans l'exemple suivant, on va de l'index -3 inclus à
# l'index -1 exclus donc le dernier ne sera pas affiché!
print('L\'avant et avant avant derniers de la liste sont:',
      liste_maman[-3:-1], '\n')

# On peut modifier un élément de la liste directement
liste_maman[0] = 'farine blanche T80'
print('La liste de maman est (après modification T80):\n',
      liste_maman, '\n')

# On peut vérifier si un élément est déjà dans la liste
if 'oeufs frais' in liste_maman:
    print('\'oeufs frais\' est dans la liste de maman.\n')

# On peut ajouter un élément à la fin de la liste
# avec la fonction "append(item)"
liste_maman.append('poisson frais')
print('La liste de maman est (ajout de \'poisson frais\'):\n',
      liste_maman, '\n')

# On peut ajouter un élément où on veut dans la liste
# avec la fonction "insert(position, item)"
liste_maman.insert(1, 'beurre salé') # 1 = 2ième position
print('La liste de maman est (ajout de \'beurre salé\'):\n',
      liste_maman, '\n')

# On peut retirer un élément de la liste
# avec la fonction "remove(item)"
liste_maman.remove('poisson frais')
print('La liste de maman est (retrait de \'poisson frais\'):\n',
      liste_maman, '\n')

# On peut retirer un élément où on veut dans la liste
# avec la fonction "pop(index)"
liste_maman.pop(1) # 1 = 2ième position
print('La liste de maman est (retrait de \'beurre salé\'):\n', liste_maman, '\n')
# Note: on pouvait aussi faire
# del liste_maman[1]
# reNote: si on fait liste_maman.pop() donc sans numéro
# et bien on retire le dernier élément

# On peut ajouter deux listes ensemble pour en créer
# une plus grande liste
liste_soeur = ['sucettes cerise', 'bonbons schtroumpf',
               'prince charmant']
liste_courses = liste_maman + liste_soeur
print('La nouvelle liste de courses est:\n',
      liste_courses, '\n')

# Trions en ordre alphabétique avec la fonction "sort()"
liste_courses.sort()

# Affichons la liste avec une boucle "for"
print('Voici les articles de la liste de courses '
      '(maman & soeur):')
for article in liste_courses:
    print('*', article)

# Le print ci-dessous n'est pas joli car il contient
# de nombreux '' et []... mais il est pratique. Tu
# peux le "commenter", c'est à dire "ne plus l'exécuter"
# en mettant le caractère "#" au début de sa ligne.
print(liste_courses)

# Liste de nombres
notes_math = [17.5, 15, 20, 18]
print('\nVoici mes notes en mathématique:', notes_math)

# Il y a aussi d'autres possibilités comme:
# - On peut copier une liste avec "copy()" ou avec "list()"
#   liste2 = liste1.copy()
# ou
#   liste2 = list(liste1)
# - On peut vider le contenu d'une liste avec "clear()"
#   liste.clear()
# - On peut effacer une liste avec "del"
#   del liste
```

Et bien, c'était peut être un peu long, mais le plus important est de savoir que les listes sont très très pratiques :smile: (zut, je l'ai déjà dit ça).

> :heavy_plus_sign: Tu noteras que dans le programme ci-dessus, nous avons **compté le nombre d'éléments** avec la fonction `len()`, **trié en ordre alphabétique** avec `sort()` et affiché la liste avec **une boucle** `for in :` (nous y reviendrons).  Voici le lien vers d'autres exemples de [listes en Python](https://docs.python.org/fr/3/tutorial/introduction.html#lists), mais tu n'es pas obligé(e) d'y aller tout de suite, tu peux continuer avec la suite, c'est toi qui voit :smile:.


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"listes.py"**) qui va nous permettre de jouer :game_die: à **"Devine la marque de voitures que j'ai en tête"** :racing_car: :red_car: :blue_car:! Pour cela:
  - Écris une liste de marques de voitures (pour cela, je te fais confiance, tu en connais plein!).
  - Choisis en une au hasard: pour cela, tu auras besoin d'un bout de code comme ci-dessous que tu devras adapter à ton programme (pas d'inquiétude, nous y reviendrons plus tard):
  ```Python
  # On va utiliser des fonctions de la bibliothèque
  # qui s’appelle "random" (hasard)
  import random

  mon_choix = random.choice(ma_liste)
  ```
  - Demande au joueur de deviner la marque que tu as choisis. Pour cela, utilise `proposition = str(input('Quelle est votre proposition?'))`.
  - Vérifie si la proposition est correcte (attention aux majuscules), si oui, indique au joueur qu'il a gagné. Si non, demande lui à nouveau de faire une proposition (tu peux utiliser une boucle `while` comme dans le bout de code ci-dessous, pas d'inquiétude, nous y reviendrons plus tard):
  ```Python
  on_sort_du_while = 0
  while on_sort_du_while == 0:
      # met ton code ici avec le input()...
      # n'oublie pas l'indentation du bloc de code du while

      # dans le code du bloc du while, si
      # le joueur a trouvé ou abandonné, il te suffit
      # de mettre "on_sort_du_while = 1" pour sortir du while
      if le_joueur_a_trouve... :
          on_sort_du_while = 1

  # Ici on est sorti du while, ajoute ton code de sortie du jeu

  ```
  - Si le joueur propose "abandon", alors tu lui indiques qu'il a perdu et tu affiches le nom de la marque que tu avais choisis.
  - Petit plus: Toutes les 2 propositions, donne un nouvel indice au joueur (une lettre supplémentaire du début du nom de la marque) afin de l'aider un peu. Affiche à la fin le nombre de propositions qu'il a faite (son score).
  - N'hésite pas à ajouter des encouragements, des petits ascii arts... pour que ton programme soit le plus beau possible :)
  Je suis certain que ton programme est trop cool :sunglasses:! J'ai hâte de jouer en famille avec :smile:!


## Les types de données `int float str list bool` et leurs conversions
Python utilise plusieurs **types de données** comme les nombres entiers, les nombres à virgules, les chaînes de caractères... et c'est important de les connaître un peu car on a parfois besoin de les convertir entre eux pour les calculs ou les affichage. Voici un liste des **types de données**:
- `int`: c'est un nombre "entier", c'est à dire un "nombre sans virgule", par exemple `a = 10`. Pour convertir vers ce type, on fera par exemple `a = int('155') # chaîne vers entier` ou bien `a = int(13.4) # flottant vers entier`
- `float`: c'est un nombre "flottant" c'est à dire un "nombre avec une virgule", par exemple `a = 10.4`
- `str`: c'est une chaîne de caractères, par exemple `a = 'coucou'`. Pour convertir vers ce type, on fera par exemple `a = str('14.4') # flottant vers chaîne` ou bien `a = str(13) # entier vers chaîne`
- `list`: c'est une liste (de nombres, de chaînes de caractères...), par exemple `a = ['pomme', 'poire', 'cerise']` ou `a = [1.5, 4.3, 6.8]`

Bon, ceux là on les avait un peu vu auparavant, en voici quelques autres:
- `bool`: c'est un "booléen", c'est à dire une "sorte de nombre" qui ne peut prendre que 2 valeurs: `True` qui signifie **vrai**, et `False` qui signifie **faux**, par exemple `a = True`
- `dict`: c'est un dictionnaire, c'est à dire une liste où chaque élément est lié à une "clé", par exemple `a = {'nom' : 'Ethan', 'age' : 10}` et on peut alors faire `print(a['nom'], a['age'])`.
- `turple` (séquence), `set` (ensemble), `range` (*gamme*)... oui, bon, il y a quelques autres types de données car on peut faire vraiment beaucoup de choses avec Python, mais certains types ne sont pas nécessaires pour t'amuser tout de suite :smile:, ce n'est pas grave de ne pas les connaître pour le moment.


> :heavy_plus_sign: Voici le lien vers la [documentation officielle de Python](https://docs.python.org/fr/3/tutorial/index.html) où tu trouveras tous les détails si tu es très curieux, mais ce n'est pas obligatoire pour t'amuser, c'est toi qui voit :smile:.


## La répétition du code avec les instructions de boucles `while` et `for`
L'instruction `while` peut se traduire en français par 'tant que' et elle permet de faire des **boucles** ou **répétitions** d'un bloc d'instructions jusqu'à ce qu'une condition soit vraie... bon, je m'arrête avec le blabla...
- [ ] Essaye l'exemple suivant:
```Python
i = 1
while i < 6:  # tant que i est < à 6, on continue la boucle
    print(i)
    i = i + 1   # on peut aussi écrire i += 1
```

:warning: Dans le code ci-dessus, tu remarqueras qu'il est facile de se tromper dans le code et d'avoir un boucle qui tourne sans jamais s'arrêter car la condition n'est jamais remplie, et oui, ça peut arriver de se tromper, ça arrive même très très souvent aux programmeurs ;-) On appelle cela, un **bug** :bug:! Pas de panique si ça arrive, il suffit alors d'appuyer en même temps sur **CTRL+C** pour arrêter le programme, pratique non :smile:, à toi d'essayer maintenant...
- [ ] Essaye d'arrêter avec **CTRL+C** ce programme fou (et buggé):
```Python
i = 1
while i < 6:
    print(i)
    i = i - 1  # OH, il y a un bug ici!

# Appuie sur CTRL+C pour arrêter ce programme fou et buggé :)
```

L'instruction `for` peut se traduire en français par "pour" et elle permet de faire des **boucles** ou **répétitions** d'un bloc d'instructions un certain nombre de fois...
- [ ] Essaye l'exemple suivant:
```Python
# Exemple de boucle for avec une liste
liste_courses = ['slip', 'chaussettes', 'chapeau']
for article in liste_courses:
    print('*', article)

# Affichage de chaque lettre d'un mot
for caractere in 'banane':
    print(caractere)

# Exemple de boucle for entre 0 et 5 (soit 6 fois)
for i in range(6):
    print(i)

# Exemple de boucle for entre 2 et 5 (soit 4 fois)
for i in range(2, 6):
    print(i)

# Exemple de 2 boucles imbriquées
for x in range(3): # donc entre 0 et 2
    for y in range(2): # donc entre 0 et 1
        print('x =', x, 'y =', y)
```

- [ ] L'instruction `break` permet de sortir d'une boucle `while` ou `for` quand on le souhaite; l'instruction `continue` permet de retourner au début de la boucle `while` ou `for` quand on le souhaite, et c'est parfois pratique, regarde ci-dessous:
```Python
# Exemple de l'instruction break
i = 1
while i < 6:
    if i == 3:
        break  # si i vaut 3, on arrête le while
    print(i)
    i = i + 1

# Exemple de l'instruction continue
for caractere in 'banane':
    if caractere == 'a':
        continue  # on n'affiche pas les 'a', retour au début
    print(caractere)

# Prend le temps de comprendre le code, joue avec un peu
# avant de passer à la suite :)
```

> :heavy_plus_sign: Si tu veux en savoir plus sur l'instruction `for`, tu peux lire la documentation officielle sur [la boucle for](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements), mais comme d'habitude, ce n'est pas obligatoire :smile:.


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"boucles.py"**) qui génère la table de multiplication **exactement** comme celle ci-dessous mais en utilisant des boucles car copier/coller la table ci-dessous entièrement, ça serait de la triche ;-). Mets ton code là où c'est indiqué. Note: tu remarqueras que les colonnes font 4 caractères de large et que les nombres sont alignés à droite de la colonne à l'aide d'espaces, **happy codage** :smile::
```Python
# Voici la table de référence (appelée table1)
table1 =r'''   x   0   1   2   3   4   5   6   7   8   9  10
   0   0   0   0   0   0   0   0   0   0   0   0
   1   0   1   2   3   4   5   6   7   8   9  10
   2   0   2   4   6   8  10  12  14  16  18  20
   3   0   3   6   9  12  15  18  21  24  27  30
   4   0   4   8  12  16  20  24  28  32  36  40
   5   0   5  10  15  20  25  30  35  40  45  50
   6   0   6  12  18  24  30  36  42  48  54  60
   7   0   7  14  21  28  35  42  49  56  63  70
   8   0   8  16  24  32  40  48  56  64  72  80
   9   0   9  18  27  36  45  54  63  72  81  90
  10   0  10  20  30  40  50  60  70  80  90 100
'''
print(table1)

# Générons maintenant notre table (appelée table2)

### DEBUT DE TON CODE ICI ###

### FIN DE TON CODE ICI ###
print(table2)

# Comparons les deux tables
if table1 == table2:
    print('Bravo, ce sont les mêmes :-)')
else:
    print('Désolé, il doit y avoir une petite erreur :-(')
```

Alors, c'était difficile les boucles? Je suis certain que tu mérites une coupe :trophy:, tu es le(la) plus fort(e), bravo :smile:.


## La saisie au clavier avec la fonction `input()`
La fonction `input()` permet de poser une question à l'utilisateur et de récupérer sa réponse sous la forme d'une chaîne de caractères (que tu peux convertir en entier par exemple, en fonction de tes besoins)...
- [ ] Par exemple:
```Python
# Exemple d'une réponse avec une chaîne de caractères
nom = input('Entre ton nom s\'il te plait? ')
print("Bonjour " + nom)

# Exemple d'une réponse avec un entier
# Ici, on repose la question à l'utilisateur (la personne
# qui répond) jusqu'à ce qu'il saisisse un nombre correct
# supérieur à 0 (bébé?) et inférieur à 117
# (Kane Tanaka, doyenne de l'humanité?)
age = -1
age_min = 0
age_max = 117
while age <= age_min or age >= age_max:
    age = int(input('Quel est ton age s\'il te plait? '))
    if age <= age_min or age >= age_max:
        print('désolé, je n\'ai pas compris!')

print('tu as', age, 'an(s)')
```

Dans le programme ci-dessus, as-tu essayé de mettre un age à 0, à -1, à "wkjdfjj"... et oui, si tu rentres une chaîne de caractères pour l'age, :boom::boom::boom: tu **plantes le programme!!!**... mais comment faire alors? Nous allons voir cela dans le chapitre suivant... Pour le moment, amusons nous :-)


- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"input.py"**) pour jouer à **"Tu mets qui dans ta poubelle sous les épluchures pourries!"** :smile:! Tout d'abord, après un message de bienvenue, tu demanderas au joueur de donner 3 prénoms (avec une boucle) et tu les sauveras dans une liste. Ensuite, tu demanderas au joueur "Qui tu amènes danser dans ta Ferrari?" et tu lui proposeras les numéros 1, 2 et 3 correspondant au 3 prénoms (comme cela, le joueur ne retape que le numéro et pas le prénom entier). Si le joueur répond 2 par exemple, alors tu poursuis avec la phrase suivante "Avec qui tu vas manger une glace?" et tu lui proposes les numéros restants. Et enfin, tu lui dis "et bien c'est [le prénom qui reste] que tu mets dans une poubelle avec des épluchures pourries! Ah, Ah, Ah"... Tu peux évidemment changer les phrases pour adapter le jeu à ton goût. Vivement qu'on fasse jouer ton frère ou ta sœur à ce petit jeu :smile:...


## Les exceptions ou comment mieux gérer les erreurs avec `try except`
En Python, il y a les mots clés `try except` qui permettent de gérer les problèmes, qu'on appelle en informatique, les **exceptions** c'est à dire "quelque chose qui arrive rarement/exceptionnellement" (une manière de dire qu'on avait prévu le problème ;-)). Il y a différents types de problèmes qui peuvent arriver dans un programme, par exemple: le fichier qu'on voulait lire a été effacé ou déplacé, l'utilisateur a entré des lettres alors qu'on voulait des chiffres, l'utilisateur a fait **CTRL+C** alors qu'on voulait sauvegarder son score, ... On ne pourra pas gérer **tous** les différents cas mais on peut essayer d'en gérer un maximum, le programme sera alors beaucoup plus agréable pour l'utilisateur :)

Quand Python détecte un problème, il nous la retourne en lui donnant un nom nous permettant de comprendre le problème et d'agir en conséquence. Il y a par exemples:
- `ValueError`: quand on essaye par exemple de convertir en entier une chaine de caractères qui ne représente pas un entier, :no_entry: `a = int("coucou")`
- `TypeError`: quand on essaye par exemple d'ajouter un nombre à une chaîne de caractères, :no_entry: `a = 12 + "coucou"`
- `NameError`: quand on utilise un variable dans un calcul ou lors d'un affichage, alors qu'on ne l'avait jamais utilisée avant, et donc Python ne la connaît pas et retourne une erreur, :no_entry: `print(a) # première utilisation de a`
- `IndexError`: quand on utilise par exemple une liste avec un index incorrect, :no_entry:
```Python
a = ['coucou', 'cuicui']
print(a[10])  # 10 est en dehors des index possibles
```
- `KeyError`: quand on utilise par exemple un dictionnaire avec une clé incorrecte, :no_entry:
```Python
a = {'Ethan' : 'coucou', 'Anna' : 'cuicui'}
print(a['Annaaaa'])  # Annaaaa n'est pas une clé du dico
```
- `KeyboardInterrupt`: quand l'utilisateur appuie sur **CTRL+C**, on peut alors capturer cet évènement et faire des actions comme fermer les fichiers, sauver le score...  :no_entry:
```Python
while True:
    try:
        print('Boucle sans fin, fait CTRL+C stp')
    except KeyboardInterrupt:
        break; # on sort du while

print('\nTu as fait CTRL+C :-)')
```
- `OverflowError`: quand on fait des calculs trop grands par exemple, :no_entry: `a = 10.0 ** 10 ** 100 # un Gogolplex`
- `ZeroDivisionError`: quand on divise par 0, c'est interdit, :no_entry: `a = 12/0`
- `SyntaxError`: par exemple quand il manque `:` au bout d'une ligne `if elif else`/`while`/`for`, :no_entry: `if a > 12 print(a) # il manque : dans la ligne`

Une liste complète se trouve dans la [documentation officielle des exceptions](https://docs.python.org/fr/3/library/exceptions.html#bltin-exceptions), mais ce n'est pas nécessaire d'aller la voir tout de suite, il faut juste savoir que ça existe **en cas de besoin** :smile:.


- [ ] Améliorons notre problème précédent (où nous demandions son age à l'utilisateur) avec une **gestion des exceptions**:
```Python
# Exemple d'une gestion d'exception
# Amuse à répondre n'importe quoi comme "jhdg" ou "16.5"
# et regarde ce que répond le programme :-)

age = -1
age_min = 0
age_max = 117

# On fait une boucle toujours vraie, on en sortira
# avec le mot clé "break" quand tout sera en ordre
while True:

    # ici on évite de planter avec try except
    try:
        # la ligne suivante génère une exception si
        # l'utilisateur n'entre pas un entier.
        # Heureusement, on la "capture" avec except
        age = int(input('Quel est ton age stp? '))

    except ValueError:
        print('Il faut saisir un chiffre entier svp!')
        continue # signifie "on reprend au début du while"

    else:
        # C'est un nombre, on peut le vérifier maintenant
        if age <= age_min or age >= age_max:
            print('L\'age doit être entre', age_min, 'et',
                  age_max, '(non compris)!')
        else:
            break # tout est en ordre, on sort du while

# Et on affiche l'age
print('tu as', age, 'an(s)')
```

Oulala, ce n'était pas simple tout cela... bon, ne t'inquiète pas, on pourra en reparler, retiens surtout qu'on peut gérer les erreurs et tu verras, quand tu en auras besoin, tu seras content d'utiliser `try except` :smile:.


> :heavy_plus_sign: Si tu veux en savoir plus sur les **exceptions** `try except finally`, tu peux lire la documentation officielle sur [les exceptions avec try except finally](https://docs.python.org/fr/3/tutorial/errors.html).


## Faire des calculs de dates et de temps
Ce n'est pas toujours très simple de faire des calculs sur les dates et sur le temps. Par exemple, si je te demande de me donner la date complète dans 12 jours, et bien tu dois d'abord vérifier que dans 12 jours on ne change pas de mois car si on change de mois, il faut savoir si c'est un mois à 28, 29, 30 ou 31 jours, et puis il faut savoir si on change d'année, et puis il faut compter les jours de semaines... Pour le temps, c'est pareil, c'est toujours un peu compliqué d'ajouter des secondes à des minutes à des heures et à des jours... mais heureusement, Python est là pour nous aider avec les fonctions du `module datetime`.

- [ ] Amuse toi avec les exemples suivants:
```Python
# On commence par indiquer à Python qu'on veut le module
# "datetime" et on indique aussi que dans notre programme
# ci-dessous, on utilisera les mots "date", "time" et
# "datetime" en fonction de nos besoins.
from datetime import date, time, datetime

# Récupérons et affichons la date d'aujourd'hui avec
# la fonction "strftime()" qui possède des paramètres très
# pratiques dont la liste est à l'adresse suivante
# https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes
maintenant = date.today()
print('Aujourd\'hui, nous sommes le',
      maintenant.strftime('%A %d %B %Y'))

# Zut, c'est en anglais, bon pour l'avoir en français
# on va importer le module "locale" et l'utiliser pour
# avoir toutes les dates et les heures en français :-)
# Si tu veux en savoir plus, c'est dans le lien suivant:
# https://docs.python.org/fr/3.6/library/locale.html
# Note: La prochaine fois, tu peux monter les deux lignes
# ci-dessous au début de ton programme
import locale
locale.setlocale(locale.LC_ALL, '')

# Affichons à nouveau la date du jour en français
print('Aujourd\'hui, nous sommes le',
      maintenant.strftime('%A %d %B %Y'),
      '(en français!)')

# Récupérons le nom du jour avec "strftime('%A')"
anniv = date(2009, 11, 13)
print('Je suis es né(e) un ' + anniv.strftime('%A') +
      ', tu le savais?')

age = maintenant - anniv
print('J\'ai', int(age.days / 365.25), 'ans.')

# Déterminons si ton anniversaire est passé cette année.
# Pour cela on récupère le jour et le mois de ton anniv
# mais avec l'année en cours
anniv_cette_annee = date(maintenant.year, anniv.month,
                         anniv.day)
if anniv_cette_annee < maintenant:
    anniv_annee_prochaine = date(maintenant.year + 1,
                                 anniv.month, anniv.day)
    prochain = anniv_annee_prochaine - maintenant
    print('Mon anniversaire est passé, le prochain est dans',
          prochain.days, 'jours.')

elif anniv_cette_annee > maintenant:
    prochain = anniv_cette_annee - maintenant
    print('Mon anniversaire est cette année dans',
          prochain.days, 'jours, c\'est cool!')

else:
    print('C\'est aujourd\'hui mon anniversaire!')

# Convertissons une date à partir d'une chaîne de caractères
# avec "strptime()", on utilise les mêmes paramètres que
# pour "strftime()" vue plus haut
tour_eiffel_fin = datetime.strptime('31 Mars 1889', '%d %B %Y')
print('Fin de la construction de la Tour Eiffel le',
      tour_eiffel_fin.strftime('%A %d %B %Y'))
```

- [ ] Pour les calculs sur le temps, voici quelques exemples:
```Python
# On commence par indiquer à Python qu'on veut le module
# "datetime" et on indique aussi que dans notre programme
# ci-dessous, on utilisera le mot "timedelta"
from datetime import timedelta

# Petite fonction pour simplifier les calculs
def duree_annuelle(activite_en_min, frequence_par_jour):
    duree = activite_en_min * frequence_par_jour * 365.25
    # La fonction "timedelta" va nous convertir les minutes
    # en une durée pratique à utiliser
    return timedelta(minutes=duree)


brossage_en_min = 3
brossage_par_jour = 2
print('Chaque année, je me brosse les dents pendant',
      duree_annuelle(brossage_en_min, brossage_par_jour))

gym_en_min = 1.5 * 60   # 1h30 soit en minutes 1.5 * 60
gym_par_jour = 2.0 / 7    # 2 fois sur 7 jours
print('Chaque année, je fais de la gym pendant',
      duree_annuelle(gym_en_min, gym_par_jour))

repas_en_min = 15 + 30 + 30 # petit déj, midi, soir
repas_par_jour = 1
print('Chaque année, je mange pendant',
      duree_annuelle(repas_en_min, repas_par_jour))

dodo_en_min = 10.5 * 60 # de 21h à 7h30 en minutes
dodo_par_jour = 1
print('Chaque année, je dors pendant',
      duree_annuelle(dodo_en_min, dodo_par_jour))
```

> :heavy_plus_sign: Si tu veux en savoir plus sur les calculs de dates et de temps, tu peux lire la documentation officielle sur [la date et le temps](https://docs.python.org/fr/3/library/datetime.html).


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"date.py"**) qui va afficher **le calendrier du mois** :spiral_calendar: que l'utilisateur souhaite voir. Par exemple, l'utilisateur entre "05/2020" et tu affiches:
  ```Python
  Calendrier 2020 - mai
  lun mar mer jeu ven sam dim
    -   -   -   -   1   2   3
    4   5   6   7   8   9  10
   11  12  13  14  15  16  17
   18  19  20  21  22  23  24
   25  26  27  28  29  30  31
    -   -   -   -   -   -   -
  ```
  Quelques petits conseils: Je te conseille de créer une liste de 7 jours x 6 lignes soit 42 éléments que tu initialises à " -". Puis, détermine le nombre de jours dans le mois en faisant une différence de dates entre le 1er du mois en cours et le 1er du mois suivant. Enfin, détermine si le 1er jour du mois est un lundi, ou un mardi... Pour cela, utilise les codes se trouvant sur le site Python https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes puis ajuste en fonction de ton calendrier. Ensuite, remplis cette liste et affiche là. Si c'est un peu trop difficile, demande de l'aide, c'est normal de demander de l'aide :-). Tu peux vérifier ton calendrier généré avec celui qui se trouve en bas à droite de ton ordinateur :smile:. Merci pour ce super calendrier, il me sera très utile, j'en suis certain :smile:!


## Générer des nombres au hasard avec `random()`
Il est souvent pratique de pouvoir générer des nombres au hasard: pour faire des tirages au sort, des jeux de dés... Pour cela, on utilise la fonction `random()`. Au fait, savais-tu qu'on dit aussi **les nombres aléatoires** pour dire les nombres au hasard :smile:.

- [ ] Amuse toi avec les exemples suivants:
```Python
# On va utiliser des fonctions de la bibliothèque
# qui s’appelle "random"
import random

# A chaque type de tirages aléatoires, on affichera
# "nombre_de_fois" le résultat. Comme cela, si on veut le
# changer, ça sera rapide :)
nombre_de_fois = 3

# Nombre flottant entre 0.0 (inclus) et 1.0 (exclus)
# avec "random.random()"
for i in range(nombre_de_fois):
    print('random.random())', random.random())

# Nombre flottant entre 2 nombres a (inclus) et b (exclus)
# avec "random.uniform(a, b)", ici entre 8.0 et 24.0
for i in range(nombre_de_fois):
    print('random.uniform(8, 24)', random.uniform(8, 24))

# Nombre entier entre 2 nombres a (inclus) et b (inclus)
# avec "random.randint(a, b)", ici entre 1 et 10
for i in range(nombre_de_fois):
    print('random.randint(1, 10)', random.randint(1, 10))

# Choisir un caractère dans une chaine avec "random.choice()"
for i in range(nombre_de_fois):
    print('random.choice(\'abcdef\')',
          random.choice('abcdef'))

# Choisir un élément dans une liste avec "random.choice()"
ma_liste = ['vtt', 'skate', 'roller', 'patins', 'trotinette']
for i in range(nombre_de_fois):
    print('random.choice(ma_liste)', random.choice(ma_liste))

# Mélanger une liste avec "random.shuffle()"
# Note: "random.shuffle()" va faire le mélange directement
# dans la liste donc celle-ci est modifiée.
print('ma_liste avant:', ma_liste)
random.shuffle(ma_liste)
print('ma_liste après:', ma_liste)
```

> :heavy_plus_sign: Si tu veux en savoir plus sur les **nombres aléatoires**, tu peux lire la documentation officielle sur [les nombres aléatoires avec la fonction random()](https://docs.python.org/fr/3/library/random.html).

!!!
:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Pourrais-tu s'il te plaît, créer un programme (**"hasard.py"**) pour jouer aux dés avec l'ordinateur. Pour cela, j'ai déjà écris une bonne partie du programme, et tu vas devoir compléter partout où il est écrit `### A TOI D'ECRIRE QUELQUE CHOSE ICI`. N'hésite pas à modifier ma proposition pour la rendre plus jolie et plus amusante :smile::
```Python
# On aura besoin de la bibliothèque des nombres aléatoires
### A TOI D'ECRIRE QUELQUE CHOSE ICI

# On utilise des gros chiffres en ascii art trouvés ici
# http://patorjk.com/software/taag/#p=display&f=Modular&t=0123456789
# Pour les utiliser, on fait une liste contenant chaque
# ligne et une fonction pour les afficher
nums = list()
nums_largeur = 9
nums_hauteur = 7
nums.append(" _______   ____    _______  _______  _   ___  _______  ___      _______   _____   _______ ")
nums.append("|  _    | |    |  |       ||       || | |   ||       ||   |    |       | |  _  | |  _    |")
nums.append("| | |   |  |   |  |____   ||___    || |_|   ||   ____||   |___ |___    | | |_| | | | |   |")
nums.append("| | |   |  |   |   ____|  | ___|   ||       ||  |____ |    _  |    |   ||   _   || |_|   |")
nums.append("| |_|   |  |   |  | ______||___    ||___    ||_____  ||   | | |    |   ||  | |  ||___    |")
nums.append("|       |  |   |  | |_____  ___|   |    |   | _____| ||   |_| |    |   ||  |_|  |    |   |")
nums.append("|_______|  |___|  |_______||_______|    |___||_______||_______|    |___||_______|    |___|")

# La fonction suivante nous permettra d'afficher les nombres
# en ascii art. On pourrait même la rendre générique et
# ainsi pouvoir choisir plusieurs polices :)
def affiche_nums(val):
    # on vérifie d'abord si le paramètre est correct
    if val not in range(0, 1000001):
        print("Le nombre doit être entre 0 et 1000000!")
        return
    # On convertie la valeur en chaine (ex: 100 devient "100")
    val_str = str(val)
    # On va parcourir chaque ligne
    for h in range(nums_hauteur):
        ligne = nums[h]
        chaine = ""
        # On va parcourir chaque caractère du nombre
        for c in val_str:
            # Une petite astuce ici permet de récupérer
            # le numéro pour la multiplication
            pos = (int(c) - int("0")) * nums_largeur
            # On choisit les caractères de la chaine
            # entre les deux positions séparées par ":"
            chaine += ligne[pos : pos + nums_largeur]
        # On affiche la ligne et on passe à la suivante
        print(chaine)


# Petit test de notre fonction d'affichage de nombres
# en ascii art
# Tu peux retirer les commentaires des lignes suivantes
# pour tester l'affichage des nombres
#for i in range(0, 101):
#    affiche_nums(i)


# Faisons quelque chose de similaire avec des dés
# en ascii art.
des = list()
des_largeur = 7
des_hauteur = 5
des.append("┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐")
des.append("│     ││ o   ││ o   ││ o o ││ o o ││ o o │")
des.append("│  o  ││     ││  o  ││     ││  o  ││ o o │")
des.append("│     ││   o ││   o ││ o o ││ o o ││ o o │")
des.append("└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘")

# La fonction suivante nous permettra d'afficher les 2 dés
def affiche_2_des(de1, de2):
    ### A TOI D'ECRIRE QUELQUE CHOSE ICI


# Petit test de notre fonction d'affichage des 2 dés
# en ascii art
# Tu peux retirer les commentaires des lignes suivantes
# pour tester l'affichage
#for i in range(1, 7):
#    affiche_2_des(i, 7 - i)

# Petite fonction qui retourne les valeurs de 2 dés et
# les affiche
def lance_et_affiche_2_des():
    ### A TOI D'ECRIRE QUELQUE CHOSE ICI
    de1 = ...
    de2 = ...
    affiche_2_des(de1, de2)
    return de1, de2


print(r"""
Bonjour, je suis ORDIN (ô.ô). Es-tu prêt pour jouer à:

     (¯`·._.·[ Le jeu de DES ]·._.·´¯)

But: Etre le premier à 100 points!
Règles:
 - On joue chacun son tour les 2 dès à la fois.
 - On multiplie les valeurs des 2 dés et on ajoute
   le résultat à son score.
 - Les doubles rapportent le double de points!
 - Le premier qui a 100 points à gagner.
 - Celui qui fait le plus grand score commence la partie
   (en cas d'égalité, c'est le joueur qui commence).

Commençons :-)
""")


# Les variables suivantes nous permettrons de savoir
# qui est en train de jouer, par défaut on met le joueur
# mais de toute façon on va tirer le 1er joueur aux dés
ordi = 0
joueur = 1
a_qui = joueur

# La liste suivante contiendra les points de chaque joueur
# ex: points[ordi] pour les points de l'ordinateur
points = [0, 0]


print("Déterminons qui commence...")
print("Lance les dés en appuyant sur ENTREE")
i = input()
de1, de2 = lance_et_affiche_2_des()
lancer_joueur = de1 * de2
print("Tu as fais " + str(lancer_joueur) + ". A mon tour...")

de1, de2 = lance_et_affiche_2_des()
lancer_ordi = de1 * de2
if lancer_joueur >= lancer_ordi:
    print("Zut, j'ai fait " + str(lancer_ordi) +
          " donc c'est toi qui commence!")
    a_qui = joueur
else:
    print("Super, j'ai fait " + str(lancer_ordi) +
          " donc c'est moi qui commence!")
    a_qui = ordi


# On sortira de cette boucle avec l'instruction "break"
while True:
    ### A TOI D'ECRIRE QUELQUE CHOSE ICI


# On affiche le nom du gagnant puis on dit au revoir
if a_qui == ordi:
    print("YOUPI, J'AI GAGNE :-)")
else:
    print("ZUT, TU AS GAGNE, BRAVO :-)")

print("Reviens vite jouer avec moi :-)")
```

## Mesurer précisément le temps et faire des pauses
Dans les programmes de jeu, il est souvent pratique de calculer des temps pour les animations ou pour dire aux joueurs "tu as 10 secondes pour répondre à la question...". Pour cela, on utilise le `module time`.

- [ ] Voici quelques exemples:
```Python
# On va utiliser le module "time"
import time

# On commence par faire des pauses de 1 seconde avec
# la fonction "sleep()" (qui veut dire "dormir")
print('A dix, je fais apparaître un mignon lapin! ' +
      'Tu décomptes avec moi?')
for i in reversed(range(10)):
    time.sleep(1)
    print(i)

print('tada')
print(r'''

                 / \
                / _ \
               | / \ |
               ||   || _______
               ||   || |\     \
               ||   || ||\     \
               ||   || || \    |
               ||   || ||  \__/
               ||   || ||   ||
                \\_/ \_/ \_//
               /   _     _   \
              /               \
              |    O     O    |
              |   \  ___  /   |
             /     \ \_/ /     \
            /  -----  |  --\    \
            |     \__/|\__/ \   |
            \       |_|_|       /
             \_____       _____/
                   \     /
                   |     |
from http://www.ascii-fr.com/-Lapins-.html''')

print('Appuie sur entrer pour continuer stp')
pause = str(input())
print('Merci et à bientôt :-)')

```

Note: Il existe de nombreuses manières de mesurer le temps et de gérer le clavier: par exemple, on peut faire des mesures de temps très très précises à la nano seconde près, on peut faire des boucles qui gèrent un appui touche uniquement si besoin (le programme est alors "non bloqué")... mais tout cela reste un peu compliqué pour le moment... et avec ce qu'on a appris, on peut déjà beaucoup s'amuser :smile:.

> :heavy_plus_sign: Si tu veux en savoir plus sur la mesure du temps et les pauses, tu peux lire la documentation officielle sur [la mesure du temps et les pauses](https://docs.python.org/fr/3/library/time.html).


## Bien organiser mes données avec les classes
Quand on fait un programme, il est souvent pratique de bien organiser les données, et les **classes**, avec le mot clé `class`, servent justement à cela. :warning: Les classes n'ont rien à voir avec l'école ;-)... les classes sont plutôt pour **le classement des documents/données**, une sorte de classeur... Par exemple, imagine que tu fais un jeu dans lequel il y a 3 personnages qui s'appellent Puffy, Catty et Missy. Chaque personnage a donc un nom mais aussi une photo, un nombre de points de vie... et bien dans ce cas, on va créer une classe qui se nommera "personnage" et on va pouvoir faire des fonctions qui vont manipuler les données de cette classe (ajouter/retirer des points de vie, afficher le nom) sans avoir besoin de faire une fonction pour chacun des personnages.

- [ ] Essayons le code suivant:
```Python
# Ce programme est un peu particulier car on va d'abord
# écrire le code de notre classe puis on l'utilisera
# et donc le début de ce programme est un peu plus bas
# après la création de la classe :-)

# Donc, commençons par la création de la classe "MonPerso"
# Tu noteras que j'ai mis des majuscules mais pas de "_"
# car on fait souvent cela pour les classes (mais pas
# pour les variables ni les fonctions)
class MonPerso:

    # Les pièces d'or et les points de vie
    # par défaut, chaque personnage a 10 de chaque
    pieces_d_or = 10
    points_vie = 10

    # La fonction __init__ ci-dessous est particulière,
    # elle est appelée automatiquement quand
    # on fait par exemple "puffy = MonPerso(...)"
    # On appelle cela un "constructeur de classe"
    # mais ce n'est pas très important.
    # Le mot clé "self" signifie que cette fonction
    # est uniquement pour la classe MonPerso
    # D'une manière générale, on me "self" devant
    # les variables de la classe quand on veut les
    # modifier dans le code dela classe...
    def __init__(self, prenom, description, photo):
        self.prenom = prenom
        self.description = description
        self.photo = photo

    # On ajoute une fonction qu'on appelera en faisant
    # par exemple puffy.nom_complet(). Là aussi, c'est une
    # fonction uniquement pour la classe MonPerso
    # donc seule les personnages pourront l'appeler.
    def nom_complet(self):
        msg = str(self.prenom + ' ' + self.description +
                  ' ' + self.photo)
        return msg                   

    # La fonction suivante permet de gérer les points de vie
    # Note: "a -= b" est comme "a = a - b" mais en plus court
    def recoit_coup(self, force):
        if self.points_vie > force:
            self.points_vie -= force # ouch, ça fait mal!
        else:
            self.points_vie = 0      # à 0 point, t'es mort!

    # Quand on mange, on gagne des points de vie.
    def mange(self, quantite):
        self.points_vie += quantite  # miam, ça fait du bien!

    # Quand on vole les pièces d'or
    def vole_or(self, nb_de_pièces):
        if self.pieces_d_or > nb_de_pièces:
            self.pieces_d_or -= nb_de_pièces
        else:
            self.pieces_d_or = 0     # 0 pièce, t'es pauvre!

    # La fonction suivante nous permettra d'afficher
    # tous les détails
    def details(self):
        msg = str(self.points_vie)
        if self.points_vie == 0:
            msg += ' point de vie (mort!)'
        elif self.points_vie >= 100:
            msg += ' points de vie (gourmand!)'
        else:
            msg += ' points de vie'

        msg += ' et ' + str(self.pieces_d_or)
        if self.pieces_d_or == 0:
            msg += ' pièce d\'or (ruiné!)'
        elif self.pieces_d_or >= 100:
            msg += ' pièces d\'or (riche!)'
        else:
            msg += ' pièces d\'or'

        return msg


# FIN DE LA CLASSE MON PERSO :-)
# Maintenant, on va l'utiliser

# On crée 3 personnages avec le constructeur __init__
# de notre classe MonPerso
puffy = MonPerso('Puffy', 'le petit chien', '____/°°¬')
catty = MonPerso('Catty', 'le grand chat', '^ↀᴥↀ^')
missy = MonPerso('Missy', 'l\'intrépide souris', '~~(__^·>')

# On peut afficher directement le contenu des variables
# de la classe avec le "."
print(puffy.prenom)

# On peut appeler les fonctions de la classe
# avec ".nom_de_la_fonction()"
print(puffy.nom_complet())
print('Il a ' + puffy.details() + '.')

# On peut mettre les personnages dans une liste si on veut
# cela est pratique pour les manipuler ensemble comme
# ci-dessous pour les afficher
mes_persos = [puffy, catty, missy]
print('\nVoici tous les personnages:')
for i in mes_persos:
    print('*', i.nom_complet(), ':\n\t', i.details())

# Donnons à manger et de l'or à Catty
print('\n')
catty.mange(120)
catty.pieces_d_or += 92
print(catty.prenom, ':', catty.details())

# On va voler l'argent de missy et l'a frappé sur la tête
missy.vole_or(12)
missy.recoit_coup(8)
print(missy.prenom, ':', missy.details())

# Et on refrappe sur la tête de la pauvre missy
missy.recoit_coup(8)
print(missy.prenom, ':', missy.details())

# Bon, on va la ressusciter en lui donnant à manger
missy.mange(108)
print(missy.prenom, ':', missy.details())
```

Les classes, c'est pratique et c'est "classe" :sunglasses:!

> :heavy_plus_sign: Si tu veux en savoir plus sur les **classes**, tu peux lire la documentation officielle sur [les classes](https://docs.python.org/fr/3/tutorial/classes.html).


## Bien organiser mes données (bis) avec les dictionnaires
Je ne souhaitais pas forcément te parler des **dictionnaires** en Python... et puis j'ai changé d'avis, car il y a des cas où c'est vraiment trop pratique. Un dictionnaire, c'est une liste où chaque élément est lié à une "clé" (on dit aussi une "entrée"), par exemple `a = {'nom' : 'Ethan', 'age' : 10}` et on peut alors faire `print(a['nom'], a['age'])`. Dans un dictionnaire, il y a donc **une "clé" associée avec une donnée** qui peut être un nombre, une chaîne de caractères... c'est donc comme pour un vrai dictionnaire où la "clé" est le mot qu'on cherche, et la donnée, c'est la définition du mot. Un dictionnaire est donc *un peu comme une classe* mais avec seulement 2 éléments (la clé et la donnée)... bof, si c'est un peu comme une classe, qu'elle est alors son intérêt? Et bien l’intérêt est que la "clé" permet de faire des recherches très rapidement et simplement.

- [ ] Voici un exemple avec lequel apprendre... et t'amuser :smile::
```Python
# Un premier exemple de dictionnaire très très simple
# On utilise les clés, ici "nom" et "age" pour récupérer
# rapidement les données, ici la chaine 'Ethan' et le
# nombre entier 10
a = {'nom' : 'Ethan', 'age' : 10}
print(a['nom'], a['age'])

# On peut afficher tout le dictionnaire
print(a)

# On peut modifier une donnée d'un dictionnaire
a['age'] = 11  # Ethan a maintenant 11 ans :-)
print(a)

# On peut ajouter des couples clé/donnée
a['sport'] = 'gym'
a['instrument'] = 'saxophone'
print(a)

# On peut supprimer une entrée avec le mot clé "del"
del a['instrument']
print(a)

# On peut connaître la taille du dictionnaire avec len()
print(len(a))

# On peut récupérer une liste des clés avec le mot clé "list"
# C'est une astuce qui peut être très pratique :-)
liste_a = list(a)
print(liste_a)

# On peut vérifier si une clé existe (avant de l'ajouter
# par exemple)
if 'passion' in a:
    print(a['passion'])
else:
    print('\'passion\' pas dans le dico, on l\'ajoute.')
    a['passion'] = 'dessin'
print(a)

# On peut afficher les clés avec une boucle "for"
for x in a:
    print('clé =', x)

# On peut afficher les données avec une boucle "for"
# et avec values()
for x in a.values():
    print('donnée =', x)

# On peut afficher tout le contenu avec une boucle for et
# items()
# Note: dans cette boucle for, items() renvoie deux valeurs
# donc on met x, y pour les récupérer, pratique !
for x, y in a.items():
    print('clé =', x, ', donnée =', y)

# On peut copier un dictionnaire dans un nouveau avec copy()
# et si on modifie b, a n'est pas modifié
b = a.copy()
del b['passion']
print('dico a =', a)
print('dico b =', b)

# On peut effacer le contenu d'un dictionnaire avec clear()
b.clear()
print('dico b =', b)
```

> :heavy_plus_sign: Si tu veux en savoir plus sur les **dictionnaires**, tu peux lire la documentation officielle sur [Les dictionnaires](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries).


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: pourrais-tu s'il te plaît, créer un programme (**"dictionnaire.py"**) qui va compter le nombre d’occurrences de chaque mot et de chaque lettre dans texte. J'ai choisi un beau texte: "Déclaration des Droits de l'Homme et du Citoyen de 1789". Utilise la performance des dictionnaires pour faire cela, tu vas voir, c'est super puissant :muscle:. Tu vas devoir compléter partout où il est écrit `### A TOI D'ECRIRE QUELQUE CHOSE ICI`, à toi de jouer :smile:.
!!!
```Python
# http://classes.bnf.fr/laicite/references/Declaration_droits_de_l_homme_citoyen_1789.pdf

texte = r"""
Déclaration des Droits de l'Homme et du Citoyen de 1789
Les Représentants du Peuple Français, constitués en Assemblée Nationale, considérant que l'ignorance, l'oubli
ou le mépris des droits de l'Homme sont les seules causes des malheurs publics et de la corruption des
Gouvernements, ont résolu d'exposer, dans une Déclaration solennelle, les droits naturels, inaliénables et sacrés
de l'Homme, afin que cette Déclaration, constamment présente à tous les Membres du corps social, leur rappelle
sans cesse leurs droits et leurs devoirs ; afin que les actes du pouvoir législatif, et ceux du pouvoir exécutif,
pouvant être à chaque instant comparés avec le but de toute institution politique, en soient plus respectés ; afin
que les réclamations des citoyens, fondées désormais sur des principes simples et incontestables, tournent
toujours au maintien de la Constitution et au bonheur de tous.
En conséquence, l'Assemblée Nationale reconnaît et déclare, en présence et sous les auspices de l'Etre
suprême, les droits suivants de l'Homme et du Citoyen.
Art. 1er. Les hommes naissent et demeurent libres et égaux en droits. Les distinctions sociales ne peuvent être
fondées que sur l'utilité commune.
Art. 2. Le but de toute association politique est la conservation des droits naturels et imprescriptibles de l'Homme.
Ces droits sont la liberté, la propriété, la sûreté, et la résistance à l'oppression.
Art. 3. Le principe de toute Souveraineté réside essentiellement dans la Nation. Nul corps, nul individu ne peut
exercer d'autorité qui n'en émane expressément.
Art. 4. La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui : ainsi, l'exercice des droits naturels de
chaque homme n'a de bornes que celles qui assurent aux autres Membres de la Société la jouissance de ces
mêmes droits. Ces bornes ne peuvent être déterminées que par la Loi.
Art. 5. La Loi n'a le droit de défendre que les actions nuisibles à la Société. Tout ce qui n'est pas défendu par la
Loi ne peut être empêché, et nul ne peut être contraint à faire ce qu'elle n'ordonne pas.
Art. 6. La Loi est l'expression de la volonté générale. Tous les Citoyens ont droit de concourir personnellement,
ou par leurs Représentants, à sa formation. Elle doit être la même pour tous, soit qu'elle protège, soit qu'elle
punisse. Tous les Citoyens étant égaux à ses yeux sont également admissibles à toutes dignités, places et
emplois publics, selon leur capacité, et sans autre distinction que celle de leurs vertus et de leurs talents.
Art. 7. Nul homme ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi, et selon les
formes qu'elle a prescrites. Ceux qui sollicitent, expédient, exécutent ou font exécuter des ordres arbitraires,
doivent être punis ; mais tout citoyen appelé ou saisi en vertu de la Loi doit obéir à l'instant : il se rend coupable
par la résistance.
Art. 8. La Loi ne doit établir que des peines strictement et évidemment nécessaires, et nul ne peut être puni qu'en
vertu d'une Loi établie et promulguée antérieurement au délit, et légalement appliquée.
Art. 9. Tout homme étant présumé innocent jusqu'à ce qu'il ait été déclaré coupable, s'il est jugé indispensable de
l'arrêter, toute rigueur qui ne serait pas nécessaire pour s'assurer de sa personne doit être sévèrement réprimée
par la loi.
Art. 10. Nul ne doit être inquiété pour ses opinions, même religieuses, pourvu que leur manifestation ne trouble
pas l'ordre public établi par la Loi.
Art. 11. La libre communication des pensées et des opinions est un des droits les plus précieux de l'Homme : tout
Citoyen peut donc parler, écrire, imprimer librement, sauf à répondre de l'abus de cette liberté dans les cas
déterminés par la Loi.
Art. 12. La garantie des droits de l'Homme et du Citoyen nécessite une force publique : cette force est donc
instituée pour l'avantage de tous, et non pour l'utilité particulière de ceux auxquels elle est confiée.
Art. 13. Pour l'entretien de la force publique, et pour les dépenses d'administration, une contribution commune
est indispensable : elle doit être également répartie entre tous les citoyens, en raison de leurs facultés.
Art. 14. Tous les Citoyens ont le droit de constater, par eux-mêmes ou par leurs représentants, la nécessité de la
contribution publique, de la consentir librement, d'en suivre l'emploi, et d'en déterminer la quotité, l'assiette, le
recouvrement et la durée.
Art. 15. La Société a le droit de demander compte à tout Agent public de son administration.
Art. 16. Toute Société dans laquelle la garantie des Droits n'est pas assurée, ni la séparation des Pouvoirs
déterminée, n'a point de Constitution.
Art. 17. La propriété étant un droit inviolable et sacré, nul ne peut en être privé, si ce n'est lorsque la nécessité
publique, légalement constatée, l'exige évidemment, et sous la condition d'une juste et préalable indemnité.
"""

### Comptons le nombre d'occurrences de chaque mot

# On commence par créer un dictionnaire vide: les clés seront
# les mots et les valeurs seront les occurrences de ces mots
mots = dict()

# On convertie le texte en une liste de mots avec "split()"
texte_en_mots = texte.split(" ")

# On parcourt le texte mot par mot
for m in texte_en_mots:
    ### A TOI D'ECRIRE QUELQUE CHOSE ICI



# Affichons le résultat
nb_items = 10
print("Voici les " + str(nb_items) + " mots avec les "
      "plus grandes occurrences:")
compteur = 0
nb_mots = len(texte_en_mots)
for i in reversed(sorted(mots, key=mots.get)):
    pour_cent = (mots[i] * 100.0) / nb_mots
    print("{:10s}".format(i) + ": " +
          "{:4d}".format(mots[i]) + " sur " +
          "{:4d}".format(nb_mots) + " au total soit " +
          "{:3.1f}".format(pour_cent) + "%")
    compteur += 1
    if compteur == nb_items:
        break


### Comptons le nombre d'occurrences de chaque lettre

# On commence par créer un dictionnaire vide: les clés seront
# les caractères et les valeurs seront les occurrences de
# ces caractères.
lettres = dict()

# On parcourt le texte caractère par caractère
for c in texte:
    ### A TOI D'ECRIRE QUELQUE CHOSE ICI

print("\n")
print("Voici les " + str(nb_items) + " caractères avec les "
      "plus grandes occurrences:")
compteur = 0
nb_caractères = len(texte)
for i in reversed(sorted(lettres, key=lettres.get)):
    pour_cent = (lettres[i] * 100.0) / nb_caractères
    print("'" + i + "'       : " +
          "{:4d}".format(lettres[i]) + " sur " +
          "{:4d}".format(nb_caractères) + " au total soit " +
          "{:3.1f}".format(pour_cent) + "%")
    compteur += 1
    if compteur == nb_items:
        break

```


## Créons le "petit générateur d'histoires"

:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Nous allons créer un programme qui va s'appeler **"le petit générateur d'histoires"**. Pour cela, pourrais-tu s'il te plaît, créer un programme (**"histoires.py"**) qui va **générer des histoires différentes à chaque exécution**: Par exemple, un même personnage est un héro grand costaux dans une histoire, un méchant dans une autre et le roi dans une troisième :smile:. Pour cela, nous allons utiliser un peu tout ce qu'on a appris jusqu'à maintenant: les listes, les dictionnaires, les nombres aléatoires, la manipulation de chaînes de caractères, les boucles... Je te propose le code ci-dessous, et tu vas devoir compléter partout où il est écrit `### A TOI D'ECRIRE QUELQUE CHOSE ICI`. N'hésite pas à modifier ma proposition pour la rendre plus jolie et plus amusante :smile::
```Python
```


# Tu peux jouer avec la `Tortue graphique` :turtle:
Le langage **Tortue graphique** (on dit aussi **LOGO**[^10]) est un langage de programmation très simple permettant de **programmer un dessin** à l'aide de mouvements simples comme lever/descendre/avancer/tourner... le crayon. Le *crayon virtuel*, qu'on ne voit pas, est assimilé à une  *tortue virtuelle*, qu'on ne voit pas non plus, oui, c'est dommage, mais ça reste amusant quand même de programmer des dessins simples :smile:.
 [^10]: [L'article Wikipedia sur le langage LOGO (ou tortue)](https://fr.wikipedia.org/wiki/Logo_(langage)).

- [ ] Essaye le programme suivant:
```Python
# Nom de la bibliothèque pour dessiner avec la tortue
from turtle import *

# Au départ, la tortue est au centre de l'écran en (0, 0)
# Dessinons un carré (on avance, on tourne à droite de 90°...)
taille_carre = 100
forward(taille_carre) # On avance (contraire = backward)
right(90)             # On tourne à 90° (contraire = left)
forward(taille_carre)
right(90)
forward(taille_carre)
right(90)
forward(taille_carre)
right(90)

# On se déplace dans le coin bas gauche mais on lève
# le crayon avant sinon on dessinera un trait
penup()               # On monte le crayon
goto(-100, -100)      # On se déplace en (-100, -100)

# Dessinons un cercle
circle(50)            # Cercle de taille 50

# Zut, on a oublié de descendre le crayon avant et on
# a dessiné dans le vide. Bon, on refait le cercle
# mais en bleu pour le bord, rouge pour l'intérieur
pendown()             # On descend le crayon
color('blue', 'red')  # Bord en bleu, intérieur en rouge
begin_fill()          # On "active" le remplissage
circle(50)            
end_fill()            # On "désactive" le remplissage

# On revient au centre (home = maison)
penup()
home()                # Retour à la maison

# Dessinons lentement et en plus gros... et avec une tortue!
speed(1)             # vitesse: 1 lent... 10 rapide, 0 whaou
pensize(5)           # épaisseur du trait, 10 gros
shape('turtle')      # On change le triangle pour une tortue
write('Coucou!',     # On écrit un message
      move=True,     # False=on bouge pas, True=on bouge
      align='left',  # alignement left, right ou center
      font=('Arial', 20, "bold"))

title('Bravo!')      # On change le titre de la fenêtre

# Tu veux en savoir plus? On peut interagir avec
# l'utilisateur (clavier, souris, questions...):
# * souris: onclick(), onrelease() et ondrag().
# * clavier: onkeypress(), onkeyrelease()...
# * poser des questions: numinput(), textinput()

# A toi de jouer avec tout cela, prend ton temps de découvrir
# d'abord les choses simples puis les plus compliquées...
```


> :heavy_plus_sign: Il existe de nombreuses commandes, mais je t'invite plutôt à aller lire la documentation sur le langage graphique [Tortue en Python](https://docs.python.org/fr/3/library/turtle.html), il y a un peu d'anglais mais tu devrais t'en sortir, demande moi si besoin. Il existe aussi une **Cheatsheet** :open_book:, soit **une feuille pour tricher** (to cheat = tricher, a sheet = une feuille)... bon, ce n'est pas pour tricher mais pour **résumer la liste des fonctions possibles**, on appelle cela aussi un **memento**. Tu retrouveras celle pour le langage tortue dans la rubrique [en bas de ce document](#liens-utiles-pour-python-snake), c'est très pratique les cheatsheets :smile:!


:construction: :construction: :construction: **A ton tour de construire** :construction: :construction: :construction:
- [ ] **Petit défi**: Nous allons créer un programme qui va s'appeler **"tortue_drapeaux.py"**) et qui va **dessiner des drapeaux de différents pays**: chaque drapeau sera dans une fonction différente qui aura 4 paramètres: longueur et hauteur du drapeau, coordonnées X et Y de sa position. Ainsi, on pourra facilement redessiner le drapeau. Ton programme aura aussi plusieurs autres fonctions: une pour dessiner un rectangle plein, une pour un rond plein, une pour dessiner une étoile pleine à 5 branches... et ainsi, les fonctions pour dessiner les drapeaux pourront faire appellent à ces fonctions rectangle, rond, étoile... A toi de choisir tes drapeaux préférés dans la liste des [drapeaux sur Wikipedia](https://fr.wikipedia.org/wiki/Galerie_des_drapeaux_des_pays_du_monde). Commence par dessiner les plus simples d'abord, comme celui de la France :fr:, de l'Allemagne :de: ou du Japon :jp: :smile:.

```Python
!!!
```


C'est cool le langage :turtle:, tu es super fort :muscle:, bravo :smile:.


Maintenant que tu connais la **tortue graphique**, tu peux t'amuser à:
- dessiner une maison, une ville avec des immeubles de différentes tailles...
- dessiner un personnage, un flocon de neige, une voiture de sport...
- et tout ce que tu veux :)


Je ne résiste pas à te montrer des créations artistiques utilisant le même principe, sur le site de [turtletoy.net](https://turtletoy.net/turtle). Tu peux t'amuser à convertir d'ailleurs les créations dans le langage tortue graphique que tu viens d'apprendre, commence peut être par des simples comme [l'étoile par défaut](https://turtletoy.net/turtle/new), mais c'est toi qui voit, surtout, prends ton temps, amuse toi, et partage tes créations :smile:.


# Créons le jeu "Le défi des Aires"
!!!
Programmer un duel des aires ? Zone de scores en temps reel avec prenoms des joueurs et lancé de dês, chaquun place a la souris ou au clavier son aire qui est rouge ou verte si on peut la deposer, avec verif si il reste de la place qq part... Tableau en 2 dimensions pour les cases
Afficher et effacer la zone du haut
Afficher les cases vide ou appartenant a chacun des joueurs...
Faire un algo qui recherche une place dans les cases vides afin d'éviter souris et clavier ou bien trouver un solution pour bouger une aire au clavier car a la souris c'est plus compliqué...


# Pour aller plus loin...
On peut faire tellement de choses avec un langage de programmation! Maintenant que tu connais un peu mieux le langage Python, tu pourrais:
* Programmer d'autres petits jeux :video_game: avec la **tortue graphique** :turtle:.
* Programmer tes constructions dans **MineCraft** ou dans **MineTest**.
* Faire un jeu :video_game: avec [Godot](https://godotengine.org/), pour cela, tu peux commencer à suivre le tutoriel pour [faire un petit jeu avec Godot](https://docs.godotengine.org/fr/latest/getting_started/step_by_step/your_first_game.html), ce n'est pas complètement du Python mais c'est très proche et cela permet de créer de supers jeux :video_game: !


# Quelques liens intéressants
## Ascii Art
*"L’art ASCII consiste à réaliser des images uniquement à l'aide des lettres et caractères spéciaux contenus dans le code ASCII"*[^20].
[^20]: [L'article Wikipedia sur l'art ASCII](https://fr.wikipedia.org/wiki/Art_ASCII).

* Sur une seule ligne: [1 Line Art](https://1lineart.kulaone.com) ou [ASCII Art Archive (one line)](https://www.asciiart.eu/ascii-one-line)

* Sur plusieurs lignes: [ASCII Art Archive (avec moteur de recherche)](https://www.asciiart.eu/) ou [Ascii art collection](https://asciiart.website/)
:bulb: Le serpent tout en haut de la page vient de [là](https://www.asciiart.eu/animals/reptiles/snakes).

* Générateur de beaux textes: [Text to ASCII Art Generator (TAAG)](
http://patorjk.com/software/taag/#p=display&f=Big&t=Tape%20ton%20texte%20ici!).
:bulb: Pour voir toutes les possibilités, tu peux cliquer sur `Test All`, c'est très pratique!

* Divers
  * La page Wikipedia sur l'art ASCII: [Wikipedia art ASCII](https://fr.wikipedia.org/wiki/Art_ASCII)
  * Quelques autres liens: [The incredibleart ascii](https://www.incredibleart.org/links/ascii.html)


## Liens utiles pour Python :snake:
* Le **tutoriel Python officiel**: c'est là qu'il faut commencer car il est très bien!
  * [Le tutoriel Python officiel](https://docs.python.org/fr/3/tutorial/index.html): c'est le sommaire, commence par là :-)!
  * [Les chaînes de caractères](https://docs.python.org/fr/3/tutorial/introduction.html#strings)
  * [Les tests if elif else](https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements)
  * [Les fonctions](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)
  * [Le style de codage Python](https://docs.python.org/fr/3/tutorial/controlflow.html#intermezzo-coding-style)
  * [Les listes](https://docs.python.org/fr/3/tutorial/introduction.html#lists)
  * [La boucle for](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements)
  * [Les exceptions avec try except finally](https://docs.python.org/fr/3/tutorial/errors.html)
  * [Les classes](https://docs.python.org/fr/3/tutorial/classes.html)
  * [Les dictionnaires](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)
  * [Quelques fonctions de la bibliothèque standard](https://docs.python.org/fr/3/tutorial/stdlib.html): [la date et le temps](https://docs.python.org/fr/3/library/datetime.html), [les nombres aléatoires avec random()](https://docs.python.org/fr/3/library/random.html), [la mesure du temps et les pauses](https://docs.python.org/fr/3/library/time.html)

* Le langage graphique [Tortue en Python](https://docs.python.org/fr/3/library/turtle.html).

* Les **Cheat sheets** Python (ou résumé des principales commandes sur une seule feuille):
  * Cheatsheet pour le langage Python: [lien direct vers le pdf](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf) ou le lien vers la [page du site](https://perso.limsi.fr/pointal/python:memento).
  * Cheatsheet pour le langage Python **Tortue**: [lien direct vers le pdf](https://perso.limsi.fr/pointal/_media/python:turtle:turtleref.pdf) ou le lien vers la [page du site](https://perso.limsi.fr/pointal/python:turtle:accueil).

* Voici un autre très bon tutoriel Python mais en anglais: [w3schools.com](https://www.w3schools.com/python/default.asp).

* Et un dernier mais en français: [python.doctor](https://python.doctor/).
