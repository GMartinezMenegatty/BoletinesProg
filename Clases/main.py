import toroide
from punto import Punto
from circulo import Circulo
from cilindro import Cilindro
from esfera import Esfera
from toroide import Toroide
from data import Data

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

tor = Toroide (3, 2)
print(tor.calcularArea())
print(tor.calcularVolumen())