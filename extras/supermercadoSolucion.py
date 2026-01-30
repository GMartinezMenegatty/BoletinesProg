efectivo=[['2', [100,1], [50,12], [20,5]],
           ['1', [50,21], [20,11], [10,7], [0.2,9]],
          ['3', [50,2], [20,9], [0.20,3], [0.5,23]]]

def mostrarContidoUnhaCaixa (caixa, totalEfectivoCaixa):


    for contidoCaixa in totalEfectivoCaixa:
        if contidoCaixa[0] == caixa:
            print('O contido da', caixa, "é:")
            for i in range(1, len(contidoCaixa)):
                if contidoCaixa[i][0] > 2.0:
                    print (contidoCaixa[i][1], "billetes de ", contidoCaixa[i][0], "euros")
                else:
                    print(contidoCaixa[i][1], "moedas de ", contidoCaixa[i][0], "euros")
            break

mostrarContidoUnhaCaixa('1', efectivo)