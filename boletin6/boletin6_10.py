a = [
    (1, 2, 3),
    (4, 5, 6)
]

b = [
    (-1, 0),
    (0, 1),
    (1, 1)
]

filas_a = len(a)
columnas_a = len(a[0])
filas_b = len(b)
columnas_b = len(b[0])

if columnas_a != filas_b:
    print("No se pueden multiplicar as matrices: dimensións incompatibles.")
else:
    resultado = []
    for i in range(filas_a):
        nueva_fila = []
        for j in range(columnas_b):  
            suma = 0
            for k in range(columnas_a):  
                suma += a[i][k] * b[k][j]
            nueva_fila.append(suma)
        resultado.append(tuple(nueva_fila))  

    print("Produto de a x b:")
    for fila in resultado:
        print(fila)
