def almacenarTemperaturas():
    temperaturas = []
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    for dia in dias:
        temperatura = float(input("Ingrese la temperatura del dia "+ dia + ": "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_media_temperaturas(temperaturas):
    totalTemperatura = 0
    for temperatura in temperaturas:
        totalTemperatura += temperatura
    return totalTemperatura/len(temperaturas)

def dias_superan_media_temperatura (temperaturas):
    dias = 0
    mediaTemperatura = calcular_media_temperaturas (temperaturas)
    for temperatura in temperaturas:
        if temperatura > mediaTemperatura:
            dias += 1
    return dias

def mostra_Dias_Superan_Temperatura(temperaturas, temperaturaLimite):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    for i, temperatura in enumerate(temperaturas):
        if temperatura > temperaturaLimite:
            print ("O dia "+ dias[i] + " superou o valor " + str(temperaturaLimite) + " en " + str(temperatura)+" graos ")

temperaturas = almacenarTemperaturas()
media = calcular_media_temperaturas(temperaturas)
print ("A media de la temperatura es: " + str(media))
numeroDias = dias_superan_media_temperatura(temperaturas)
print (str(numeroDias)+ " Dias superan a media de temperaturas")
print ("Dias que la temperatura supera la media: ")
mostra_Dias_Superan_Temperatura(temperaturas, media)

