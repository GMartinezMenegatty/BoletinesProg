#texto = " una cadena cualquiera "
#print(texto)

#t = [" una", "cadena", "cualquiera "]



def limpiadorCadenas (cadena):
    for c in cadena:
        if c == ' ':
            cadena = cadena[1:]
        else:
            break
    for i in range (len(cadena)-1, -1, -1):
        if cadena[i] == ' ':
            cadena = cadena[:i]
        else:
            break
    return cadena

limpiar = limpiadorCadenas('')