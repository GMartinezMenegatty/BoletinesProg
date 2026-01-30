texto = "Python Python Python"
texto_sin_espacios = texto.replace(" ", "")

vocales = 0

for v in "aeiouAEIOU":
    vocales += texto_sin_espacios.count(v)

total_letras = len(texto_sin_espacios)

consonantes = total_letras - vocales

print("El texto tiene", vocales, "vocales y", consonantes, "consonantes.")