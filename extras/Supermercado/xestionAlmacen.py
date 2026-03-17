from Supermercado.almacen import Almacen
from Supermercado.producto import Producto


class XestionAlmacen:
    def __init__(self):
        almacen = Almacen('productos.csv')

    def menuPrincipal(self):

        while True:
            print("Programa de xestion de almacen")
            print("------------------------------")
            print("1. Listar Productos.")
            print("2. Engadir producto")
            print("3. Sair")
            opcion = input("Elixa unha opcion")
            match opcion:
                case '1':
                    self.mostrarProductos()
                case '2':
                    self.dialogoEngadirProducto()
                case '3':
                    break

    def mostrarProductos(self):
        for producto in self.almacen.listaProductos:
            print(f"Cantidade {producto.nome}: {producto.cantidade}")
            print(f"Prezo: {producto.prezo}")


    def dialogoEngadirProducto(self):
        nome = input("Introduzca nome do producto: ")
        cantidade = input("Introduzca a cantidade: ")
        prezo = float (input("Introduzca prezo do producto: "))
        print(f"Vai a introducir {cantidade} unidades do producto {nome} a {prezo}")
        correcto = input("E correcto? (s/n")
        if correcto == 's':
            self.almacen.introducirProducto(Producto(nome, cantidade, prezo))


if __name__ == '__main__':
    xestor = XestionAlmacen()
    xestor.mostrarProductos()


