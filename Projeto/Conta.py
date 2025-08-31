class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self.numero = numero
        self._saldo = 0.0


    @property # Transforma um método em um atributo somente leitura.
    def saldo(self):    
        return self._saldo


    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = saldo
# Getter: usado para obter um valor de forma encapsulada.
# Setter: usado para alterar o valor, aplicando regras/validações.

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")

    
    def depositar(self, valor):
        self.saldo += valor


    def extrato(self):
        print("Cliente:", self._titular,"\nSaldo atual:", self._saldo)

