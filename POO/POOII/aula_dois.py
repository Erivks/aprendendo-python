#ATRIBUTOS, ASSOCIAÇÕES e FUNÇÕES
class Minha(object):
    def __init__(self):
        self.x = 0 #Atributos definidos
        self.y = 0

'''ATRIBUTOS'''
#Instânciando classe
meu = Minha()

#Acessando o valor de atributos de um objeto
#Para acessar o valor de um objeto basta especificar o objeto,
#adicionar um ponto (.) e depois, o nome do atributo.
print(meu.x)

#É possível também modificar atributos da seguinte forma
meu.x = 5
print(meu.x)

#Pode - se criar novos atributos
meu.z = 1
print(meu.z)

'''ASSOCIAÇÕES'''
#Associação é quando se tem uma interação direta de uma classe com outra
class PessoaAmaAnimal(object):
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro(object):
    def __init__(self, nome, cor_de_pelo):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
    def daApatinha(self):
        print('{} extendeu a partinha.'.format(self.nome))
    def latir(self):
        print('au au au au!')

#Criando o objeto cachorro como 'rex'
rex = Cachorro('Rex', 'Marrom')
#Passando 'rex' como atributo para o objeto 'Erick'
#Isso é uma associação
Erick = PessoaAmaAnimal('Erick', 62.0, rex)
#Pode-se acessar atributos do objeto 'Cachorro' apartir 
#do atributo 'cao' no obejto 'PessoaAmaAnimal'
print(Erick.cao.cor_de_pelo)
#Chamando método 'treinar' do objeto pessoa, que chama os métodos
#do objeto cachorro
print(Erick.treinar())

#Todo objeto que é passada para um função é há mudança em algum atributo
#o atributo também mudará fora da função
def MudaNome(pessoa):
    pessoa.nome = 'Carlos'

MudaNome(Erick)
    