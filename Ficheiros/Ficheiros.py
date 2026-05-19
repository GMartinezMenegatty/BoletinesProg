
ficheiro = open('/home/dam/PROG/extras/contraseña.py')

for linha in ficheiro:
    print(linha)

ficheiro.close()

class Barco:
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes):

        self.set_eslora(eslora)
        self.set_toneladas_carga(toneladas_carga)
        self.set_calado(calado)
        self.set_potencia(potencia)
        self.set_velocidade(velocidade)
        self.set_consumo_medio(consumo_medio)
        self.__nome = nome
        self.__matricula = matricula
        self.set_num_tripulantes(num_tripulantes)


    def get_eslora(self):
        return self.__eslora
    def get_toneladas_carga(self):
        return self.__toneladas_carga
    def get_calado(self):
        return self.__calado
    def get_potencia(self):
        return self.__potencia
    def get_velocidade(self):
        return self.__velocidade
    def get_consumo_medio(self):
        return self.__consumo_medio
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def get_num_tripulantes(self):
        return self.__num_tripulantes

    def set_eslora(self, eslora):
        if eslora > 0:
            self.__eslora = eslora
        else:
            raise ValueError("Cantidad invalida")

    def set_toneladas_carga(self, toneladas_carga):
        if toneladas_carga >= 0:
            self.__toneladas_carga = toneladas_carga
        else:
            raise ValueError("Cantidad invalida")

    def set_calado(self, calado):
        if calado > 0:
            self.__calado = calado
        else:
            raise ValueError("Cantidad invalida")

    def set_potencia(self, potencia):
        if potencia > 0:
            self.__potencia = potencia
        else:
            raise ValueError("Cantidad invalida")

    def set_velocidade(self, velocidade):
        if velocidade >= 0:
            self.__velocidade = velocidade
        else:
            raise ValueError("Cantidad invalida")

    def set_consumo_medio(self, consumo):
        if consumo >= 0:
            self.__consumo_medio = consumo
        else:
            raise ValueError("Cantidad invalida")

    def set_num_tripulantes(self, num_tripulantes):
        if num_tripulantes > 0:
            self.__num_tripulantes = num_tripulantes
        else:
            raise ValueError("Cantidad invalida")

    # Metodos obligatorios
    def calculo_custe_consumo(self, dias: int, prezo: float) -> float:
        if dias < 0 or prezo < 0:
            raise ValueError("Datos invalidos")
        return self.__consumo_medio * dias * prezo

    def calculo_facturacion(self, prezo, millas, porcentaxe_ocupado):
        facturacion = prezo * millas * porcentaxe_ocupado/100
        return facturacion

    def __str__(self):
        return f"Barco\nNome: {self.__nome}\nMatricula: {self.__matricula}\nEslora: {self.__eslora}\nToneladas de carga: {self.__toneladas_carga}\nCalado: {self.__calado}\nPotencia: {self.__potencia}\nVelocidade: {self.__velocidade}\nConsumo medio: {self.__consumo_medio}\nNumero de tripulantes: {self.__num_tripulantes}"

class BarcoAuxiliar(Barco):
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion):

        super().__init__(eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes)

        self.set_capacidade_conxelacion(capacidade_conxelacion)

    def get_capacidade_conxelacion(self):
        return self.__capacidade_conxelacion

    def set_capacidade_conxelacion(self, capacidade):
        if capacidade > 0:
            self.__capacidade_conxelacion = capacidade
        else:
            raise ValueError("Cantidad invalida")

    def __str__(self):
        return f"Auxiliar: {super().__str__()} "


class BarcoAuxiliarFuel(BarcoAuxiliar):
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion, capacidade_fuel):

        super().__init__(eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion)

        self.set_capacidade_fuel(capacidade_fuel)

    def get_capacidade_fuel(self):
        return self.__capacidade_fuel

    def set_capacidade_fuel(self, capacidade):
        if capacidade > 0:
            self.__capacidade_fuel = capacidade
        else:
            raise ValueError("Cantidad invalida")

    def __str__(self):
        return f"{super().__str__()}\nFuel: {self.__capacidade_fuel} "

#2
import csv

class Asento:
    def __init__(self, numero: str, clase: str):
        self.numero = numero
        self.clase = clase
        self.ocupado = False
        self.pasaxeiro = None

    def leer_csv(self):
        asientos = []
        with open("asentos.csv", newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                numero = fila["numero"]
                clase = fila["clase"]
                asiento = Asento(numero, clase)
                asientos.append(asiento)
        print(f"Archivo .csv leído: {asientos}")
        return asientos

    def mostrar_csv(self):
        lista = []
        try:
            with open("asentos.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

                if not lineas:
                    print("No hay pasajeros guardados.")
                else:

                    for linea in lineas:
                        numero, clase, ocupado, pasaxeiro = linea.strip().split(",")

                        persona = (numero,clase,ocupado,pasaxeiro)
                        lista.append(persona)
                    return lista

        except FileNotFoundError:
            print("El archivo no existe todavía.")


    def __str__(self):
        return f"Asento: {self.numero} {self.clase}"

    def __abs__(self):
        return f"Asento: {self.numero} {self.clase}"

#3
def crear_asentos(num_asentos):
    lista = []

    num_business = int(num_asentos * 0.10)
    num_preferente = int(num_asentos * 0.20)

    contador = 1

    while len(lista) < num_asentos:
        if contador == 13:
            contador += 1
            continue

        if len(lista) < num_business:
            clase = "business"
        elif len(lista) < num_business + num_preferente:
            clase = "preferente"
        else:
            clase = "turista"
        añadir = [contador,clase,False,None]
        lista.append(añadir)
        contador += 1
    return lista

def buscar_asento_libre(lista, clase):
    for asento in lista:
        if asento[1] == clase and not asento.ocupado:
            return asento
        else:
            return None

def ocupar_asento(lista, numero, nome_pasaxeiro):
    for asento in lista:
        print(asento[0])
        if asento[0] == numero:
            if asento[2] == False:
                asento[2] = True
                asento[3] = nome_pasaxeiro
                print("asignado")

        else:
            print("no asignado")

    print("Asento non atopado")
    return None

#4
def ler_ocupacion(ruta_ficheiro):
    lista = []

    with open(ruta_ficheiro, encoding='utf-8') as f:
        for liña in f:
            liña = liña.strip()

            # Eliminar "Asento:"
            contido = liña.replace("Asento:", "").strip()

            partes = contido.split()

            numero = partes[0]
            clase = partes[1]
            estado = " ".join(partes[2:])

            asento = Asento(numero, clase)

            if estado != "libre":
                asento.ocupado = True
                asento.pasaxeiro = estado

            lista.append(asento)

    return lista


import csv


# Ejercicio 1
class Barco:
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes):
        self.set_nome = nome
        self.set_matricula(matricula)
        self.set_bandeira(bandeira)
        self.set_salvavidas(salvavidas)
        self.set_eslora(eslora)
        self.set_volume(volume)
        self.set_tripulantes(tripulantes)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_bandeira(self):
        return self.__bandeira

    def set_bandeira(self, bandeira):
        self.__bandeira = bandeira

    def get_salvavidas(self):
        return self.__salvavidas

    def set_salvavidas(self, salvavidas):
        self.__salvavidas = salvavidas

    def get_eslora(self):
        return self.__eslora

    def set_eslora(self, eslora):
        self.__eslora = eslora

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_tripulantes(self):
        return self.__tripulantes

    def set_tripulantes(self, tripulantes):
        if tripulantes > self.__salvavidas:
            raise ValueError("A tripulación non pode superar os salvavidas")
        self.__tripulantes = tripulantes

    def calculo_facturacion(self):
        pass

    def __str__(self):
        return f"Nome: {self.__nome}, Matricula: {self.__matricula}, Bandeira: {self.__bandeira}, Salvavidas: {self.__salvavidas}, Eslora: {self.__eslora}, Volume: {self.__volume}, Tripulantes: {self.__tripulantes}"


class BarcoPasaxeiros(Barco):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera,
                 prazas_turista):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes)
        self.set_prazas_primera(prazas_primera)
        self.set_prazas_turista(prazas_turista)

    def get_prazas_primera(self):
        return self.__prazas_primera

    def set_prazas_primera(self, valor):
        if (valor + self.get_tripulantes()) > self.get_salvavidas():
            raise ValueError("Superase a capacidade de salvavidas")
        self.__prazas_primera = valor

    def get_prazas_turista(self):
        return self.__prazas_turista

    def set_prazas_turista(self, valor):
        if (valor + self.get_tripulantes()) > self.get_salvavidas():
            raise ValueError("Supérase a capacidade de salvavidas")
        self.__prazas_turista = valor

    def calculo_facturacion(self, millas, porcentaxe_ocupacion):
        facturacion_primera = self.__prazas_primera * porcentaxe_ocupacion * millas * 0.7
        facturacion_turista = self.__prazas_turista * porcentaxe_ocupacion * millas * 0.55
        return facturacion_primera + facturacion_turista

    def __str__(self):
        return super().__str__() + f", 1ª Clase: {self.__prazas_primera}, Turista: {self.__prazas_turista}"


class BarcoPasaxeirosVehiculos(BarcoPasaxeiros):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera,
                 prazas_turista, prazas_turismos):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera,
                         prazas_turista)
        self.set_prazas_turismos(prazas_turismos)

    def get_prazas_turismos(self):
        return self.__prazas_turismos

    def set_prazas_turismos(self, valor):
        self.__prazas_turismos = valor

    def calculo_facturacion(self, millas, porcentaxe_ocupacion):
        base = super().calculo_facturacion(millas, porcentaxe_ocupacion)
        return base + (self.__prazas_turismos * porcentaxe_ocupacion * millas * 1.5)

    def __str__(self):
        return super().__str__() + f", Turismos: {self.__prazas_turismos}"


class BarcoPasaxeirosCompleto(BarcoPasaxeirosVehiculos):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera,
                 prazas_turista, prazas_turismos, prazas_camions):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera,
                         prazas_turista, prazas_turismos)
        self.set_prazas_camions(prazas_camions)

    def get_prazas_camions(self):
        return self.__prazas_camions

    def set_prazas_camions(self, valor):
        self.__prazas_camions = valor

    def __str__(self):
        return super().__str__() + f", Camións: {self.__prazas_camions}"


# Ejercicio 2
class Barco2:
    def __init__(self, matricula):
        self.__matricula = self.__verificar_matricula(matricula)

    def get_matricula(self):
        return self.__matricula

    def __verificar_matricula(self, matricula):
        partes = matricula.split("-")
        if len(partes) != 4:
            raise ValueError("Formato de matricula incorrecto")

        inicio = partes[0].split(" ")
        if len(inicio) != 2 or not inicio[0].endswith("ª"):
            raise ValueError("Erro na lista de actividade ou provincia")

        if not (partes[1].isdigit() and partes[2].isdigit() and len(partes[3]) == 2):
            raise ValueError("Erro nos díxitos de distrito, folio ou ano")

        return matricula


# Ejercicio 3
class LinhaTren:
    def __init__(self, numero: str, orixe: str, destino: str, capacidade: int):
        self.numero = numero
        self.orixe = orixe
        self.destino = destino
        self.capacidade = capacidade


def xestionar_linhas():
    linhas = []
    while True:
        print("\n1. Alta | 2. Buscar por orixe | 3. Borrar por numero | 4. Sair")
        opcion = input("Opción: ")

        if opcion == "1":
            numero = input("Numero: ")
            orixe = input("Orixe: ")
            destino = input("Destino: ")
            capacidade = int(input("Capacidade: "))
            linhas.append(LinhaTren(numero, orixe, destino, capacidade))
        elif opcion == "2":
            busqueda = input("Orixe a buscar: ")
            for linha in linhas:
                if linha.orixe == busqueda:
                    print(f"Liña {linha.numero} con destino {linha.destino}")
        elif opcion == "3":
            borrar = input("Numero de liña a borrar: ")
            linhas = [linha for linha in linhas if linha.numero != borrar]
        elif opcion == "4":
            break
    return linhas


# Ejercicio 4
def ler_ficheiro_tren(suposto4):
    lista_tren = []
    try:
        with open(suposto4.txt, 'r') as f:
            for linea in f:
                if linea.strip():
                    parte_num, resto = linea.split(":")
                    parte_ruta, parte_prazas = resto.strip().split("Prazas:")
                    orixe, destino = parte_ruta.strip().split("-")

                    obxecto = LinhaTren(
                        parte_num.strip(),
                        orixe.strip(),
                        destino.strip(),
                        parte_prazas.strip()
                    )
                    lista_tren.append(obxecto)
    except FileNotFoundError:
        print("Ficheiro non atopado")
    return lista_tren

