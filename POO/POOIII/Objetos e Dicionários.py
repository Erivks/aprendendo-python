#COMPARAÇÃO ENTRE OBJETOS E DICIONÁRIOS E 
# MÉTODO ESPECIAL PARA DICIONÁRIOS

'''DICIONÁRIO'''
#Criando dict
pessoa = {'Nome': 'Lucas', 'Emprego': 'Advogado', 'Idade': 20, 'Cor de cabelo': 'Pedro'}
#Mudando um valor dentro do dict
pessoa['Nome'] = 'Erick'
#Acessando valor
print(pessoa['Emprego'])
#Criando novas chaves
pessoa['Peso'] = 87.0

#Olhando um dict e comparando com uma class, 
# não são muito diferentes e para comparação faremos uma classe Pessoa
class Pessoa(object):
    pass #criando uma classe vazia com statement pass

#Criando objeto
Lucas = Pessoa()

#Criando atributos para o objeto
Lucas.nome = 'Lucas'
Lucas.idade = 27
Lucas.emprego = 'Advogado'
'''Em python, os objetos criados são 
adicionados internamente dentro de um dicionario'''
dicionario = Lucas.__dict__ #Método especial que retorna o objeto como um dicionário
print(dicionario)

'''Objetos são mais vantajosos:
Pela facilidade de se trabalhar com eles;
Por ser mais fácil criar vários objetos, cada um com seus métodos;
Em objetos, existem as Heranças, Polimofismo e Encapsulamento.
Em objetos, sabemos exatamente os paramêtros que devem ser passados'''

#Um dos motivos pelo qual Python é uma linguagem mais lenta, 
# é pelo fato de que os objetos são armazenados em dict's 

#Assim como pode-se usar o método __dict__ em objetos, 
# também é possível usá-lo em classes para saber seus métodos
print(Pessoa.__dict__)