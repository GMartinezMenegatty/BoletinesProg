from DniError import DniError

# 1.  Dadas as clases mostradas no diagrama UML (Persoa, Deportista), codificar os métodos setter para que si o crear o # obxecto do tipo 
# persoa se introduce un DNI non válido xere unha excepción do tipo DniNonValido. 
# Codificar o metodo setLicenza para que verifique que o formato da licenza sexa  correcto.
# O formato da licenza (aaaadddnnnnnn)  é  da seguinte maneira :

# aaaa, 4 números que representan o ano en curso.
# ddd, abreviatura do deporte (fut fútbol, bal balocesto, etc).
# nnnnnn, 6 números do número único de licenza.



class Persona:
    def __init__(self,nome, direccion, dni):
        self.set_nome(nome)
        self.set_direccion(direccion)
        self.setDni(dni)

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
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
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def get_direccion(self):
        return self.__direccion

    nome = property(get_nome, set_nome)
    direccion = property(get_direccion, set_direccion)
    dni = property(getDni, setDni)


class Deportista(Persona):
    def __init__(self,nome, dni,direccion, deporte, clube, licenza):
        super().__init__(nome, dni, direccion)
        self.set_Deporte(deporte)
        self.set_clube (clube)
        self.set_licenza(licenza)

    def set_Deporte(self, deporte):
        self.__deporte = deporte

    def get_Deporte(self):
        return self.__deporte   
    
    def set_clube(self, clube):
        self.__clube = clube
    
    def get_clube(self):
        return self.__clube

    def set_licenza(self, licenza):
        if len(licenza) == 13:
            if licenza[0:3].isdigit():
                if licenza[4:7].isalpha():
                    if licenza[7:].isdigit():
                        self.__licenza = licenza
                    else:
                        raise ValueError("Los ultimos 6 digitos deben ser numeros")
                else:
                    raise ValueError("Los digitos 5,6 y 7 deben ser letras")
            else:
                raise ValueError("Los primeros 4 digitos deben ser numeros")
        else:
            raise ValueError("La longitud de la licencia es incorrecta")
    
    def get_licenza(self):
        return self.__licenza
    
    licenza = property(get_licenza, set_licenza)
    deporte = property(get_Deporte, set_Deporte)
    clube = property(get_clube, set_clube)

try:
    juan = Deportista ( "juan", "00000000T","Florida", "fut", "Real Madrid", "2023fut123456")
except DniError as e:
    print(str(e))



