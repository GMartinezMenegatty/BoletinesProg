asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
suspendidas = []
i = 0

for asignatura in asignaturas:
    nota = int(input("Ingresa tu nota de "+asignatura + ": "))
    if nota < 5:
        notas.append(nota)
        suspendidas.append(asignatura)
for n in notas:
    print(suspendidas[i], notas[i])
    i += 1

