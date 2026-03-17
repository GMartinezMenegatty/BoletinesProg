import csv

from Supermercado.producto import Producto


class Almacen:
    def __init__(self, rutaFicheiro):
        self.listaProductos = []
        self.cargarProductos(rutaFicheiro)

    def engadirProductos(self, producto):
        self.listaProductos.append (producto)

    def cargarProductos(self, ficheiro):
        with open(ficheiro, 'r', newline="") as fich:
            readerProductos = csv.DictReader(fich)
            for linhaProducto in readerProductos:
                p = Producto (linhaProducto['Nome'],
                          linhaProducto['Cantidade'],
                          linhaProducto['Prezo'])
                self.listaProductos.append(p)

if __name__ == "__main__":
    a = Almacen('productos.csv')