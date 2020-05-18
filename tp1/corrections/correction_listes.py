# On va utiliser des fonctions de la bibliothèque
# qui s’appelle "random" (hasard)
import random

# Liste des marques de voitures
marques = ['Bugatti', 'Renault', 'Peugeot', 'Citroen',
           'Dacia', 'Ferrari', 'Audi', 'BMW', 'Fiat']

print('Es-tu prêt pour jouer à')
print('Devine la marque de voitures que j\'ai en tête :-)')
print('Ok, alors c\'est parti!')

mon_choix = random.choice(marques)
# La ligne suivante est juste pour le debuggage
# print(mon_choix)

print('J\'ai choisi une marque, à toi de la deviner!')
print('euh, si c\'est trop dur, tape "Abandon" ;-)')


compteur_aide = 0
compteur_lettre = 0
compteur_proposition = 0
on_sort_du_while = 0

while on_sort_du_while == 0:    
    # met ton code ici avec le input()...
    # n'oublie pas l'indentation du bloc de code du while

    if compteur_aide >= 2:
        # TODO il faudrait vérifier que compteur_lettre
        # ne va pas au delà de mon_choix...
        print('Petit indice, la lettre', compteur_lettre + 1,
              'est', mon_choix[compteur_lettre])
        compteur_aide = 1
        compteur_lettre += 1
    else:
        compteur_aide += 1

    compteur_proposition += 1
    proposition = str(input('Quelle est ta proposition? '))

    # dans le code du bloc du while, si
    # le joueur a trouvé ou abandonné, il te suffit
    # de mettre "on_sort_du_while = 1" pour sortir du while
    if proposition.lower() == mon_choix.lower():
        print('Bravo, tu as trouvé en', compteur_proposition,
              'coups, tu es un champion!')
        on_sort_du_while = 1

    if proposition.lower() == 'Abandon'.lower():
        print('Oh, tu abandonnes :-( C\'était trop dur?')
        print('La réponse était:', mon_choix)
        on_sort_du_while = 1       
        

# Ici on est sorti du while, ajoute ton code de sortie du jeu
print('A bientôt :-)')
