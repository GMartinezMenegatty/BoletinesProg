from circulo import Circulo
import math

class Cilindro(Circulo):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y, radio)
        self.altura = abs(altura)

    def calcularArea(self):
       #return 2 * math.pi * self.radio * (self.altura * math.pi)
       return super().calcularArea() * 2 + super().calcularPerimetro() * self.altura

    c1 = Cilindro (0, 0 , 2, 3)
