from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Erick', 20, '197.125.667-65')
conta = Conta(cliente1, 400.60)
conta.depositar(1000.40)
conta.sacar(200.50)

print(conta)