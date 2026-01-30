
import math

def crearmenu():
    print("De que figura quiere calcular su area: ")
    print("1. Rectangulo")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Salir")

def calculararearectangulo(base, altura):
    return base * altura

def calcularareatriangulo(base, altura):
    area = calculararearectangulo(base, altura)/2
    return area

def calcularareacirculo(radio):
    # radio * radio * 3.1416
    return math.pow(radio,2) * math.pi

def recogerParametros(opcion):
    if opcion == 1 or opcion == 2:
        base = float(input("Ingrese el valor de la base: "))
        altura = float(input("Ingrese el valor de la altura: "))
        return base, altura
    elif opcion == 3:
        radio = float(input("Ingrese el valor del radio: "))
        return radio

def ejercicioBoletin_4_2():
    opcion = 0
    while opcion != 4:
        crearmenu()
        opcion = int(input("Elige una opcion: "))
        if opcion > 0 and opcion < 5:
            if opcion == 1 or opcion == 2:
                base, altura = recogerParametros(opcion)
                if opcion == 1:
                    area = calculararearectangulo(base, altura)
                    print("El area del rectangulo es: ", area)
                if opcion == 2:
                    area = calcularareatriangulo(base, altura)
                    print("El area del triangulo es: ", area)
            elif opcion == 3:
                radio = recogerParametros(opcion)
                area = calcularareacirculo(radio)
                print("El area del circulo es: ", area)
        else:
            print("Opcion no valida")

ejercicioBoletin_4_2()



