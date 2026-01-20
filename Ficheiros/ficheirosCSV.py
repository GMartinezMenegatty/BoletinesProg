import csv

with open('exemplo.csv', 'w') as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow (['Nome', 'Edade', 'Xenero'])
    writer.writerow(['Pedro', '23', 'Home'])
    writer.writerow(['Rosa', '25', 'Muller'])

with open ('exemplo2.csv', 'w') as ficheiro:
    ficheiro.write ("Nome" + ',' + 'Edade' + ',' + 'Xenero' + '\n')
    ficheiro.write ("Pedro" + ',' + '23' + ',' + 'Home' + '\n')
    ficheiro.write ("Rosa" + ',' + '25' + ',' + 'Muller')

with open ('exemplo.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for fila in reader:
        print(fila)