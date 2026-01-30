#1. Escribir o resultado das seguintes expresións:
#a) ((3 + 2) % 2 – 15) / 2 * 5=
#b) (6 + (6) / 7) + 35 / 2 -8 * 5 / 4 * 2 =
#c) 3 + 6 * 14 % 3 =
#d) 8 + 7 * 3 + 4 * 6 /2 % 4 =
#e) 27 % 4 +15 / 4 =
#f) 37 / 42  - 2 =
#g) 9 * 2 / 3 * 25 * 3 =
#h) (7 * 3 – 4 * 4) * 2 / 4 * 2 =

print ('1')

a = ((3 + 2) % 2 - 15) / 2 * 5
print ('a.', a )

b = (6 + (6) / 7) + 35 / 2 -8 * 5 / 4 * 2
print ('b.', b )

c = 3 + 6 * 14 % 3
print ('c.', c )

d = 8 + 7 * 3 + 4 * 6 /2 % 4
print ('d.', d )

e = 27 % 4 +15 / 4
print ('e.', e )

f = 37 / 42  - 2
print ('f.', f )

g = 9 * 2 / 3 * 25 * 3
print ('g.', g )

h = (7 * 3 - 4 * 4) * 2 / 4 * 2
print ('h.', h )

#2. Cales dos seguintes nomes de variables non son válidos?
#a) Salto- mortal , salto_mortal, salto + mortal, 2salto, “salto”
#b) cantidade total, cant_total, cant5, cantidadeTotal

print ('--')
print (2)

print ("Salto- mortal")
a2 = "Salto- mortal" == False
print ('a.', a2)

print ("salto_mortal")
b2 = "salto_mortal" != True
print ('b.', b2)

print ("salto + mortal")
c2 = "salto + mortal" == False
print ('c.', c2)

print ("2salto")
d2 = "2salto" == False
print ('d.', d2)

print ('"salto"')
e2 = '"salto"' == False
print ('e.', e2)

print ("cantidade total")
f2 = "cantidade total" == False
print ('f.', f2)

print ("cant_total")
g2 = "cant_total" != True
print ('g.', g2)

print ("cant5")
h2 = "cant5" != True
print ('h.', h2)

print ("cantidadeTotal")
i2 = "cantidadeTotal" != True
print ('i.', i2)

#3. Expresar, utilizando operadores aritméticos, as seguintes expresións

print ('--')
print (3)

a3 = "(m + n) / n"
print ('a3.', a3 )

b3 = "((m + n) / p) / ((p - r) / s)"
print ('b3.', b3 )

c3 = "(m + 4) / (p - q)"
print ('c3.', c3 )

d3 = "(c * r * t) / 100"
print ('d3.', d3 )

e3 = "(m + n) / (p + (q / r))"
print ('e3.', e3 )

f3 = "(m / n) * (p + q)"
print ('f3.', f3 )

g3 = "n * ((1 + i)^t) * i / ((1 + i)^t) - 1"
print ('g3.', g3 )

#4 Avalia as seguintes expresións
# a) true and true == false
# b) not false == true
# c) (true and true) or false == true
# d) (false or false) and false != true
# e) (not(true and false)) == false
# f) “12” + “12” == “24”
# g) “34” + “43” == “3443”

print ('--')
print (4)

a4 = True and True
print ('a4.', a4 )

b4 = not False
print ('b4.', b4 )

c4 = (True and True) or False
print ('c4.', c4 )

d4 = (False or False) and False
print ('d4.', d4 )

e4 = (not(True and False))
print ('e4.', e4 )

f4 = "12" + "12"
print ('f4.', f4 )

g4 = "34" + "43"
print ('g4.', g4 )

# 5. Avaliar as seguintes espresións, tendo en conta que as variables  teñen os valores:
# a) i = 1, j = 0, k = 1 				i + k <= j – k * 3 and k >= 2
# b) i = 3, j = 2, k = -1				i == 3 or j <= 2 and k > 0
# c) tipo = 10, rede = 7,5 			tipo < rede + 1,5
# d) ano = 1993				ano % 400 == 0
# e) 3 == 2 or 5 > 1 + 1
# f ) 5 – 2 > 4 and not(0,5 == 1 / 5)
# g) a = 2, b = 5, c = 6, d = 10		a >= b or a >= c and a <d
# h) a = 2, b = 5, c = 6, d = 10		a + b < c and a + c < d or 2 * a < a + b
# i)  a = 2, b = 5, c = 6, d = 10		!(a * b < d) and !(a * b < c) or b + c <= d

print ('--')
print (5)

i, j, k = 1, 0, 1
a5 = i + k <= j - k * 3 and k >= 2
print('a.', a5)

i, j, k = 3, 2, -1
b5 = i == 3 or j <= 2 and k > 0
print('b.', b5)

tipo, rede = 10, 7.5
c5 = tipo < rede + 1.5
print('c.', c5)

ano = 1993
d5 = ano % 400 == 0
print('d.', d5)

e5 = 3 == 2 or 5 > 1 + 1
print('e.', e5)

f5 = 5 - 2 > 4 and not (0.5 == 1 / 5)
print('f.', f5)

a, b, c, d = 2, 5, 6, 10
g5 = a >= b or a >= c and a < d
print('g.', g5)

a, b, c, d = 2, 5, 6, 10
h5 = a + b < c and a + c < d or 2 * a < a + b
print('h.', h5)

a, b, c, d = 2, 5, 6, 10
i5 = (not (a * b < d)) and (not (a * b < c)) or b + c <= d
print('i.', i5)
