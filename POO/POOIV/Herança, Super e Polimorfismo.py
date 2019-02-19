#Herança e Polimorfismo
class Mamifero(object):
    def __init__(self, cor_de_pelo, genero, num_de_patas):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.num_de_patas = num_de_patas    
    def falar(self):
        print('Olá, sou um mamífero e sei falar.')
    def andar(self):
        print('Estou andando sobre {}.'.format(self.num_de_patas))
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam.')
            return
        else:
            print('Amamentando meu filhote.')

#Criando um objeto da classe mamífero e usando seus métodos
#Um cachorro
Rex = Mamifero('Marrom', 'Masculino', 4)
Rex.falar()
Rex.amamentar()
Rex.andar()
#Um humano
Julia = Mamifero('Preto', 'Feminino', 2)
Julia.andar()
Julia.amamentar()
Julia.falar()

'''Quando queremos que determinadas subclasses (Pessoa ou Cachorro) 
herdem determinadas características de uma Superclasse, 
estaremos falando de Herança.'''

#Para dizermos que uma classe (Pessoa) é filha de outra (Mamifero) 
# e assim aproveitar suas caracteristicas, devemos fazer o seguinte:

class Pessoa(Mamifero): #Assim a classe 'Pessoa' é uma subclasse da Mamifero
    #Isso permitirá acessar atributos e métodos da classe Mamifero
    pass #Definindo a classe como vazia

#Criando um objeto da classe Pessoa, 
# que herdou atributos e métodos da Classe Mamifero
Julia = Pessoa('Preto', 'Feminino', 2)
#Podemos usar todos os métodos
Julia.andar()
Julia.falar()
Julia.amamentar()

#Podemos fazer mais, definir um método 
# construtor próprio para a classe Pessoa
class _Pessoa(Mamifero):
    #Quando escrevemos um método em uma subclasse com o mesmo 
    #nome de um método na superclasse, estamos reescrevendo esse método.
    def __init__(self):
        self.cabelo = 'Loiro'

#A classe pessoa deixou os outros parametros 
#pois foi sobreposto pelo novo atributo criado
Julia = _Pessoa()
#Ainda podemos usar os métodos mas não irá funcionar pois 'amamentar' precisa 
#do atributo genero que deixou de existir
Julia.amamentar()
'''Isso se chama Polimorfismo, pois o método construtor 
da Julia, sobrepos o método construtor do Mamifero, 
criando dois métodos diferentes'''

class Pessoa_(Mamifero):
    #Pegando o método construtor da Superclasse(Mamifero) 
    #para o método contrutor da Subclasse(Pessoa)
    def __init__(self, cor_de_pelo, genero, num_de_patas, cabelo):
        '''Inicia-se a função 'super()' passando como parametros
        O nome da classe onde super está sendo chamado 'Pessoa';
        A instancia de objeto 'self';
        Após um ponto (.), o método que queremos chamar (__init__);
        E os argumentos necessários para esse métedo 'cor_de_pelo, genero, num_de_patas'.'''
        super(Pessoa_, self).__init__(cor_de_pelo, genero, num_de_patas)
        #Essa seria a forma completa, 
        #mas pode-se declarar apenas a função 'super()'
        self.cabelo = cabelo

Julia = Pessoa_('Preto', 'Feminino', 2, 'Loiro')

class Pessoa__(Mamifero):
    #Pegando o método construtor da Superclasse(Mamifero) 
    #para o método contrutor da Subclasse(Pessoa)
    def __init__(self, cor_de_pelo, genero, num_de_patas, cabelo):
        '''A forma anterior seria a forma completa mas tendo o mesmo
        resultado pode-se declarar apenas a função 'super()' '''
        super()
        self.cabelo = cabelo

Julia = Pessoa__('Preto', 'Feminino', 2, 'Loiro')

'''Pode-se usar super() em qualquer outro método, 
não se limitando ao contrutor'''
class Pessoa___(Mamifero):
    def __init__(self, cor_de_pelo, genero, num_de_patas, cabelo):
        super()
        self.cabelo = cabelo
    def falar(self):
        super().falar()
        print('Sou uma pessoa e sei falar')

Julia = Pessoa___('Preto', 'Feminino', 2, 'Loiro')
Julia.falar()