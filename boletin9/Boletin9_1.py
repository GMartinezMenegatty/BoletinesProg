
class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._numPaginas = numPaginas
        self._valoracion = valoracion

    def getTitulo(self):
        return self._titulo

    def getAutor(self):
        return self._autor

    def getAno(self):
        return self._ano

    def getNumPaginas(self):
        return self._numPaginas

    def getValoracion(self):
        return self._valoracion

    def setTitulo(self, titulo):
        self._titulo = titulo

    def setAutor(self, autor):
        self._autor = autor

    def setAno(self, ano):
        self._ano = ano

    def setNumPaginas(self, num):
        self._numPaginas = num

    def setValoracion(self, val):
        self._valoracion = val

    def amosarLibro(self):
        return (f"Título: {self._titulo} | Autor: {self._autor} | Ano: {self._ano} | "
                f"Páxinas: {self._numPaginas} | Valoración: {self._valoracion}")



