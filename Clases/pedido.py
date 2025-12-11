#from cliente import Cliente
from produto import Produto
from data import Data
'''
eliminarPrduto
engadirProduto
calcularPrezoTotal
calculoIva
mostrarCesta
'''

class Pedido:
    def __init__(self, cesta_produto, cliente, data):
        self.cesta_pedido = list(cesta_produto)
        self.cliente = cliente
        self.data = data

    def getCestaPedido(self):
        return self.cesta_pedido


    def setCliente(self, cliente):
        self.cliente = cliente
    def getCliente(self):
        return self.cliente


    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data

    def setCodigoPostal(self, codigo_postal):
        self.codigo_postal = codigo_postal
    def getCodigoPostal(self):
        return self.codigo_postal

    def eliminarProduto(self):
        pass

    def engadirProduto(self, produto, cantidad):
        if produto.decrementarStock(cantidad):
            self.cesta_pedido.append((produto, cantidad))


    def calcularPrezoTotal(self):
        total = 0
        for entrada in self.cesta_pedido:
            total = total + entrada[1] * entrada[0].getPrezo()

    def calculoIva(self):
        iva = self.calcularPrezoTotal() * 0.21
        return iva

    def mostrarCesta(self):      
        for entrada in self.cesta_pedido:
                print(f"Produto: {entrada[0].getNome()} - Cantidade: {entrada[1]} - Prezo unitario: {entrada[0].getPrezo()} ")  

    cesta_pedido = property (getCestaPedido)
    cliente = property (setCliente, getCliente)
    data = property (setData, getData)
    codigo_postal = property (setCodigoPostal, getCodigoPostal)

