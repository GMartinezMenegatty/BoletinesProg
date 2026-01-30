nom1 = str(input("Escribe un nombre: "))
peso1 = int(input("Escribe su peso: "))

nom2 = str(input("Escribe otro nombre: "))
peso2 = int(input("Escribe su peso: "))

if peso1 > peso2:
    print(f"{nom1} es mas pesado que {nom2}")
    print(f"la diferencia de peso es {peso1 - peso2} kg")
elif peso2 > peso1:
    print(f"{nom2} es mas pesado que {nom1}")
    print(f"la diferencia de peso es {peso2 - peso1} kg")