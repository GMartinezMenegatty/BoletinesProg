class Xestor_Notas:
    def __init__(self, ruta):
        self.__ruta = ruta

    def engadir_nota(self, texto):
        if isinstance(texto, str):
            with open(self.__ruta,'a') as notas:
                notas.write(f"{texto}\n")

    def leer_notas(self):
        with open(self.__ruta, 'r') as notas:
            print(notas.read())


    def buscar_clave(self, palabra):
        with open(self.__ruta, 'r') as notas:
            lineas = notas.readlines()
            for linea in lineas:
                if palabra in linea:
                    print(linea)

    def menu(self):
        opcion = 999
        while opcion != 0:
            print("\n--- Xestion del almacén ---")
            print("1. Engadir nota")
            print("2. Leer notas")
            print("3. Buscar notas por palabra clave")
            print("0. Salir")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                opcion = str(input("Escribe lo que quieras guardar: "))
                self.engadir_nota(opcion)
            elif opcion == 2:
                self.leer_notas()
                print("Se ha guardado correctamente")
            elif opcion == 3:
                opcion = str(input("Cual es la palabra clave: "))
                self.buscar_clave(opcion)
                print("Se ha guardado correctamente")
            elif opcion == 0:
                print("Saliendo del programa...")
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    xestor = Xestor_Notas('notas.txt')
    xestor.menu()