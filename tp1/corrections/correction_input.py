print("Bienvenue à")
print("************************************")
print("*** Tu mets qui dans ta poubelle ***")
print("*** sous les épluchures pourries ***")
print("************************************")

print("J'ai besoin de 3 prénoms de tes ami(e)s stp")

prenoms = []

for i in range(3):
    prenom = input("Prénom de l'ami(e) " + str(i + 1) + ": ")
    prenoms.append(prenom)

print(prenoms)

print("Qui tu amènes danser dans ta Ferrari?")
msg = ""
for i in range(len(prenoms)):
    msg += str(i + 1) + ") " + prenoms[i] + "    "

print(msg)

numero = int(input("Réponse: "))
prenoms.pop(numero - 1)

print("Avec qui tu vas manger une glace?")
msg = ""
for i in range(len(prenoms)):
    msg += str(i + 1) + ") " + prenoms[i] + "    "

print(msg)

numero = int(input("Réponse: "))
prenoms.pop(numero - 1)

print("Et bien c'est " + prenoms[0] + " que tu mets dans "
      "une poubelle avec des épluchures pourries! "
      "Ah, Ah, Ah")
