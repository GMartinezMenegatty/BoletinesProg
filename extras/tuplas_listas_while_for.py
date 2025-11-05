#las tuplas no se pueden cambiar
#l = [10, 20, [30, "treinta reg", "XXX"], 40, 50]
#t = (10,20,30,40,50,60,70,80,90,100)
#print(l[2])
#print(l[2][1])
#print(l[-3])
#print(t[0])
#print(t[1:4])
#print(t[1:4:2])
#print(t[:10:3])
#print(t[2::3])
#print(t[1:8:])
#print(t[::])
#print(t[::-1])
# count
t = (10,20,30,40,50,60,70,80)

i = 0
suma = 0
while i<len(t):    #i <= 7:
    suma = suma + t[i]
    i += 1    # i = i + 1    a i se le suma 1 y a i se le deja ese resultado

print (suma)

suma = 0

for numero in t:
    print (numero)
    suma = suma + numero

#print (suma)

for i in range(0, 8):  #  (7,0,-1)   permite hacer un incremento negativo o positivo, genera un numero
    print (i)
    print (t[i])

for i, numero in enumerate(t):
    print (i)
    print (numero)
    print (t[i])

#ejemplo bucle for

t = (100,200,300,400,500,600,700,800,900)
iteracion = 1

print ("antes de entrar al bucle")

for numero in t:
    print ("iteracion", iteracion)
    print ("elemento de tupla", numero)
    print ("incremento i")
    iteracion = iteracion + 1

#diccionario
#se meten entre llaves y cada conjunto de valores se separa por comas
#primero se coloca la clave y luego su valor
colores = {"verde":"green",
           "morado":"purple",
           "brown":"cafe"
           }
print (colores["verde"])  #si coloco una clave me da el valor

print (colores.keys())   #accedo a las claves
print (colores.values())  #accedo a los valores
print (colores.items())   #accedo a la lista completa

for color in colores.values():
    print (color)

for clave in colores.keys():
    print (clave)

print (colores.get("verde"))
print(colores["verde"])
print ( colores.keys())

for clave,valor in colores.items():
    print ("la clave es: ", clave, "\nel valor es: ", valor)


