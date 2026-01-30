class Conta:
    def __init__(self, nome, numero, interese, saldo):
        self._nome = nome
        self._numero = numero
        self._interese = interese
        self._saldo = saldo

    def getNome(self): 
        return self._nome
    
    def getNumero(self): 
        return self._numero
    
    def getInterese(self): 
        return self._interese
    
    def getSaldo(self): 
        return self._saldo

    def setNome(self, nome): 
        self._nome = nome
        
    def setNumero(self, numero): 
        self._numero = numero

    def setInterese(self, interese): 
        self._interese = interese

    def setSaldo(self, saldo): 
        self._saldo = saldo

    def ingreso(self, cantidade):
        if cantidade > 0:
            self._saldo += cantidade

    def reintegro(self, cantidade):
        if 0 < cantidade <= self._saldo:
            self._saldo -= cantidade

    def transferencia(self, contaDestino, importe):
        if 0 < importe <= self._saldo:
            self._saldo -= importe
            contaDestino._saldo += importe
