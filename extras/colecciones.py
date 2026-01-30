s = { 10, 15.5, "Vinte"}
s = set([20,30,40])
print(type(s))
print(s)
#print(s[1]) no funciona

s.add(40)
s.add(50)
s.update([80,90,70])
s.remove(70)

print(s)


fs = frozenset([3,4,5,6])
print(fs)
#fs.add(7) no se puede

print(fs.union(s))
print(s.intersection(fs))

elementoAleatorio = s.pop()
print(elementoAleatorio)


#comrpobaacion mas rapido q listas
n = {1,2,3,4,5}
print(3 in n)

#Achega de elementos unicos
l2 = [1,2,3,4,5]
l3 = [2,3,4]
print(set(l2)-set(l3))