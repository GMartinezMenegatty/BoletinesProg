bil1 = int(input('¿cuantos billetes de 100?: '))
bil2 = int(input('¿cuantos billetes de 20?: '))
bil3 = int(input('¿cuantos billetes de 5?: '))
mon = int(input('¿cuantos monedas de 1?: '))

bil1 = bil1 * 100
bil2 = bil2 * 20
bil3 = bil3 * 5

suma = bil1 + bil2 + bil3 + mon
print(suma)