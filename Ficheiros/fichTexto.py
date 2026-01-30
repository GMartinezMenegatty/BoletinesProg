ficheiro = open('/home/dam/PROG/boletines/ejercicios-programacion-castelao/ejercicios clase/ficheiros/saudo.txt', 'r')
print(ficheiro.read())
ficheiro.close()

ficheiro = open('/home/dam/PROG/boletines/ejercicios-programacion-castelao/ejercicios clase/ficheiros/saudo.txt', 'a')
ficheiro.write("Ola mundo\n")
ficheiro.close()

'''Descomentar para borrar contenido del ficheiro
with open('/home/dam/PROG/boletines/ejercicios-programacion-castelao/ejercicios clase/ficheiros/saudo.txt', 'r') as ficheiro:
    primeira_linha = ficheiro.readline()
with open('/home/dam/PROG/boletines/ejercicios-programacion-castelao/ejercicios clase/ficheiros/saudo.txt', 'w') as ficheiro:
    ficheiro.write(primeira_linha)
'''

ficheiro = open('/home/dam/PROG/boletines/ejercicios-programacion-castelao/ejercicios clase/ficheiros/saudo.txt', 'r')
print(ficheiro.read())
ficheiro.close()