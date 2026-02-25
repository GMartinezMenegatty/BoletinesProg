from xogador import Xogador


class Partida:
    def __init__(self, numXogadores):
        self.__xogadores = []
        self.__num_max_xogadores = numXogadores

    def add_xogador(self, xogador):
        if len(self.__xogadores < self.__num_max_xogadores):
            self.__xogadores.append(xogador)
            return len(self.__xogadores) -1
        else:
            return -1

    def get_xogador(self,nome):
        for xogador in self.__xogadores:
            if xogador.get_nome() == nome:
                return xogador
        return None



