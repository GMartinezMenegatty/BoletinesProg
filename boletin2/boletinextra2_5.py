saldoFijo = int(input('cuanto es el saldo: '))
km = int(input('cuantos kilometros: '))
diadesp = int(input('cuantos dias: '))
ventas = int(input('cuantas ventas: '))

km = km * 2
diadesp = diadesp * 30
ventas = ventas * 0.05
saldobruto = saldoFijo + diadesp + ventas + km
print('el valor del saldo bruto es: ', saldobruto)

irpf = saldobruto * 0.18
ret = 36

saldoliquido = saldobruto - irpf - ret
print('el valor del saldo liquido es: ', saldoliquido)