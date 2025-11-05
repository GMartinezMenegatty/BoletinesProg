
usuContra = [["Manuel", "canMorto"], ["pepe", "usuaya"]]

def comprobarUsuario (listaUsuarioContrasinal):
    existeUsuario = False
    nomeUsuario = input("Ingrese el nombre del usuario: ")
    contrasinal = input("Ingrese la contrasinal del usuario: ")
    for usuarioContrasinal in listaUsuarioContrasinal:
        if usuarioContrasinal[0] == nomeUsuario:
            if usuarioContrasinal[1] == contrasinal:
                existeUsuario = True

    return existeUsuario

existe = comprobarUsuario(usuContra)

if existe:
    print("Usuario validado")
else:
    print("Usuario no valido")


def comprobarLonxitude (contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False

def comprobarMaiusculasContrasinal (contrasinal):
    maiusculas = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for letra in contrasinal:







