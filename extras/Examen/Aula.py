from extras.Examen.Equipo import Equipo
from extras.Examen.equipoNonExisteError import EquipoNonExisteError


class Aula:
    def __init__(self, nome: str, num_max_equipos: int):
        self.__nome = nome
        self.__num_max_equipos = num_max_equipos
        self._equipos = []

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome: str):
        self.__nome = nome

    def get_num_max_equipos(self):
        return self.__num_max_equipos
    def set_num_max_equipos(self, num_max_equipos: int):
        self.__num_max_equipos = num_max_equipos

    def numero_equipos(self):
        return self._equipos

    def get_equipo(self, codigo: str):
        for equipo in self._equipos:
            if equipo.codigo == codigo:
                return equipo
        return None

    def add_equipo(self, equipo:Equipo):
        self._equipos.append(equipo)
        if Equipo in self._equipos:
            return -1
        elif self._equipos >= self.__num_max_equipos:
            return -2
        return None

    def eliminar_equipo(self, codigo: str):
        if codigo in self._equipos:
            self._equipos.remove(Equipo)
            return True
        elif codigo not in self._equipos:
            return False
        return None

    def cambiar_estado_equipo(self, codigo: str, novo_estado: str):
        if Equipo not in self._equipos:
            raise EquipoNonExisteError ("El equipo no existe")

    def __str__(self):
        return f"{self.__nome} - {self._equipos}/{self.__num_max_equipos} equipos rexistrados"











