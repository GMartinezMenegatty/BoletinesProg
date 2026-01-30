from persoa import Persoa

class Alumno(Persoa):
    contar = 3
    def __init__(self, nome, edade, dni, direccion, nacionalidad, ciclo):
        super().__init__(nome, edade, dni, direccion, nacionalidad)
        self.ciclo = ciclo

    def sumar(self):
        Alumno.contar += 1
        self.sumar()


alumno1 = Alumno('Manuel', 29, '1234H', 'Su casa', 'es','DAM')
alumno2 = Alumno('Pepe', 62, '4321Q', 'Tu trastero', 'fr','ASIR')
alumno3 = Alumno('Maria', 44, '5678K', 'Debajo de un puente', 'po','DAW')



print(Alumno.contar)