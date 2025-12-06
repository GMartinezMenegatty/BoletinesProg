# Coñecidos, o nome e o peso de dúas persoas, 
#o programa escribirá por consola os datos da persoa
#que pesa máis e a diferenza de peso entre elas.

personas = (('Ana', 70), ('Luis', 80))

def DiferenciaPersonas(personas):
    (nome1, peso1), (nome2, peso2) = personas
    peso1 = (peso1)
    peso2 = (peso2)
    if peso1 > peso2:
        print(f'A persoa que pesa máis é {nome1} con {peso1} kg.')
        print(f'A diferenza de peso é: {peso1 - peso2} kg.')
    elif peso2 > peso1:
        print(f'A persoa que pesa máis é {nome2} con {peso2} kg.')
        print(f'A diferenza de peso é: {peso2 - peso1} kg.')
    else:
        print('Ambas persoas pesan o mesmo.')

DiferenciaPersonas(personas)

    