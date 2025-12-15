from datetime import datetime

class Persoa:
    def __init__(self, nome, dni, cp):
        self.__nome = nome
        self.__dni = dni
        self.__cp = cp

    def setNome (self, nome):
        self.__nome = nome

    def getNome (self):
        return self.__nome

    def setDni (self, dni):
        self.__dni = dni

    def getDni (self):
        return self.__dni

    def setCp (self, cp):
        if cp == 5:
            return True
        else:
            return False

    def getCp (self):
        return self.__cp

    def __eq__(self, outro):
        return self.__dni == outro.dni

    def __str__(self):
        return "El nombre es: "+ self.__nome + "El dni es: " + self.__dni + "El Codigo Postal es: " + self.__cp

    nome = property (setNome, getNome)
    dni = property (setDni, getDni)
    cp = property (setCp, getCp)


class Cliente:
    def __init__(self, nome, dni, cp, telf):
        self.__nome = nome
        self.__dni = dni
        self.__cp = cp
        self.__telf = telf


    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setDni(self, dni):
        self.__dni = dni

    def getDni(self):
        return self.__dni

    def setCp(self, cp):
        self.__cp = cp

    def getCp(self):
        return self.__cp

    def setTelf(self, telf):
        for n in telf:
            if n[0] == "+":
                if n[3] == " " and n[7] == " " and n[11] == " ":
                    if len(telf) == 15:
                        if isinstance (telf, int):
                            if n >= 0 and n <= 9:
                                return self.__telf
            else:
                return "+00 000 000 000"

    def getTelf(self):
        return self.__telf

    def __str__ (self):
        return "El nombre es: "+ self.__nome + "El dni es: " + self.__dni + "El Codigo Postal es: " + self.__cp + "El Telefono es: " + self.__telf

    nome = property (setNome, getNome)
    dni = property (setDni, getDni)
    cp = property (setCp, getCp)
    telf = property (setTelf, getTelf)


class Llamada(Cliente):
    def __init__(self, cliente, telfInter, data):
        super().__init__(cliente)
        self.__telfInter = telfInter
        self.data = data

    def setCliente(self):
        return super().setNome, super().setTelf, super().setCp, super().setDni

    def getCliente(self):
        return self.setCliente

    def setTelfInter (self, telfInter):
        self.__telfInter = telfInter

    def getTelfInter(self):
        return self.__telfInter

    def setData (self, data):
        datetime = 0
        if data > 0:
            return True

    def getData(self):
        return self.data

    def minutosLlamada(self, data):
        minutosLlamada = 0
        if data > 0 :
            minutosLlamada += 1

    def __str__(self):
        return "El cliente es: " + super().__str__() + "El telefono del interlocutor es: " + self.__telfInter + "La data de la llamada es: " + self.data

    cliente = property (setCliente, getCliente)
    telfinter = property (setTelfInter, getTelfInter)
    data = property (setData, getData)


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
