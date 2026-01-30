from dniError import DniError
from nussError import NussError


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


class Persoa2:
    def __init__(self, nome, dni, edade):
        self.setNome (nome)
        self.setDni (dni)
        self.setEdade (edade)

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setDni(self, dni):
        if len(dni) == 9 :
            if dni[:-1].isdigit() :
                if dni[-1].isalpha():
                    letraDni = 'TRWAGMYFPDXBNJZSQVHLCKE'
                    resto = int(dni[:-1]) % 23
                    if letraDni[resto] == dni[-1:].upper():
                        self.__dni = dni
                    else:
                        raise DniError("Letra incorrecta")
                else:
                    raise DniError ("El ultimo digito no es una letra")
            else:
                raise DniError ("Los digitos no son numeros")
        else:
            raise DniError ("La longitud es incorrecta")

    def getDni(self):
        return self.__dni

    def setEdade(self,edade):
        if type(edade) == int:
            if edade >= 0:
                self.__edade = edade
            else:
                raise ValueError (f"O valor {edade} ten que ser maior que 0")
        else:
            raise TypeError(f"O tipo {type(edade)} non e o tipo correcto")

    def getEdade(self):
        return self.__edade

    nome = property(getNome,setNome)
    dni = property(getDni,setDni)
    edade = property(getEdade,setEdade)

class Trabajador (Persoa2):
    def __init__(self, nome, dni, edade, nuss):
        super().__init__(nome, dni, edade)
        self.setNuss (nuss)

    def setNuss(self, nuss):
        if len(nuss) == 16 :
            if nuss[2] == '/' and nuss[-3] == '/':
                if nuss[0:1].isdigit() and nuss[3:12].isdigit() and nuss[14:15].isdigit():
                    self.__nuss = nuss
                else:
                    raise NussError ("No son numeros")
            else:
                raise NussError ("El formato debe ser 'nn/nnnnnnnnnn/nn'")
        else:
            raise NussError (f"La longitud de {nuss} es incorrecta")






