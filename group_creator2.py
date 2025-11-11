import random

person = ["David", "Sergio", "Jorge", "Santiago", "Héctor", "Diego", "Marco", "Ginebra", "Izaro", "Nerea", "Rojo", "Adrián"]

x = int(input("Please insert the number of integrants of the group: "))

grupos_random = []
grupos_random.append()
aux_grupos_random = 0

while person:
    random.shuffle(person)
    if len(grupos_random[aux_grupos_random]) < group_size:
        grupos_random[aux_grupos_random].append(person.pop())
    
    else:
        aux_grupos_random += 1
        grupos_random.append([])
        grupos_random[aux_grupos_random].append(person.pop())

for grupo in grupos_random:
    if len(grupo) == 1:
        grupos_random

    else:
        


