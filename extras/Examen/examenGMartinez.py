from datetime import datetime

class Persoa:
    def __init__(self, nome, dni, cp):
        self.setNome (nome)
        self.setDni (dni)
        self.setCp (cp)

    def setNome (self, nome):
        if isinstance (nome, str):
            nomeSenEspazos = nome.replace(' ', '')
            if nomeSenEspazos.isalpha():
                self.__nome = nome
            else:
                self.__nome = "XXXX"

    def getNome (self):
        return self.__nome

    def setDni (self, dni):
        if isinstance(dni, str):
            self.__dni = dni
        else:
            self.__dni = "XXXX"

    def getDni (self):
        return self.__dni

    def setCp (self, cp):
        self.__cp = "00000"
        if type (cp) == str:
            if len(cp) == 5:
                if cp.isnumeric ():
                    self.__cp = cp

    def getCp (self):
        return self.__cp

    def __eq__(self, outro):
        return self.__dni == outro.dni

    def __str__(self):
        return "El nombre es: "+ self.__nome + "El dni es: " + self.__dni + "El Codigo Postal es: " + self.__cp

    nome = property (setNome, getNome)
    dni = property (setDni, getDni)
    cp = property (setCp, getCp)


class Cliente (Persoa):
    def __init__(self, nome, dni, cp, telf):
        super().__init__(nome, dni, cp)
        self.setTelf (telf)

    def setTelf(self, telf):
        self.__telf = "+00 000 000 000"
        if isinstance (telf, str):
            if len (telf) == 15:
                if telf[0] == '+' and telf[3] == ' ' and telf[7] == ' ' and telf[11] == ' ':
                    telefonoSenEspazos = telf[1:].replace(' ', '')
                    if telefonoSenEspazos.isnumeric():
                        self.__telf = telf

    def getTelf(self):
        return self.__telf

    def __str__ (self):
        return super().__str__() + "El Telefono es: " + self.__telf

    telf = property (setTelf, getTelf)

class Llamada:
    def __init__(self, cliente, telfInter, dhIni, dhFin, sainte):
        self._setCliente (cliente)
        self.setTelefono (telfInter)
        self.setDhInicio (dhIni)
        self.__DhFin = dhFin if isinstance (dhFin, datetime) else None
        self.__sainte = sainte if isinstance (sainte, bool) else None

    def _setCliente(self, cliente):
        self.__cliente = cliente if isinstance (cliente, Cliente) else None

    def getCliente(self):
        return self.__cliente

    def _setTelefono(self, telf):
        self.__telf = "+00 000 000 000"
        if isinstance (telf, str):
            if len (telf) == 15:
                if telf[0] == '+' and telf[3] == ' ' and telf[7] == ' ' and telf[11] == ' ':
                    telefonoSenEspazos = telf[1:].replace(' ', '')
                    if telefonoSenEspazos.isnumeric():
                        self.__telf = telf

    def getTelfInter(self):
        return self.__telfInter

    def setDhInicio(self, dhIni):
        self.__DhInicio = dhIni if isinstance(dhIni, datetime) else None

    def getDhInicio(self):
        return self.__DhInicio

    def minutosLlamada(self):
        duracion = self.__dhFin - self.__dhIni
        return duracion.total_seconds()/60

    def __str__(self):
        return "El cliente es: " + super().__str__() + "El telefono del interlocutor es: " + self.__telfInter + "La data de la llamada es: " + self.data

    telfinter = property (_setTelefono, getTelfInter)


class ControlLlamadas (Llamada):
    def __init__(self, llamada):
        super().minutosLlamada(self)
        self.llamada = llamada

    def setLlamada(self, llamada):
        self.llamada = llamada

    def getLlamada(self):
        return self.llamada

    def engadirLlamada(self, llamada, data):
        if llamada is not None:
            self.engadirLlamada.append((llamada, data))

    llamada = property (setLlamada, getLlamada)
