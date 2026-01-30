cadena = input("Ingrese una cadena de texto: ")
primeras_letras = "".join([palabra[0] for palabra in cadena.split()])

print(primeras_letras)


cadena = input("Ingrese una cadena de texto: ")

cadena_mayusculas = cadena.title()
print (cadena_mayusculas)


def encontrar_palabras_con_a(frase):
  palabras = frase.split()
  palabras_con_a = []
  for palabra in palabras:
    if palabra.startswith('a') or palabra.startswith('A'):
      palabras_con_a.append(palabra)
  return palabras_con_a

mi_frase = input("Ingresa una frase: ")
resultado = encontrar_palabras_con_a(mi_frase)
print(resultado)