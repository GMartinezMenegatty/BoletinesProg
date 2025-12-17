
class Persoa:
    def __init__(self,nome,edade,dni,direccion,nacionalidade):
        self.nome = nome
        if self.comprobarEdade(edade):
            self.edade = edade
        else:
            self.edade = 0

        if self.comprobarDni(dni):
            self.dni = dni
        else:
            self.dni = "00000000X"
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def comprobarEdade(self,edade):
        if edade >= 0 and edade <= 150:
            return True
        else:
            return False

    def comprobarDni(self,dni):
        if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
            letraDni = 'TRWAGMYFPDXBNJZSQVHLCKE'
            resto = int(dni[:-1]) % 23
            if letraDni[resto] == dni[-1:].upper():
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        cadea = f"Nome: {self.nome}\n Edade: {self.edade}\n Dni: {self.dni}\n Direccion: {self.direccion}\n Nacionalidade: {self.nacionalidade}"
        '''cadea = "Nome: " + self.nome + "\n"
        cadea = cadea + "Dni: "+ self.dni + "\n"
        cadea = cadea + "Direccion: " + self.direccion + "\n"
        cadea = cadea + "Nacionalidade: " + self.nacionalidade + "\n"
        cadea = cadea + "Edade: " + str(self.edade) + "\n" '''
        return cadea

    def __eq__(self,outro):
        return self.dni == outro.dni

    def __gt__(self,outro):
        return self.edade > outro.edade

    def __lt__(self,outro):
        return self.edade < outro.edade


