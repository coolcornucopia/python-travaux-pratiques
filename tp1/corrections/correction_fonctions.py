# La fonction "fievre()" revoie un message indiquant
# si on a de la fièvre, en fonction de sa température
# et du seuil de fièvre (généralement 38.5°C pour un
# adulte et 38.1°C pour un bébé de moins de 1 an).
def fievre(temperature, seuil = 38.5):
    if temperature > seuil:
        print('tu as de la fièvre :-(')
    else:
        print('tu n\'as pas de fièvre :-)')

# On teste la fonction avec un ou plusieurs paramètres
fievre(39.1)
fievre(37.2)
fievre(38.4, 38.1)
