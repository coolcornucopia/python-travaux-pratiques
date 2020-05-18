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
def affiche_en_couleurs(couleur, texte):
    idle.write(texte, couleurs[couleur])

arc_en_ciel = ["rouge", "orange", "vert", "bleu", "mauve"]

def affiche_en_arc_en_ciel(texte):
    i = 0
    inc = 1
    for c in texte:
        # On ne change pas de couleur si c'est un espace
        # afin de voir toutes les couleurs de l'arc en ciel
        # dans le texte.
        if c == ' ':
            affiche_en_couleurs("blanc", c)
            continue # on poursuit la boucle au départ
        else:
            affiche_en_couleurs(arc_en_ciel[i], c)

        # On passe à la couleur suivante de l'arc en ciel
        # soit en incrémentant ou décrémentant la couleur
        # on fait donc 0 1 2 3 4 3 2 1 0 1 2 3 4 3 2 ...
        i += inc
        if i == len(arc_en_ciel):
            inc = -1
            i = len(arc_en_ciel) - 2
        elif i < 0:
            inc = 1
            i = 1

### AJOUTE TES EXEMPLES D'UTILISATION DE TES FONCTIONS ICI
affiche_en_couleurs("bleu", "coucou\n")
affiche_en_couleurs("orange", "coucou\n")
affiche_en_arc_en_ciel("------------------------\n")
affiche_en_arc_en_ciel("------------------------\n")
affiche_en_arc_en_ciel("------------------------\n")
affiche_en_arc_en_ciel("Oh le bel Arc En Ciel!!!\n")

