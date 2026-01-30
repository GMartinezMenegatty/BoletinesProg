entrada = input("Introduce números separados por comas: ")

numeros = []
numero = ""

for caracter in entrada:
    if caracter == ",":
        numeros.append(float(numero))
        numero = ""
    else:
        numero += caracter

numeros.append(float(numero))

contador = 0
for n in numeros:
    contador += 1

suma = 0
for x in numeros:
    suma += x

media = suma / contador

suma_cuadrados = 0
for x in numeros:
    suma_cuadrados += (x - media) ** 2

desviacion = (suma_cuadrados / contador) ** 0.5

print("Media:", media)
print("Desviación típica:", desviacion)
