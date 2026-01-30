class Consumo:
    def __init__(self, km=0, litros=0, vMed=0, pGas=0):
        self.km = km
        self.litros = litros
        self.vMed = vMed
        self.pGas = pGas

    def getTempo(self):
        return self.km / self.vMed if self.vMed > 0 else 0

    def consumoMedio(self):
        return (self.litros * 100) / self.km if self.km > 0 else 0

    def consumoEuros(self):
        return self.consumoMedio() * self.pGas

    def setKms(self, km):
        self.km = km

    def setLitros(self, litros):
        self.litros = litros

    def setvMed(self, v):
        self.vMed = v

    def setPGas(self, p):
        self.pGas = p


