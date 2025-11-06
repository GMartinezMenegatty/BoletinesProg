

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n\t x = "+ str(self.x) + " \n\t y = "+ str(self.y) #\n\t es para saltar de linea
        return cadeaPunto

    def __str__(self):
        return self.toString()

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y   #comparacion