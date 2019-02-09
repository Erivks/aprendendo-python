from veiculo import Veiculo
from carro import Carro

caminhão = Veiculo('azul', 6, 'Ford', 10.0)

print('CAMINHÃO:')
print('Cor:', caminhão.cor)
print('Marca:', caminhão.marca)
print('Tanque:', caminhão.tanque)
print("")

carro = Carro('cinza', 'BMW', 11.0)

print("CARRO:")
print('Cor:', carro.cor)
print('Marca:', carro.marca)
print('Tanque:', carro.tanque)
print('Abastecendo o carro...')
carro.abastecer(30)
print('Tanque:', carro.tanque)