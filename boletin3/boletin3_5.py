#Dados 3 números que se supoñen distintos, indicar cal é o maior.

def numeroMayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(numeroMayor(3, 7, 8))

    
