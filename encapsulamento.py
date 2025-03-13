class Conta:
    def __init__(self, saldo = 0):
        self._saldo = saldo

    def depositar(self, valor):
        pass
    
    def sacar(self, valor):
        pass

    def mostrar_saldo(self):
       return self._saldo


conta = Conta(100)
# Atraves de um método da classe Conta, o saldo é acessado
print(conta.mostrar_saldo())

