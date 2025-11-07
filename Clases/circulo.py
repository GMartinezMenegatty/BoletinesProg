from punto import Punto
import math

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = abs(radio)

    def obterDiametro(self):
        return self.radio * 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

    def calcularArea(self):
        return math.pi * pow(self.radio, 2)
       #return math.pi * self.radio * self.radio
       #return math.pi * (self.radio ** 2)

    def aCadea(self):
        cadea = super().aCadea() + "\n\t Radio: " + str(self.radio) + "\n\t Diametro:"+ str(self.obterDiametro()) +"\n\t Area: " + str(self.calcularArea())
        return cadea

