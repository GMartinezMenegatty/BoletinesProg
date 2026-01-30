loteria = []

for numero in range(1, 7):
    valor = int(input("Ingresa el numero de "+str(numero) + ": "))
    loteria.append(valor)
loteria.sort()
print(loteria)