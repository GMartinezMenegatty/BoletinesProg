
class Persoa:
    def __init__(self,nome,edade,dni,direccion,nacionalidade):
        self.nome = nome
        self.edade = edade
        self.dni = dni
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def nombre(self):
        cadeaNome = "Tu nombre:"+ str(self.nome)
        return cadeaNome

    def edad(self):
        edade = "Tu edade:"+ str(self.edade)
        return edade