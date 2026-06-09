from extras.Examen.Equipo import Equipo
from extras.Examen.Aula import Aula

class  Centro:
    def __init__(self, nome_centro: str, aulas):
        self.__nome_centro = nome_centro
        self._aulas = []

    def get_nome(self):
        return self.__nome_centro
    def set_nome(self, nome_centro):
        self.__nome_centro = nome_centro

    def get_aulas(self):
        return self._aulas
    def set_aulas(self, aulas):
        self._aulas = aulas

    def buscar_aula (self, nome_aula):
        for nome_aula in self._aulas:
            return nome_aula
        return None

    def mostrar_menu(self):
        print("1. Crear Aula.")
        print("2. Crear Equipo.")
        print("3. Eliminar Equipo.")
        print("4. Cambiar Estado dun equipo.")
        print("5. Importar os equipos dunha aula.")
        print("6. Sair.")

    def menu(self):
        global equipo
        opcion = 0
        while opcion != 6:
            self.mostrar_menu()
            opcion = input("Escriba la opcion que desee: ")
            match opcion:
                case 1:
                    aula = input("Escribe el aula que quieres crear: ")
                    Aula.append(Aula(equipo))

                case 2:
                    equipo = input("Escribe el equipo que quieres crear: ")
                    Equipo.append(Equipo(equipo))

                case 3:
                    eliminar = input("Escribe el equipo que quieres eliminar: ")
                    pass

                case 4:
                    pass

                case 5:
                    pass

def importar_aula( ruta_fichero):
    lista = []

    with open (ruta_fichero, "r") as fichero:
        for linea in fichero:
            resto = linea.split(",")
            if len(resto) == 1 :
                aula = resto[0]
            else:
                print (resto)
                #equipo = Equipo ()
                #lista.append(Equipo)


        tupla = aula, lista
        return tupla

importar_aula("aula.txt")