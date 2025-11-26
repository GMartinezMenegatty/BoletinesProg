from Boletin9_1 import Libro
from Boletin9_2 import Consumo
from Boletin9_3 import Coche
from Boletin9_4 import Conta

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

class Boletin_9_3:
    def main():
        car = Coche()
        car.acelerar(50)
        car.frenar(20)
        print("Velocidade final:", car.getVelocidade())


Boletin_9_3.main()

class Principal4:
    def main():
        c1 = Conta("Ana", "1234", 1.5, 1000)
        c2 = Conta("Luis", "9999", 1.2, 500)

        c1.transferencia(c2, 200)

        print("Saldo Ana:", c1.getSaldo())
        print("Saldo Luis:", c2.getSaldo())


Principal4.main()
