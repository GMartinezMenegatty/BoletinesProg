#Dada unha lista de números enteiros e un enteiro k, escribir unha función que:
#Devolte tres listas, unha cos menores, outra cos maiores e outra cos iguais a k.
#Devolte unha lista con aqueles que son múltiplos de k.

def consultarNumeros (enteros, k):
    menores = []
    mayores = []
    igual = []
    multiplos = []
    for entero in enteros:
        if entero < k:
            menores.append(entero)
        elif entero > k:
            mayores.append(entero)
        else:
            igual.append(entero)
        if entero % k == 0:
            multiplos.append(entero)

    return menores, mayores, igual, multiplos

enteros = [2, 3, 4, 5, 6, 7, 8]
k = 5

menores, mayores, igual, multiplos = consultarNumeros (enteros, k)

print(menores)
print(mayores)
print(igual)
print(multiplos)


