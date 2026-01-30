producto = str(input("introduzca el nombre del producto: "))
ventas = int(input("introduzca las ventas: "))

if ventas <= 100:
    print("bajo")
elif ventas > 100 and ventas <= 500:
    print("medio")
elif ventas > 500 and ventas <= 1000:
    print("alto")
else:
    print("primera necesidad")