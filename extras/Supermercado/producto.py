class Producto:
    def __init__(self, nome, cantidade, prezo):
        self.__nome = nome
        self.__cantidade = cantidade
        self.__prezo = prezo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cantidade(self):
        return self.__cantidade

    @cantidade.setter
    def cantidade(self, cantidade):
        self.__cantidade = cantidade

    @property
    def prezo(self):
        return self.__prezo

    @prezo.setter
    def prezo(self, prezo):
        self.__prezo = prezo

    def calcular_valor_prezo(self):
        return self.__prezo * self.__cantidade




