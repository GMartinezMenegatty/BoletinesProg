# funciones que devuelven algo y otras que no, las funciones se deben definir, para que
# se ejecute debo colocar los parentesis a continuacion, sino no se ejecuta

def crearmenu():
        print("De que figura quiere calcular su area: ")
        print("1. Triangulo")
        print("2. Rectangulo")
        print("3. Circulo")
        print("4. Salir")
        print("Elige opcion: ")


def calcularareatriangulo(base, altura):    #si tiene parametro se mete dentro de los parentesis
        area = base * altura / 2
        return area # puedo devolver varias cosas separadas por una coma

crearmenu()
areaTriangulo = calcularareatriangulo(4, 3)
print(areaTriangulo)

#print (calcularareacirculo())
#print (calculararearectangulo())
#print (calculararearectangulo(2))
#print (calculararearectangulo(42, 2))
#print (calculararearectangulo(altura = 3, base = 2))

def suma (n1, n2, *otrosnumeros):
    suma = n1 + n2
    for n in otrosnumeros:
        suma = suma + n
    return suma


print (suma (1, 3))

def datosPersona (dni, nome, **datosExtendidos):
    print("el dni es: ", dni)
    print("el nome es: ", nome)
    for k, v in datosExtendidos.items():  #clave, valor
        print(k, "es:", v)

datosPersona("3333333", "lala", altura = 1.82, peso = 70)