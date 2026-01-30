#Reemplace tódolos espazos polo caracter.
#Ex: ‘meu arquivo de texto.txt’ e ‘\_’ 
#debería devoltar ‘meu\_arquivo\_de\_texto.txt’

#Inserte o caracter entre cada letra da cadea.
#Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r

#Reemplace tódolos díxitos na cadea polo caracter.
#Ex: súa clave é: 1540 e ‘X’ debería devotar 
#súa clave é: XXXX

#Inserte o caracter cada 3 díxitos na cadea.
#Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0

def devolverpalabra(cadena, caracter):
    return cadena.replace(' ', caracter)
cadena = 'meu arquivo de texto.xml'
resultado = devolverpalabra(cadena, '/')
print(resultado)

def separador (cadena, caracter):
    resultado = ""
    for i in range(len(cadena)):
        resultado += cadena[i]
        if i != len(cadena) - 1:
            resultado += caracter
    return resultado
texto = "separar"
resultado = separador (texto, ",")
print(resultado)

def reemplazardigitos(cadena, caracter):
    resultado = ""
    for c in cadena:
        if c.isdigit():
            resultado += caracter
        else:
            resultado += c
    return resultado
texto = input("Ingrese su clave: ")
resultado = reemplazardigitos(texto,"X")
print(resultado)

def insertarcadatresdigitos(cadena, caracter):
    partes = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
    return caracter.join(partes)
texto = "2552552550"
resultado = insertarcadatresdigitos(texto, ".")
print(texto)
print(resultado)