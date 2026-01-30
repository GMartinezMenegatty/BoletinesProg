valor = int(input('¿cual es el valor?: '))

bil100 = valor // 100
valor = valor % 100

bil20 = valor // 20
valor = valor % 20

bil5 = valor // 5
valor = valor % 5

mon= valor // 1
valor = valor % 1

print('el valor en billetes de 100: ', bil100)
print('el valor es 20: ', bil20)
print('el valor es 5: ', bil5)
print('el valor es 1: ', mon)