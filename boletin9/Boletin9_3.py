class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return self.velocidade

    def acelerar(self, valor):
        self.velocidade += valor

    def frenar(self, menos):
        self.velocidade -= menos
        if self.velocidade < 0:
            self.velocidade = 0



