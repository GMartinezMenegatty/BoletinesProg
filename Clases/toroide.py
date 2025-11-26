import math
from circulo import Circulo
from punto import Punto
'''
class Toroide:
    def __init__(self, radio1, radio2):
        self.radio1 = radio1
        self.radio2 = radio2

    def calcularVolumen(self):
        return 2 * pow(math.pi,2) * self.radio1 * pow(self.radio2,2)

    def calcularArea(self):
        return 4 * pow(math.pi,2) * self.radio1 * self.radio2
'''
class Toroide(Circulo):
    def __init__(self, x, y, r,  centro):
        super().__init__(x, y, r)
        self.centroToroX = centro.x
        self.centroToroY = centro.y

    def calculoRadioMaior(self):
        return self.distancia(Punto(self.centroToroX, self.centroToroY))

    def calcularArea(self):
        # R = distancia centro circunferencia e centro toroide
        # r = R - radio circunferencia
        radioMaior = self.calculoRadioMaior()
        radioMenor = radioMaior - self.radio
        return 4 * math.pi ** 2 * radioMaior * radioMenor

    def volumen(self):
        return 2 * math.pi * self.calculoRadioMaior() * super().calcularArea()

