class Xogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__puntuacion = 0

    def get_nome (self):
        return self.__nome

    @property
    def nome(self):
        return self.__nome

    def get_puntuacion(self):
        return self.__puntuacion