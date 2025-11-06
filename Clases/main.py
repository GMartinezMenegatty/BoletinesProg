from punto import Punto


p1 = Punto(2,3)
p2 = Punto(9,1)
p2.x = 2
p2.y = 3


print (p1==p2)

p1 = p2
p3 = p2

p1.x = 99999

print(p1.toString())
print(p2)

print(p1.x)
