#Escribir funcións que dada unha cadena de caracteres:
#Imprima os dous primeiros caracteres. 	
#Imprima os tres últimos caracteres. 	
#Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca 	 	
#Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer. 

def primerosdoscaracteres (cadena):
    return cadena [0:2]
cadena= input("Escribe una palabra: ")
print (cadena [0:2])

def ultimostrescaracteres (cadena):
    return cadena [0:2]
cadena= input("Escribe una palabra: ")
print (cadena [-3: ])

def cadadoscaracteres (cadena):
    return cadena [0:2]
cadena= input("Escribe una palabra: ")
print (cadena [0: :2])

def cadenaigualalreves (cadena):
    return cadena [0:2]
cadena= input("Escribe una palabra: ")
print (cadena + cadena[::-1])