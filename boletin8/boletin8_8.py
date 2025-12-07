#Escribir unha función que reciba unha lista de tuplas 
#(Apelido, Nome, Inicial_segundo_nome) e devolte unha 
#lista de cadenas onde cada unha conteña 
#primero o nome, logo a inicial cun punto, 
#e logo o apelido.

personas = [('Perez', 'Ana', 'M'), ('Sainz', 'Carlos', 'A')]

def InfPersonas (personas):
    persona = []
    for apelido, nome, inicial_segundo_nome in personas:
        cadea = f'{nome} {inicial_segundo_nome}. {apelido}'
        persona.append(cadea)
    
    return persona

lista = InfPersonas(personas)

for p in lista:
    print (p)




