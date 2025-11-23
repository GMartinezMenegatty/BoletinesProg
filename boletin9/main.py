from Boletin9_1 import Libro
from Boletin9_2 import Consumo

class Principal:
    def main():
        libro1 = Libro("Mujercitas", "Alcott", 1868, 296, 10)
        print(libro1.amosarLibro())


Principal.main()

class Principal2:
    def main():
        obx1 = Consumo()
        obx1.setLitros(50)
        obx1.setPGas(1.57)

        obx2 = Consumo(500, 20, 500, 1.50)
        print("Consumo medio:", obx2.consumoMedio())

        obx2.setLitros(40)
        print("Velocidade media:", obx2.vMed)


Principal2.main()