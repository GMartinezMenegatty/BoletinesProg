# Condicional multiple match case

x = 40

if x == 10:
    print ("X e 10")
elif x == 20:
    print("X e 20")
elif x == 30:
    print("X e 30")

match x:
    case 10:
        print ("X e 10")
    case 20:
        print ("X e 20")
    case 30:
        print ("X e 30")
    case _:
        print("X non e 10, 20 ou 30")

match x:
    case 10|20|30:
        print (f"X e {x}")
    case _:
        print("X non e 10, 20 ou 30")

y = 20
match x:
    case 10 if y % 2 == 0:
        print("X e 10 e Y divisible entre 2")
    case 10:
        print("X e 10 e Y non divisible entre 2")
    case _:
        print ("Opcion desconocida")


l = [2, 3, 5]

match l:
    case (x, y):
        print (f"Coleccion con dous elementos {x}, {y}")
    case (x, y, z):
        print (f"Coleccion con los elementos {x}, {y}, {z}")
    case _:
        print ("Formato desconocido")

persoa = {"nome" : "Manuel", "curso" : "Dam", "edade" : 19}

match persoa:
    case {"nome": nome, "curso": curso}:
        print (f"Nome: {nome}, curso: {curso}")
    case {"nome": nome}:
        print (f"Nome: {nome}")
    case _:
        print("Formato desconocido")

class Figura:
    pass

class Circulo (Figura):
    def __init__ (self, r):
        self.radio = r

class Rectangle (Figura):
    def __init__ (self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

f = Circulo (15)
f = Rectangle (10, 12)

match f:
    case Circulo(r):
        print (f"Circulo con radio = {r}")
    case Rectangle(ancho, alto):
        print(f"Rectangulo con ancho = {ancho}, alto = {alto}")
    case _:
        print ("Formato desconocido")



