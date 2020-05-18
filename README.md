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

# Python - Travaux Pratiques
[Python](https://fr.wikipedia.org/wiki/Python_(langage)) est le nom d'un **langage de programmation**, très utilisé dans beaucoup de domaines: internet, intelligence artificielle, analyse de données, électronique[^1]... et MineCraft[^2]!
[^1]: Python pour l'électronique avec [MicroPython](https://micropython.org).
[^2]: Exemples de [Python avec MineCraft ](https://www.instructables.com/id/Python-coding-for-Minecraft/).

Le but de ces travaux pratiques ("TP") est que l'enfant (ou l'adulte) apprenne **quelques notions de programmation** comme les chaînes de caractères, les variables, les listes, les conditions, les boucles, les classes... et cela, **tout en s'amusant et en découvrant le formidable langage Python** :smile:...

# Notes pour l'encadrant/parent/enseignant
Pour le moment, il y a les travaux pratiques suivants:
* tp1:

Note: les informations suivantes fonctionnent sous Linux ET sous Windows, tout comme le TP lui-même :-)

## Pour quel age? Combien de temps?...
Environ pour un enfant de 10 ans, mais cela varie beaucoup. Il faut au moins avoir son [passeport b2i](http://monecole.fr/monB2i/).

Pour la durée, la aussi c'est très variable, je préfère que l'enfant prenne son temps à essayer plutôt qu'il soit sous la contrainte d'avoir à finir au bout d'un temps donné, je préfère qu'il en fasse moins mais qu'il ait mieux compris et qu'il se soit plus amusé à créer avec ce qu'il a appris...

## Configurer l'éditeur
Le choix de l'éditeur est ici celui par défaut dans Python soit "IDLE" car je n'ai rien trouvé de plus simple.
* L'installation sous windows contient IDLE par défaut.
* Sous linux, il faut faire ```sudo apt-get install idle-python```

Configuration (menu Options/Configure IDLE):
* Police de caractères de taille 12 (je préfère que ça soit bien lisible)
* thème "IDLE Dark" (quelques notes sur ce point un peu plus bas)
* "At Startup" = "Open Edit Window" (pour pouvoir taper directement un programme)
* "At Start of Run (F5)" = "No Prompt" (éviter d'avoir des questions à chaque fois)
* "Auto-Squeeze Min. Lines" = "200" (pour pouvoir afficher des grandes images en ascii art)

## Convertir "Travaux pratiques sur Python" du markdown en html
Pour une utilisation **hors ligne**, il est possible de générer un fichier html ou pdf.

La syntaxe [markdown de github](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) est utilisée.

Pour la conversion en pdf ou en html, j'utilise l'éditeur [atom.io](https://atom.io/) avec le package [markdown-preview-enhanced](https://atom.io/packages/markdown-preview-enhanced) dont la procédure d'installation se trouve [ici](https://shd101wyy.github.io/markdown-preview-enhanced/#/installation).

Comme l'éditeur IDLE utilise un thème "Dark", je souhaitais que le fichier html soit lui aussi avec le thème Dark de github, pour cela, dans atom, menu "preferences", Packages,  markdown-preview-enhanced, Settings et mettre le "Preview Theme" à "github-dark.css" + cocher "Print Background".

Ce package contient une aide sur la syntaxe markdown très complète [ici](https://shd101wyy.github.io/markdown-preview-enhanced/#/markdown-basics) ainsi que le support de nombreux graphiques (ditaa, Graphviz, PlantUML) et formats de sortie (pdf, html, ebook, png...).

Note: le résultat des émoticons est plus joli avec Chrome qu'avec Firefox mais c'est discutable :-)

> :warning: Avant la génération finale, ne pas oublier de générer le sommaire en haut du document.

## dark mode ou light Module
Je préfère le dark mode comme décrit ci-dessus mais on peut aussi faire du light mode en suivant 'à l'inverse' la description des 2 paragraphes ci-dessus.
Note: Il n'y a pas vraiment d'avantages ni de désavantages entre les deux, cf l'article suivant https://www.nngroup.com/articles/dark-mode/

## Imprimer les cheat sheets Python
Si vous le souhaitez, vous pouvez imprimer les cheat sheets Python et les donner aux élèves, c'est vous qui voyez... mais **je ne le recommande pas pour le tp1** car les cheatsheets restent pour un usage plus régulier et non pour une découverte de la programmation...

* Les **Cheat sheets** Python (ou résumé des principales commandes sur une seule feuille):
  * Cheatsheet pour le langage Python: [lien direct vers le pdf](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf) ou le lien vers la [page du site](https://perso.limsi.fr/pointal/python:memento).
  * Cheatsheet pour le langage Python **Tortue**: [lien direct vers le pdf](https://perso.limsi.fr/pointal/_media/python:turtle:turtleref.pdf) ou le lien vers la [page du site](https://perso.limsi.fr/pointal/python:turtle:accueil).

## personnaliser les travaux pratiques
Je trouve cela sympa de **personnaliser les travaux pratiques**, pour cela:
* Remplacer le prénom "Ethan/ethan" par celui de l'élève (attention aux majuscules/minuscules).
* Remplacer le prénom "Anna/anna" par celui de la sœur ou du frère de l'élève (attention aux majuscules/minuscules), adapter au mieux à la fratrie...
* Remplacer la date d'anniversaire `anniv = date(2009, 11, 13)` par celle de l'élève.
* Remplacer le sport `a['sport'] = 'gym'`, l'instrument de musique `a['instrument'] = 'saxophone'`...
* Ajouter des ascii arts qui plaisent à l'élève...
