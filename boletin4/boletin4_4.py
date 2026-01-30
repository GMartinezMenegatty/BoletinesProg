num = int(input("digite um numero: "))

valores = {
    0: "",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciseis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
}

valoresDec = {
    2: "veinti",
    3: "treinta",
    4: "cuarenta",
    5: "cincuenta",
    6: "sesenta",
    7: "setenta",
    8: "ochenta",
    9: "noventa",
}

snum = str(num)
num1 = int(snum[0])
num2 = int(snum[1])
num1 = valoresDec[num1]
num2 = valores[num2]


if num < 1 or num > 99:
    print("numero invalido")
elif num >= 1 and num <= 99:
    if num < 21:
        print(valores[num])
    elif num >= 20 and num < 30:
        print(num1 + num2)
    else:
        num = str(num)
        num1 = int(num[0])
        num2 = int(num[1])
        num1 = valoresDec[num1]
        num2 = valores[num2]
        if num2 == "":
            print(num1)
        else:
            print(num1, "y", num2)

