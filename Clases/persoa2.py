class Persoa:
    def __init__(self, nome, dni, nuss, telefono):
        self._nome = nome
        self._dni = dni
        self._nuss = nuss
        self._telefono = telefono
#        self._iniJor = iniJor
#        self._finJor = finJor

    def setNome (self, nome):
        self._nome = nome
    def getNome (self):
        return self._nome
    def setDni(self, dni):
        self._dni = dni
    def getDni(self):
        return self._dni
    def setNuss (self, nuss):
        self._nuss = nuss
    def getNuss (self):
        return self._nuss
    def setTelefono (self, telefono):
        self._telefono = telefono
    def getTelefono (self):
        return self._telefono
#    def setIniJor (self, iniJor):
#        self._iniJor = iniJor
#    def getIniJor (self):
#        return self._iniJor
 #   def setFinJor (self, finJor):
 #       self._finJor = finJor
 #   def getFinJor (self):
 #       return self._finJor
    def comprobacionNuss (self):
        if len(self._nuss) == 14:
            if self._nuss[2] == "/" and self._nuss[11] == "/":
                numss = self._nuss.replace("/", "")
                numeros = ""
                for num in numss:
                    if num.isdigit():
                        numeros = numeros + num
                if len(numeros) == 12:
                    return True
                else:
                    self._nuss = "00/00000000/00"
            else:
                self._nuss = "00/00000000/00"

#   def comprobacionTelefono (self):
#        if len(self._telefono) == 14:
#            if self._telefono[0] == "+" and self._telefono[3] == " " and self._telefono[7] == " " and self._telefono[11] == " ":
 #               return self._telefono
 #           else:
 #               return "+00 000 000 000"

#    def calcularMinutos(self):
persona1 = Persoa("n1", "123A", "00/123p5678/90", "+34 123 456 789")
print(persona1.comprobacionNuss())




