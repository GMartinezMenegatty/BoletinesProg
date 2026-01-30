#1
numeros = (10,11,12,13,14,15,16,17,18,19,20)

i = 0
suma = 10
for numero in numeros:
    print (numero)


for i, numero in enumerate(numeros):
    print (i)
    print (numero)
    print (numeros[i])

#2
print ("---")
#def CelsiusFahrenheit (temperatura):
    #return 9/5 * temperatura + 32

temperatura = float(input("Digite sua temperatura em Celsius: "))

f = 9/5 * temperatura + 32
print (f)

#3
print ("---")

tF = 0

i = 0

#while (tF <= 120):
 #   tc = (5/9) * (tF - 32)
  #  print(tc)
   # i = i + 1
    #tF = tF + 10

for tF in range(0, 121, 10): #desde 0, hasta 121, con incrementos de 10 en 10
    tc = (5/9) * (tF - 32)
    print(tF, tc)

#4
print ("---")

primernumero = int(input("Digite el primer número: "))
segundonumero = int(input("Digite el segundo número: "))
 
for numero in range(primernumero, segundonumero + 1):
     if numero % 2 == 0:
         print(numero)

#5
print ("---")

n = int(input("Introduce el valor de n: "))
triangular = 0
for i in range(0, n + 1):
    triangular += i
    print(f"{i} - {triangular}")

n = int(input("Introduce el valor de n: "))
for i in range(0, n + 1):
    triangular = i * (i + 1) // 2
    print(f"{i} - {triangular}")

#el segundo es mas eficiente

#6
print ("---")

def leer_valores(m):
    
    valores = []
    for i in range(m):
        valor = int(input(f"Ingrese el valor #{i + 1}: "))
        valores.append(valor)
    return valores

def calcular_factorial(n):
   
    if n < 0:
        return None  
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def imprimir_resultados(valores):
    
    for i, val in enumerate(valores):
        fact = calcular_factorial(val)
        if fact is not None:
            print(f"{i + 1}. El factorial de {val} es {fact}")
        else:
            print(f"{i + 1}. El factorial no está definido para {val}")

def main():
    m = int(input("¿Cuántos valores deseas ingresar? "))
    valores = leer_valores(m)
    imprimir_resultados(valores)


main()


#7
print ("---")

for ficha1 in range(7):
    for ficha2 in range(ficha1, 7):
        print(f"({ficha1}, {ficha2})")

#8  
print ("---")

n = int(input("Introduce el valor de n: "))
for ficha1 in range(0, n):
    for ficha2 in range(ficha1, n + 1):
        print(f"({ficha1}, {ficha2})")

#9
print ("---")

negativos = positivos = ceros = 0
for i in range(10):
    num = int(input(f"Introduce un número {i + 1}: "))
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        ceros += 1

print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")
print(f"Ceros: {ceros}")

#10
print ("---")

base = int(input("Introduce la base del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))

while base <=0 or altura <=0:
    print("La base y la altura deben ser números positivos.")
    base = int(input("Introduce la base del rectángulo: "))
    altura = int(input("Introduce la altura del rectángulo: "))
else:
    area = base * altura
    print(f"Área: {area}")
    
#11
print ("---")

while True:
    num = int(input("Introduce un número (pulse 0 para salir): "))
    if num == 0:
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
#12
print ("---")

trabajadores = 0
sueldo1000 = 0
sueldo_1000 = 0

while True:
    sueldo = int(input("Introduce un número (pulse 0 para continuar): "))
    if sueldo == 0:
        break
    if sueldo < 0:
        print("Número negativo, intente de nuevo.")
        continue
    trabajadores += 1
    if sueldo >= 1000 <= 1750:
        sueldo1000 += 1
    elif sueldo < 1000:
        sueldo_1000 += 1

if trabajadores > 0:
    porcentaje_1000 = (sueldo_1000 / trabajadores) * 100
    print(f"trabajadores que ganan 1000 a 1750: {sueldo1000}")
    print(f"trabajadores que ganan menos de 1000: {sueldo_1000}")
    print(f"porcentaje de trabajadores que ganan menos de 1000: {porcentaje_1000:}%")
else:
    print("No se ingresaron datos de trabajadores.")

#13
print ("---")

n = int(input("Introduce el valor de n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

#14
print ("---")

suma = 0
for i in range(10):
    num = int(input(f"Introduce un número {i + 1}: "))
    if num == 999:
        break
    suma += num
print(f"La suma total es: {suma}")
