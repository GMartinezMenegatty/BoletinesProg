dni = int(input("digite su dni: "))

tabla = [
    "T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"
    ]
letra = dni % 23
print(f"Tu dni completo es:{dni}{tabla[letra]}")