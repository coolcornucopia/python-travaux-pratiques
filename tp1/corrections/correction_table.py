# fonction pour aligner à droite un nombre entre 0 et 999
# inclus sur 4 caractères dont le premier est un espace
# Note: il était possible de faire cela simplement avec
#       "return '{:>4}'.format(val)"
def align4(val):
    # traitons d'abord les valeurs incorrectes
    if val > 999 or val < 0:
        return ' !!!'
    elif val < 10:
        return '   ' + str(val)
    elif val < 100:
        return '  ' + str(val)
    else:
        return ' ' + str(val)

# Voici la table de référence
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

# Générons maintenant notre table
# on prépare d'abord la première ligne
ligne = '   x'
for x in range(11):
    ligne += align4(x)

table2 = ligne + '\n'

for x in range(11):
    ligne = align4(x)
    for y in range(11):
        ligne += align4(x * y)
    table2 += ligne + '\n'

print(table2)

# Comparons les deux tables
if table1 == table2:
    print('Bravo, ce sont les mêmes :-)')
else:
    print('Désolé, il doit y avoir une petite erreur :-(')
