'''Gabriela Martinez Menegatty'''


'''Suposto 1'''
class Barcos:
    def __init__(self, nome, matricula, bandeira, num_equipo_salvavidas):
        self.__nome = nome
        self.__matricula = matricula
        self.__bandeira = bandeira
        self.num_equipo_salvavidas = num_equipo_salvavidas

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def bandeira(self):
        return self.__bandeira

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira
        
    def num_salvavidas(self):
        pass
        
        
    def calculo_facturacion(self, millas:float, porcentaxe_ocupacion:float):
        contenedores = 0.31 * millas * porcentaxe_ocupacion / 100
        clase_1 = 0.7 * millas * porcentaxe_ocupacion / 100
        clase_turista = 0.55 * millas * porcentaxe_ocupacion / 100
        turismos = 1.5 * millas * porcentaxe_ocupacion / 100
        camions = 3.3 * millas * porcentaxe_ocupacion / 100
        return f"Facturacion total: {contenedores}, {clase_1}, {clase_turista}, {turismos}, {camions}"
        
    def __str__(self):
        return f"El nome del barco es: {self.nome},\n Su matricula: {self.matricula},\n Su bandeira: {self.bandeira},\n Su cantidad de salvavidas: {self.num_equipo_salvavidas}"

class Contenedores(Barcos):
    def __init__(self, capacidade_toneladas, num_compartimentos):
        Barcos.__init__(self)
        self.capacidade_toneladas = capacidade_toneladas
        self.num_compartimentos = num_compartimentos


'''Suposto 2'''

def comprobar_matricula (self, matricula):
    matricula = []
    engadir = input("Ingrese la matricula a comprobar: ")
    matricula.append(engadir)
    if matricula [0:1] == "7a":
        if matricula[3:] == "VI-2-63-19":
            return True
        raise ValueError ("La matricula es equivocada")
    else:
        return False

'''Suposto 3'''

class LinhaTren:
    def __init__(self, numero: str, orixe:str, destino:str, capacidade:int):
        self.numero = numero
        self.orixe = orixe
        self.destino = destino
        self.capacidade = capacidade

    def engadir_linha(self):
        LinhaTren = []
        LinhaTren.append(self.numero)
        LinhaTren.append(self.orixe)
        LinhaTren.append(self.destino)
        LinhaTren.append(self.capacidade)

    def dar_alta(self):
        pass

    def buscar_linha(self):
        orixe = []

        for i in range(len(self.orixe)):
            orixe.append(self.orixe[i])

    def borrar_linha(self, linea):
        lineas = LinhaTren
        if linea in lineas:
            pass




    def menu_linha(self):

        opcion = 0
        while (opcion != 4):
            self.mostrar_menu()
            opcion = input("Escriba la opcion que desee: ")
            match (opcion):
                case 1:
                    self.dar_alta()

                case 2:
                    pais = input("Escribe el pais que quieras buscar: ")
                    self.buscar_linha(pais)
                    if pais in self.orixe:
                        print(pais)

                case 3:
                    self.borrar_linha()

    def mostrar_menu(self):
        print("1. Dar de alta unha liña.")
        print("2. Buscar liñas cun orixe determinado.")
        print("3. Borrar unha liña por numero.")
        print("4. Salir.")


'''Suposto 4'''

def leer_fichero (self, ruta):
    with open(ruta, 'r') as fichero:
        for linha in fichero:
            espazo1 = linha.index(":")
            espazo2 = linha.index(":", espazo1 + 1)
            espazo3 = linha.index("-", espazo2 + 1)
            espazo4 = linha.index("-", espazo3 + 1)
            num_linha = linha[:espazo1]
            orixe = linha[espazo1 + 1:espazo2]
            destino = linha[espazo2 + 1:espazo3]
            num_max_pasajeros = linha[espazo3 + 1:espazo4]
            try:
                self.leer_fichero(f"{num_linha}:{orixe}-{destino} {num_max_pasajeros}")
            except ValueError as e:
                print(e)








