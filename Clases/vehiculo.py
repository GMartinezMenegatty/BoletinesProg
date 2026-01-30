from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia):
        self._matricula = matricula
        self._velocidadeMaxima = velocidadeMaxima
        self._autonomia = autonomia


    @property
    def matricula(self):
        return self.matricula

    @matricula.setter
    def matricula(self, matricula):
        self.matricula = matricula

    @property
    def velocidadeMaxima(self):
        return self.velocidademaxima

    @velocidadeMaxima.setter
    def matricula(self, matricula):
        self.velocidademaxima = matricula

    @property
    def autonomia(self):
        return self.autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self.autonomia = autonomia

    @abstractmethod
    def arrincar(self):
        pass

    def deter(self):
        print(f"El vehiculo {self.matricula} esta parado")

    @abstractmethod
    def mostrar_datos(self):
        pass

class Terrestre(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self._numeroRodas = numeroRodas

    @property
    def numeroRodas(self):
        return self._numeroRodas

    @numeroRodas.setter
    def numeroRodas(self, numeroRodas):
        self.numeroRodas = numeroRodas



class Aereo(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, altitudeMaxima):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self.altitudeMaxima = altitudeMaxima

    @property
    def altitudeMaxima(self):
        return self.altitudeMaxima

    @altitudeMaxima.setter
    def altitudeMaxima(self, altitudeMaxima):
        self.altitudeMaxima = altitudeMaxima

class Coche_Autonomo(Terrestre):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas, numeroPlazas):
        super().__init__(matricula,velocidadeMaxima,autonomia,numeroRodas)
        self.numeroPlazas = numeroPlazas

    @property
    def numeroPlazas(self):
        return self._numeroPlazas

    @numeroPlazas.setter
    def numeroPlazas(self, numeroPlazas):
        self._numeroPlazas = numeroPlazas

    def arrincar(self):
        print("Coche Autonomo arranca")

    def mostrar_datos(self):
        print(f"Coche autonomo {self._matricula} {self._autonomia} {self.numeroRodas} {self.numeroPlazas}")

if __name__ == '__main__':
    coche1 = Coche_Autonomo("0000BBB",100,250,4,4)
    print(coche1.mostrar_datos())