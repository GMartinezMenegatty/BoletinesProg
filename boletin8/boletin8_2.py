#Escribir unha función que indique si duas fichas de dominó encaixan ou non.
#  As fichas son recibidas en duas tuplas, por exemplo: (3,4) e (5,4).
#  A función devolta un booleano co resultado do encaixe

def fichas_encajan(ficha1, ficha2):
    return ficha1[0] in ficha2 or ficha1[1] in ficha2

ficha1 = input("Introduce la primera ficha: ")
ficha2 = input("Introduce la segunda ficha: ")

ficha1 = tuple(int(x) for x in ficha1.split(','))
ficha2 = tuple(int(x) for x in ficha2.split(','))

if all(1 <= x <= 6 for x in ficha1 + ficha2):
    if fichas_encajan(ficha1, ficha2):
        print(True)
    else:
        print(False)
else:
    print("Los valores deben estar entre 1 y 6.")
