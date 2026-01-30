#Dada unha lista de números enteiros, escribir unha función que:
#Devolte unha lista con tódolos que sexan primos.
#Devolte o sumatorio e o promedio dos valores.
#Devolte unha lista co factorial de cada un de eses números.
import math

enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def calcularNumeros (enteros):
    primos = []
    for n in enteros:
        if n > 1:
            e_primo = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    e_primo = False
                    break
            if e_primo:
                primos.append(n)

    suma = sum(enteros)
    promedio = suma / len(enteros)
    factoriales = [math.factorial(n) for n in enteros]

    return suma, promedio, primos, factoriales

suma, promedio, primos, factoriales = calcularNumeros(enteros)
print(suma)
print(promedio)
print(primos)
print(factoriales)
