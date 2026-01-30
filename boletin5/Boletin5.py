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

while (tF <= 120):
    tc = (5/9) * (tF - 32)
    print(tc)
    i = i + 1
    tF = tF + 10

for tF in range(0, 121, 10): #desde 0, hasta 121, con incrementos de 10 en 10
    tc = (5/9) * (tF - 32)
    print(tF, tc)