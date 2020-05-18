from datetime import date, datetime

# Passage en dates françaises
import locale
locale.setlocale(locale.LC_ALL, '')

# la fonction suivante aligne à droite sur 2 caractères
# une valeur entre 1 et 31. On pourrait faire autrement
# mais c'est amusant de faire des fonctions :-)
def align2(val):
    if val < 10:
        return " " + str(val)
    else:
        return str(val)


print("Bonjour, je vais afficher le calendrier du "
      "mois de votre choix :-)")

date_str = input("Entrer un mois sous la forme mm/aaaa: ")
date_utilisateur = datetime.strptime(date_str, '%m/%Y')

annee = date_utilisateur.strftime("%Y")
mois = date_utilisateur.strftime("%B")

print("Calendrier " + annee + " - " + mois)
print("lun mar mer jeu ven sam dim")

# Creation d'une liste contenant " -" dans chaque case
jours = []
for i in range(7 * 6):
    jours.append(" -")

# Déterminons le 1er jour du mois (0=dim, 1=lun..., 6=sam)
jour1 = int(date_utilisateur.strftime("%w"))

# Nous voulons que le premier jour soit un lundi donc
# on convertie de 0=dim, 1=lun... à 0=lun, 2=mar...
# Pour cela, on fait -1 pour tous les jours sauf le dimanche
if jour1 > 0:   # cas des autres jours que dimanche
    jour1 -= 1
else:           # cas du dimanche
    jour1 = 6

# Déterminons le nombre de jours dans le mois
# pour cela on calcule le nombre de jours entre le 1er
# du mois et le 1er du mois suivant
date_mois_prochain = datetime(date_utilisateur.year,
                              date_utilisateur.month + 1,
                              date_utilisateur.day)
nb_jours_dans_mois = date_mois_prochain - date_utilisateur

# On remplie à nouveau notre liste
for i in range(nb_jours_dans_mois.days):
    jours[i + jour1] = align2(i + 1)

# On affiche notre liste
compteur = 0
for i in range(6):
    txt = ""
    for j in range(7):
        txt += " " + jours[compteur] + " "
        compteur += 1
    print(txt)
