from string import punctuation

from ExamenNavieira.equipo import Equipo
import csv


class Torneo:
    def __init__(self, nome, num_max_equipos):
        self.__nome = nome
        self.__equipos = []
        self.__num_max_equipos = num_max_equipos

    @property
    def nome(self):
        return self.__nome

    def get_equipo(self, nome):
        for equipo in self.__equipos:
            if equipo.nome == nome:
                return equipo
        return None

    def add_equipo(self, equipo):
        if len(self.__equipos) < self.__num_max_equipos:
            if not equipo in self.__equipos:
                self.__equipos.append(equipo)
                return len(self.__equipos) - 1
            else:
                return -1
        else:
            return -1

    def rexistrar_encontro(self, encontro_resultado):
        """Rexistra o resultado dun encontro a partir dunha cadea de texto.

        Analiza a cadea con formato 'local-visitante resultadoLocal-resultadoVisitante', filtra
        e rexistra o resultado no equipa correspondente.

        En primeiro lugar se separa o nome das equipas do resultado, que están separados por
        un espazo. Despois se separa o texto que describe  o nome do local e o visitante, amén
        do resultado de cada un deles.  Estes dous textos están separados por un guión.

        Posteriormente se busca o equipo local e visitante na lista de equipos do torneo. Se
        existen, rexístrase a victoria, empate ou derrota, dependendo da comparación numérica
        dos resultados.

        :param encontro_resultado: Cadea de texto (str) con formato 'local-visitante resultadoLocal-resultadoVisitante'
        :return:
        :exception: ValueError

        """
        encontro, resultado = encontro_resultado.split()
        nome_local, nome_visitante = encontro.split('-')
        r_local, r_visitante = resultado.split('-')
        print(nome_local)
        print(nome_visitante)
        local = self.get_equipo(nome_local)

        visitante = self.get_equipo(nome_visitante)
        if local is not None and visitante is not None:
            if int(r_local) > int(r_visitante):
                local.add_victoria()
                visitante.add_perdido()
            elif int(r_local) < int(r_visitante):
                local.add_perdido()
                visitante.add_victoria()
            else:
                local.add_empate()
                visitante.add_empate()
        else:
            raise ValueError(f"Un dos equipos non está na lista do torneo {local} {visitante}")

    def numero_equipos(self):
        return len(self.__equipos)

    def get_equipos(self):
        return self.__equipos

    def get_clasificacion(self):
        l_aux = self.__equipos[:]
        lClasificacion = []

        while len(l_aux) > 1:
            ind_aux = 0
            for i in range(len(l_aux) - 1):
                if l_aux[ind_aux].get_puntos() < l_aux[i + 1].get_puntos():
                    ind_aux = i + 1
            equipo = l_aux.pop(ind_aux)
            lClasificacion.append(equipo)
        lClasificacion.append(l_aux[0])
        return lClasificacion

    def importar_resultados_ficheiro(self, ruta):
        """Importa os resultados dos enfrontamentos do torneo dende un ficheiro.

        Abrimos ficheiro. Leemos liña a liña. Rexistramos o resultado
        do encontro chamando o método rexistrar_resultado. Pechamos
        ficheiro.

        O formato da liña do ficheiro é "local-visitante resultadoLocal-resultadoVisitante"

        :param ruta:
        :return:
        """
        ficheiro = open(ruta, "r")
        # for linha in ficheiro:
        #   self.rexistrar_encontro (linha)
        while linha := ficheiro.readline():
            self.rexistrar_encontro(linha)
        ficheiro.close()

    def importar_resultados_ficheiro2(self, ruta):
        """Importa os resultados dos enfrontamentos do torneo dende un ficheiro.

        Abrimos ficheiro. Leemos liña a liña. Rexistramos o resultado
        do encontro chamando o método rexistrar_resultado. Pechamos
        ficheiro.

        O formato da liña do ficheiro é "local visitante (resultadoLocal, resultadoVisitante)

        :param ruta:
        :return:
        """
        with open(ruta, 'r') as ficheiro:
            for linha in ficheiro:
                espazo1 = linha.index(" ")
                espazo2 = linha.index(" ", espazo1 + 1)
                local = linha[:espazo1]
                visitante = linha[espazo1 + 1:espazo2]
                # resultado = linha [espazo2+1:-1]
                resultado = linha[espazo2 + 1:]
                resultado = resultado.replace("(", "")
                resultado = resultado.replace(")", "")
                rLocal, rVisitante = resultado.split("-")
                try:
                    self.rexistrar_encontro(f"{local}-{visitante} {rLocal}-{rVisitante}")
                except ValueError as e:
                    print(e)

    def importar_resultados_ficheiro_CSV(self, ruta):
        """Importa os resultados dos enfrontamentos do torneo dende un ficheiro CSV.

        Abrimos ficheiro. Leemos liña a liña. Rexistramos o resultado
        do encontro chamando o método rexistrar_resultado. Pechamos
        ficheiro.

        O formato da liña do ficheiro é "local visitante (resultadoLocal, resultadoVisitante)

        :param ruta:
        :return:
        """

        with open(ruta, 'r', newline="") as ficheiro:
            ficheiro.readline()
            reader = csv.reader(ficheiro)
            for linha in reader:
                print(linha)
                local = linha [0].strip()
                visitante = linha[1].strip()
                rLocal = linha [2].strip()
                rVisitante = linha [3].strip()

                try:
                    self.rexistrar_encontro(f"{local}-{visitante} {rLocal}-{rVisitante}")
                except ValueError as e:
                    print(e)

    def crear_ficheiro_clasificacion_CSV (self, nomeFich):
        """
        Crea un ficheiro con clasificion do torneo en formato CSV

        :param nomeFich: nome do Ficheiro onde se garda a clsificacion
        :return:
        """
        clasificacion = self.get_clasificacion()

        with open(nomeFich, 'w', newline="") as ficheiro:
            writer = csv.writer(ficheiro, delimiter=',')
            writer.writerow(['Equipo', 'Puntuacion'])
            for equipo in clasificacion:
                nome = equipo.nome
                puntuacion = equipo.get_puntos()
                writer.writerow ([nome, puntuacion])

    def crear_ficheiro_clasificacion_CSV_dict (self, nomeFich):
        """
        Crea un ficheiro con clasificion do torneo en formato CSV

        :param nomeFich: nome do Ficheiro onde se garda a clsificacion
        :return:
        """
        clasificacion = self.get_clasificacion()

        with open(nomeFich, 'w', newline="") as ficheiro:
            cabeceira = ['Nome', 'Puntuacion']
            writer = csv.DictWriter(ficheiro, fieldnames = cabeceira)
            writer.writeheader()
            for equipo in clasificacion:
                nome = equipo.nome
                puntuacion = equipo.get_puntos()
                writer.writerow ({'Nome': nome, 'Puntuacion': puntuacion})





if __name__ == "__main__":
    t = Torneo("Tutextrem", 6)
    e = Equipo("Celta")
    t.add_equipo(e)
    e = Equipo("Sevilla")
    t.add_equipo(e)
    e = Equipo("Español")
    t.add_equipo(e)
    e = Equipo("Girona")
    t.add_equipo(e)
    e = Equipo("Villareal")
    t.add_equipo(e)
    e = Equipo("Betis")
    t.add_equipo(e)
    print(t.get_equipos())
    print(t.get_clasificacion())
    t.importar_resultados_ficheiro_CSV(
        "/home/dam/PROG/extras/Examen/resultados4xornada.csv")
    t.crear_ficheiro_clasificacion_CSV("clasificacion.csv")
    t.crear_ficheiro_clasificacion_CSV_dict("clasificacionDict.csv")

    for equipo in t.get_clasificacion():
        print (equipo.nome)
        print (equipo.get_puntos())
'''
    with open('clasificacion.csv', 'a', newline="") as ficheiro:
        for equipo in t.get_clasificacion():
            writer = csv.writer(ficheiro)
            writer.writerow(t.get_clasificacion())
'''


