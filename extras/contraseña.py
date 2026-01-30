import random

def crearContraseña(n):
    t = ['1234567890', 'abcdefghijklmnñopqrstuvwxyz', 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ', '-_.:,;´{[]+*^°¸¡¿}?=()/&%$·"!ª']
    i=0
    contraseña=''
    while i<n:
        tipo = random.randint(0, 3)
        isim = random.randint(0,len(t[tipo])-1)
        contraseña = contraseña + t[tipo][isim]
        i+=1
    return contraseña

 while True:
     n=input("Ingrese la longitud de la contraseña: ")
     if n >= 6 and n <= 12:
         print(crearContraseña(n))
         if n == 0:
             break
         else:
             print("La longitud valida es entre 6 y 12")
