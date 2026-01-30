def suma(a,b):
    return a+b

def saudo():
    print("Ola")

def multiplica(y):
    def producto(x):
        return x * y
    return producto

doble = multiplica(2)
print(doble)
print(doble(5))

def decorador(func):
    def envoltorio():
        print("Executa antes da funcion",func.__name__)
        func()
        print("Executa despois da funcion",func.__name__)
    return envoltorio

@decorador
def saudo2():
    print("Ola")


functionDecorada = decorador(saudo)
functionDecorada()
decorador(saudo)

print (functionDecorada())

saudo2()

def decorador2(func):
    def envoltorio(*args, **kwargs):
        print("Executa antes da funcion", func.__name__)
        resultado = func(*args, **kwargs)
        print("Executa despois da funcion", func.__name__)
        return resultado
    return envoltorio

s = decorador2(suma)(3,3)
print (s)

def mult2(a,b):
    return a*b

m = mult2(3,3)
print(m)