from punto import Punto
from punto2 import Punto2
from circulo import Circulo
from cilindro import Cilindro
from esfera import Esfera
from toroide import Toroide
from hora import Hora
from data import Data
from bombilla import Bombilla
from cliente import Cliente
from persoa import Persoa, Persoa2

try:
    p3 = Punto2(5, 6)
except TypeError as e:
    print("Error:" + str(e))
else:
    p3.setX(7)
    p3.x = 5
    print(p3)
    print(p3.x)
    print(p3.getY())



p1 = Punto(2,3)
p2 = Punto(9,1)
p2.x = 2
p2.y = 3


print (p1==p2)

p1 = p2
p3 = p2

p1.x = 99999

print(p1.aCadea())
print(p2)

print(p1.x)

c1 = Circulo(2,3,1)

print(c1.aCadea())

cil = Cilindro (3,2,3, 5)
print(cil.calcularArea())

'''hoxe = Data (21, 11, 2025)

print (hoxe)'''

esf = Esfera (2, 3, 5)
print(esf.calcularVolumen())

#tor = Toroide (3, 2,5,3)
#print(tor.calcularArea())
#print(tor.calcularVolumen())


'''
hora=Hora(21, 11, 25)
print (hora.aCadea())
'''

bombilla1 = Bombilla("ON")
print(bombilla1.getEstado())

bombilla1.setEstado("OFF")
print(bombilla1.getEstado())

bombilla1.setEstado("OFF")
print(bombilla1.getEstado())



manuel = Persoa("Manuel",53,"00000400T","Garcia Barbon","Española")
print(manuel)

juan = Persoa("Juan", 34, "00000400T", "Florida", "Española")
print (manuel == juan)
print (manuel < juan)
print (manuel > juan)

pepe = Persoa2('Pepe', "12345678T", 23)
