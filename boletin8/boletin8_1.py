#Escribir unha función que reciba unha tupla de elementos e indique si 
#se encontran ordeados de menor a maior ou non.

def esta_ordenada(tupla):
    for i in range(len(tupla) - 1):
        if tupla[i] > tupla[i + 1]:
            return False
    return True

valores = input("Introduce los elementos separados por comas: ")

tupla = tuple(int(n.strip()) for n in valores.split(','))

if esta_ordenada(tupla):
    print (True)
else:
    print(False)
