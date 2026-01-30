
def verificarFormatoData(data):
    verificacion = False
    data = data.strip()
    if len(data)== 10:
        if data[2] == '/' and data[5] == '/':
            dataSeparada = data.split('/')
            if len(dataSeparada[0]) == 2 and len(dataSeparada[1]) == 2 and len(dataSeparada[2]) == 4:
                if dataSeparada[0].isdecimal() and dataSeparada[1].isdecimal() and dataSeparada[2].isdecimal():
                    verificacion = True
    return verificacion

#print(verificarFormatoData("02/07/2007"))

def verificarDiaMes(data):
    verficacion = False
    diasMes = { 1 : 31,
                2 : 28,
                3 : 31,
                4 : 30,
                5 : 31,
                6 : 30,
                7 : 31,
                8 : 31,
                9 : 30,
                10 : 31,
                11 : 30,
                12 : 31,}
    d = int(data[:2])
    m = int(data[3:5])
    a = int(data[6:])
    if m > 1 and m < 13:
       if m == 2 :
            if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                diasMes[2] = 29
            if d <= diasMes[m] and d > 0:
                 verificacion = True

    return verificacion
