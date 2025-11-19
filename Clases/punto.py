class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def aCadea(self):
        cadeaPunto = "As coordenadas son: \n\t x = "+ str(self.x) + " \n\t y = "+ str(self.y) #\n\t es para saltar de linea
        return cadeaPunto

    def __str__(self):
        return self.aCadea()

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y   #comparacion