from circulo import Circulo
import math

class Esfera (Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x, y, radio)

    def calcularArea(self):
        return 4 * super().calcularArea()

    def calcularVolumen(self):
        # volume = (4/3) * math.pi * pow (self.radio, 3)
        # volume = (self.calcularArea() * self.radio) / 3.
        volume = (4/3) * super().calcularArea() * self.radio
        return volume





