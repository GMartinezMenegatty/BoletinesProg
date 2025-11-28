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

    def incrementarSegundos2(self, segundos):
        horas = segundos // 3600
        segundos = segundos - 3600 * horas
        self.__hora = (self.__hora + horas) % 24
        minutos = segundos // 60
        segundos = segundos - minutos * 60
        self.__minuto = self.__minuto + minutos
        if self.__minuto >= 60:
            self.__minuto = self.__minuto % 60
            self.__hora = (self.__hora + 1) % 24
        self.__segundo = self.__segundo + segundos
        if self.__segundo >= 60:
            self.__segundo = self.__segundo % 60
            self.__minuto += 1
            if self.__minuto >= 60:
                self.__minuto = self.__minuto % 60
                self.__hora += 1
                if self.__hora >= 23:
                    self.__hora = self.__hora % 24

    def incrementarMinutos(self, minutos):
        horas = minutos // 60
        minutos = minutos - 60 * horas
        self.incrementarHoras(horas)
        self.__minuto = self.__minuto + minutos
        if self.__minuto >= 60:
            self.__minuto = self.__minuto % 60
            self.incrementarHoras (1)

    def incrementarHoras(self, horas):
        self.__hora = self.__hora + horas

    def __str__ (self):
        return str(self.__hora) + ":" + str(self.__minuto) + ":" + str(self.__segundo)


'''
    def incrementarSegundos3(self, segundos):
        minutos = segundos // 60
        self.incrementarMinutos(minutos)
        segundos = segundos - minutos * 60
        if self.__segundo >= 60:
            self.__segundo = self.__segundo % 60
            self.__minuto += 1
            if self.__minuto >= 60:
                self.__minuto = self.__minuto % 60
                self.__hora += 1
                if self.__hora >= 23:
                    self.__hora = self.__hora % 24
'''

'''
    def incrementarSegundos(self, segundos):
        s = segundos % 60
        segundos = segundos - s
        self.__segundo = self.__segundo + s
        if self.__segundo >= 60:
            self.__segundo = self.__segundo % 60
            self.__minuto += 1
            if self.__minuto >= 60:
                self.__minuto = self.__minuto % 60
                self.__hora += 1
                if self.__hora >= 24:
                    self.__hora = self.__hora % 24
        minutos = segundos // 60
        segundos = segundos - minutos % 60
        self.__minuto = self.__minuto + minutos
        if self.__minuto >= 60:
            self.__minuto = self.__minuto % 60
            self.__hora += 1
            if self.__hora >= 24:
                self.__hora = self.__hora % 24
        horas = segundos // 3600
        self.__hora = self.__hora + horas
        if self.__hora > 23:
            self.__hora = self.__hora % 24
'''

h1 = Hora(23, 59, 59)
#h1.incrementarMinutos(7200)
h2 = Hora(23, 59, 59)
h2.incrementarSegundos2(1)
print(h1,h2)

