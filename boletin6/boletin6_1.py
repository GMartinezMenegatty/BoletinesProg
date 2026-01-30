asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
i = 0

for asignatura in asignaturas:
    nota = int(input("Ingresa tu nota de "+asignatura + ": "))
    notas.append(nota)
for i, nota in enumerate(notas):
    print(asignaturas[i], nota)