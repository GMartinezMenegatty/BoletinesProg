#Crea a aplicación que permita gardar e recuperar os datos dos clientes dunha empresa.
#Para o cal, defina a clase Cliente, que teña os atributos:

#id, identificador de cliente
#nome
#teléfono

#Os obxectos Cliente se recollerán nunha lista.
#A aplicación terá un menú que posibilitará as seguintes opcións:

#Engadir novo cliente
#Modificar datos
#Dar de baixa clientes.
#Listar os clientes.

#A información se gardará nun ficheiro binario,
#que cargará en memoria o iniciar o programa e se gardará en disco, actualizado  o rematar.

class Cliente:
    def __init__(self, id, nome, telefono):
        self.id = id
        self.nome = nome
        self.telefono = telefono

    def lista_cliente(self,cliente):
        cliente = []

