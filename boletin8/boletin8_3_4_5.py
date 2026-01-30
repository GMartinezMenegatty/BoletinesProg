#3
#Escribir unha función que reciba unha tupla con nomes e para cada nome 
#imprima unha mensaxe ‘Estimado don/dona Nome’

def saludo():
    nomes = ('Ana', 'Luis', 'María', 'Carlos', 'Sofía')
    for nome in nomes:
        print(f'Estimado don/dona {nome}')

saludo()


#4
#Escribir unha función que reciba unha tupla con nomes, 
#unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior 
#(exercicio 3) para os n nombres que se encontran a partires da posición p.

def saludo_posicion(nomes, p, n):
    seleccion = nomes[p : p + n]
    for nome, xenero in seleccion:
        if xenero == 'femenino':
            print(f'Estimada dona {nome}')
        elif xenero == 'masculino':
            print(f'Estimado don {nome}')
        else:
            print(f'Estimada/e {nome}')
nomes = (
    ("Ana", "femenino"),
    ("Luis", "masculino"),
    ("María", "femenino"),
    ("Carlos", "masculino"),
    ("Sofía", "femenino")
)

saludo_posicion(nomes, 1, 3)

#5
#Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, 
#deberán recibir unha tupla de tuplas, contendo o nome e o xénero, 
#adaptando a mensaxe con don ou dona dependendo deste.


def saludo_genero(nomes):
        for nome, genero in nomes:
            if genero == 'femenino':
                    print(f'Estimada dona {nome}')
            else:
                if genero == 'masculino':
                    print(f'Estimado don {nome}')
nomes = (
     ('ana', 'femenino'),
     ('luis', 'masculino'),
     ('maria', 'femenino'),
     ('carlos', 'masculino'),
     ('sofia', 'femenino')
     )
        
saludo_genero(nomes)
    



