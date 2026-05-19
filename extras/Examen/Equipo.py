class Equipo:
    def __init__(self, codigo: str, procesador: str, ram: int, disco: int):
        self.__codigo = codigo
        self._procesador = procesador
        self._ram = ram
        self._disco = disco
        self.estado = "Operativo"

    def get_codigo(self):
        return self.__codigo
    def set_codigo(self, codigo: str):
        self.__codigo = codigo

    def get_procesador(self):
        return self._procesador
    def set_procesador(self, procesador: str):
        self._procesador = procesador

    def get_ram(self):
        return self._ram
    def set_ram(self, ram: int):
        self._ram = ram

    def get_disco(self):
        return self._disco
    def set_disco(self, disco: int):
        self._disco = disco

    def __str__(self):
        return f"{self.__codigo} {self._procesador} | RAM: {self._ram} GB| Disco: {self._disco} GB| Estado: {self.estado}"





