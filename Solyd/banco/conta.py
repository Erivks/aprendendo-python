class Conta():
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print('Erro no deposito.')
        else:
            self.saldo += valor
    def sacar(self, valor):
        if self.saldo + valor < 0:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            
    def __str__(self):
        return 'Cliente: ' + str(self.cliente.nome) + '\nSaldo: ' + str(self.saldo)