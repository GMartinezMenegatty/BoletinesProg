from circulo import Circulo
import math

class Cilindro(Circulo):
    def __init__(self, x, y, radio, altura):
        super.__init__(x, y, radio)
        self.altura = altura

    def calcularArea(self):
        return 2 * math.pi * self.radio * (self.altura * math.pi)

    def aCadea(self):
        super().aCadea() + "Area: " + str(self.calcularArea())