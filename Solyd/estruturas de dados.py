minha_lista = ['Gui', 'João'] #Lista (list) Mutável
minha_tupla = ('Gui', 'João') #Tupla (tuple) Imutável
meu_dicionario = {'nome': 'Guilherme', 'Idade': 27} #Dicionario (dict)
meu_conjunto = {'Gui', 'João'} #Conjunto (set) Elementos são únicos, não se repetem

# TUPLA #
'''Quando for substituir uma tupla é necessário a substituição dela inteira.'''
minha_tupla = ('Fabricio', 'Mauro') 
'''Verificando elemento em tupla'''
if 'Fabricio' in minha_tupla:
    print("Está na tupla")
else:
    print("Não está na tupla")

# DICIONÁRIO #
'''Pode-se pesquisar o valor especificando a chave'''
print(meu_dicionario['nome'])
'''Mostrando todos os valores de um dict'''
for valor in meu_dicionario.values():
    print(valor)
'''Verificando se uma chave ou valor existe'''
if 'Guilherme' in meu_dicionario.values():
    print('TRUE')
if 'nome' in meu_dicionario.keys():
    print('TRUE')
'''Substituindo um valor de um dict'''
meu_dicionario['nome'] = 'João'
'''Adicionando um valor'''
meu_dicionario['endereco'] = 'Av. Rio Branco'

# CONJUNTO #
'''Adicionado valor'''
meu_conjunto.add('Maria')
'''Valores não podem ser repetidos'''
meu_conjunto.add('Gui')
'''Removendo valores'''
meu_conjunto.remove('Gui')