texto = "Ola, son alumno de DAM1, e son programador desde o 2025"

espacios = texto.count(" ")
print(espacios)

digitos = sum(texto.count(d) for d in "0123456789")
print(digitos)

letras = sum(1 for c in texto if c.isalpha())
print(letras)   

