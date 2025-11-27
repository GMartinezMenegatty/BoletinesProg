'''
setHora(horas)
getHoras()
setMinutos(minutos)
getMinutos()
setSegundos(segundos)
getSegundos()

converterSegundos()
converterMinutos()
incrementarMinutos(minutos)
incrementarSegundos(segundos)
incrementarHoras(horas)
mostrarFormato12Horas()

---
class Hora:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def setHora(self, horas):
            self.horas = horas

    def setMinuto(self, minutos):
        if self.minutos >= 0 and self.minutos <= 59:
            if self.minutos.isdigit():
                self.minutos = minutos

    def setSegundo(self, segundos):
        if self.segundos >= 0 and self.segundos <= 59:
            if self.segundos.isdigit():
                self.segundos = segundos

    def getHoras(self):
        return self.horas

    def getMinutos(self):
        return self.minutos

    def getSegundos(self):
        return self.segundos

    def aCadea(self):
        return "La hora es: " + str(self.horas) + " minutos: " + str(self.minutos) + " segundos: " + str(self.segundos)
---
    def getHora(self):
        return self.__horas

    def setMinutos(self, minutos):

    def getMinutos(self):
        return self.__minutos

    def setSegundos(self, segundos):

    def getSegundos(self):
        return self.__segundos
'''

class Hora:
    def __init__(self, hora, minuto, segundo):
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def setHora(self, hora):
        if type(hora) == int:
            if hora < 24 and hora >= 0:
                self.__hora = hora
            else:
                self.__hora = 0
        else:
            self.__hora = 0

    def setMinuto(self, minuto):
        if isinstance (minuto,int):
            if minuto < 60 and minuto >= 0:
                self.__minuto = minuto
            else:
                self.__minuto = 0
        else:
            self.__minuto = 0

    def setSegundo(self, segundo):
        if isinstance (segundo,int):
            if segundo < 60 and segundo >= 0:
                self.__segundo = segundo
            else:
                self.__segundo = 0
        else:
            self.__segundo = 0

    def incrementarSegundos(self, segundos):
        s = segundos % 60
        self.__segundo = self.__segundo + s
        if self.__segundo >= 60:
            self.__segundo = self.__segundo % 60
            self.__minuto += 1
            if self.__minuto >= 60:
                self.__minuto = self.__minuto % 60
                self.__hora += 1
                if self.__hora >= 24:
                    self.__hora = self.__hora % 24
        minutos = segundos / 60
        self.__minuto = self.__minuto + minutos
        if self.__minuto >= 60:
            self.__minuto = self.__minuto % 60
            self.__hora += 1
            if self.__hora >= 24:
                self.__hora = self.__hora % 24
        horas = minutos / 60
        self.__hora = (self.__hora + horas) % 24




    def __str__ (self):
        return str(self.__hora) + ":" + str(self.__minuto) + ":" + str(self.__segundo)

h1 = Hora(-3434, "string", 23)

