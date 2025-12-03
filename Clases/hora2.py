

class Hora:
    def __init__(self, hora = 0, *minutoSegundo):
        #Comprobacion si o formato e int, int, int
        if isinstance(hora, int):
            self.__asignacionHoraInt(hora, minutoSegundo)

        if type (hora) == str:
            self.__asignacionHoraStr (hora)

        if isinstance(hora, list) or isinstance (hora, tuple):
            self.__asignacionHoraColeccion(hora)

        if isinstance (hora, float):
            self.__asignacionHoraFloat (hora)

        if type (hora) == Hora:
            self.asignacionHoraHora (hora)


    def __asignacionHoraInt (self, hora, minutoSegundo):
        self.setHora(hora)
        if minutoSegundo is not None:
            if len(minutoSegundo) == 1:
                if isinstance(minutoSegundo[0], int):
                    self.setMinuto = (minutoSegundo[0])
            elif len(minutoSegundo) == 2:
                if isinstance(minutoSegundo[0], int):
                    self.setMinuto = (minutoSegundo[0])
                if isinstance(minutoSegundo[1], int):
                    self.setSegundo = (minutoSegundo[1])

    def __asignacionHoraStr (self, hora):
        if len(hora) == 8:
            if hora[2] == ':' and hora [5] == ':':
                hms = hora.split(':')
                if hms[0].isnumeric():
                    h = int(hms[0])
                    if h >= 0 and h <= 24:
                        self.setHora(h)
                if hms[1].isnumeric():
                    m = int(hms[1])
                    if m >= 0 and m <= 59:
                        self.setMinuto = (m)
                if hms[2].isnumeric():
                    s = int(hms[2])
                    if s >= 0 and s <= 59:
                        self.setSegundo = (s)
        else:
            self.setHora (0)
            self.minuto (0)
            self.segundo (0)


    def __asignacionHoraColeccion(self, hora, minutoSegundo):


    def __asignacionHoraFloat(self, hora, minutoSegundo):


    def __asignacionHoraHora(self, hora, minutoSegundo):






    def setHora(self, hora):
        if hora < 24 and hora >= 0:
             self.__hora = hora
         else:
              self.__hora = 0

    def getHora(self):
        return self.__hora

    def setMinuto(self, minuto):
        if isinstance (minuto,int):
            if minuto < 60 and minuto >= 0:
                self.__minuto = minuto
            else:
                self.__minuto = 0
        else:
            self.__minuto = 0

    def getMinuto(self):
        return self.__minuto

    def setSegundo(self, segundo):
        if isinstance (segundo,int):
            if segundo < 60 and segundo >= 0:
                self.__segundo = segundo
            else:
                self.__segundo = 0
        else:
            self.__segundo = 0

    def getSegundo(self):
        return self.__segundo

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

    hora = property (getHora, setHora)
    minuto = property (getMinuto, setMinuto)
    segundo = property (getSegundo, setSegundo)

h1 = Hora(23, 59, 59)
# h1.incrementarMinutos(7200)
h2 = Hora(23, 59, 59)
h2.incrementarSegundos2(1)
print(h1, h2)