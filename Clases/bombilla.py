class Bombilla:
    def __init__(self, estado):
        self.__estado = estado

    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado





    def acende(self):
        if self.__estado == "ON":
            self.__estado = "ON"
        if self.__estado == "OFF":
            self.__estado = "ON"

    def apaga(self):
        if self.__estado == "OFF":
            self.__estado = "OFF"
        if self.__estado == "ON":
            self.__estado = "OFF"

    def interuptor(self):
        if self.__estado == "OFF":
            self.__estado = "ON"
        if self.__estado == "ON":
            self.__estado = "OFF"