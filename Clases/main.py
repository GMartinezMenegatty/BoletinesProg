from punto import Punto
from circulo import Circulo
from cilindro import Cilindro

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

cl1 = Cilindro(2,3,1,3)
print(cl1.aCadea())