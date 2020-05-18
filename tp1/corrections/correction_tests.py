# La taille de mon animal préférée, je peux la changer
# afin de tester mon programme
taille_mon_animal = 6.4

# Les tailles des autres animaux
taille_lion = 1.2
taille_elephant = 3.2
taille_girafe = 6.1

msg_mon_animal = 'Mon animal préféré (' + \
                 str(taille_mon_animal) + 'm) '

msg_lion = 'un lion (' + str(taille_lion) + 'm)'
msg_elephant = 'un éléphant (' + str(taille_elephant) + 'm)'
msg_girafe = 'une girafe (' + str(taille_girafe) + 'm)'

msg_petit = ' plus petit qu\''
msg_aussi = ' aussi grand qu\''
msg_grand = ' plus grand qu\''

if taille_mon_animal < taille_lion:
    print(msg_mon_animal + 'est' + msg_petit + msg_lion +
          '.')
    
elif taille_mon_animal == taille_lion:
    print(msg_mon_animal + 'est' + msg_aussi + msg_lion +
          '.')
    
elif taille_mon_animal < taille_elephant:
    print(msg_mon_animal + 'est' + msg_grand + msg_lion +
          ' mais' + msg_petit + msg_elephant + '.')
    
elif taille_mon_animal == taille_elephant:
    print(msg_mon_animal + 'est' + msg_grand + msg_lion +
          ' mais' + msg_aussi + msg_elephant + '.')
    
elif taille_mon_animal < taille_girafe:
    print(msg_mon_animal + 'est' + msg_grand + msg_elephant +
          ' mais' + msg_petit + msg_girafe + '.')
    
elif taille_mon_animal == taille_girafe:
    print(msg_mon_animal + 'est' + msg_grand + msg_elephant +
          ' mais' + msg_aussi + msg_girafe + '.')
else:
    print(msg_mon_animal + 'est' + msg_grand + msg_girafe +
          '.')

