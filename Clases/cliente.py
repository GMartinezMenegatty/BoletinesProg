
class Cliente:
    def __init__(self, nome, email, direccion, codigo_postal):
        self.__nome = nome
        self.email = email
        self.direccion = direccion
        self.codigo_postal = codigo_postal

    def __setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome


    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email


    def setDireccion(self, direccion):
        self.direccion = direccion
    def getDireccion(self):
        return self.direccion


    def setCodigoPostal(self, codigo_postal):
        self.codigo_postal = codigo_postal
    def getCodigoPostal(self):
        return self.codigo_postal

