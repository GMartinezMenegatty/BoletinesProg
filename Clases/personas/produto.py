
class Produto:
    def __init__(self, nome, prezo, cantidade_stock):
        self.__nome = nome
        self.prezo = prezo
        self.cantidade_stock = cantidade_stock

    def setNome(self):
        self.__nome = self.nome
    def getNome(self):
        return self.__nome

    def setPrezo(self, prezo):
        self.prezo = abs(prezo)

    def getPrezo(self):
        return self.prezo


    def setCantidadeStock(self, cantidade_stock):
        self.cantidade_stock = abs(cantidade_stock)

    def getCantidadeStock(self):
        return self.cantidade_stock

    def decrementarStock (self, cantidad):
        if self.cantidade_stock >= cantidad :
            self.cantidade_stock -= cantidad
            return True
        else:
            return False

    def incrementarStock(self, cantidad):
        if cantidad > 0:
            self.cantidade_stock += cantidad

    nome = property (setNome, getNome)
    prezo = property (setPrezo, getPrezo)
    cantidad = property (setCantidadeStock, getCantidadeStock)

