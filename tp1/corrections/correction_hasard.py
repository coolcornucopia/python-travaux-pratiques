# On aura besoin de la bibliothèque des nombres aléatoires
import random

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
    # on vérifie d'abord si les paramètres sont corrects
    if de1 not in range(1, 7) or de2 not in range(1, 7):
        print("Les dés doivent être entre 1 et 6!")
        return
    for h in range(des_hauteur):
        ligne = des[h]
        # On prépare le premier dé
        pos = (de1 - 1) * des_largeur
        chaine = ligne[pos : pos + des_largeur]
        # On ajoute un peu d'espaces entre les 2 dés
        chaine += "     "
        # On prépare le second dé
        pos = (de2 - 1) * des_largeur
        chaine += ligne[pos : pos + des_largeur]
        # Et on affiche la ligne avec les 2 dés puis on
        # passe à la ligne suivante
        print(chaine)


# Petit test de notre fonction d'affichage des 2 dés
# en ascii art
# Tu peux retirer les commentaires des lignes suivantes
# pour tester l'affichage
#for i in range(1, 7):
#    affiche_2_des(i, 7 - i)

# Petite fonction qui retourne les valeurs de 2 dés et
# les affiche
def lance_et_affiche_2_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
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
    print("Appuie sur ENTREE")
    i = input()
    print("\n" * 100)

    if a_qui == ordi:
        print("A mon tour, je lance les dés...")
    else:
        print("A ton tour, lance les dés en appuyant sur ENTREE...")
        i = input()

    # On tire les 2 dés et on les affiche
    de1, de2 = lance_et_affiche_2_des()
    lancer = de1 * de2

    if de1 == de2:
        print("DOUBLE!!!")
        lancer *= 2   

    points[a_qui] += lancer

    if a_qui == ordi:
        print("J'ai fais " + str(lancer) +
              ". J'ai maintenant...")
    else:
        print("Tu as fais " + str(lancer) +
              ". Tu as maintenant...")
    
    affiche_nums(points[a_qui])

    # On vérifie si le joueur en cours à gagner
    # Si oui, on sort du while
    if points[a_qui] >= 100:
        break

    # On change de joueur
    if a_qui == ordi:
        a_qui = joueur
    else:
        a_qui = ordi


# On affiche le nom du gagnant puis on dit au revoir
if a_qui == ordi:
    print("YOUPI, J'AI GAGNE :-)")
else:
    print("ZUT, TU AS GAGNE, BRAVO :-)")

print("Reviens vite jouer avec moi :-)")
