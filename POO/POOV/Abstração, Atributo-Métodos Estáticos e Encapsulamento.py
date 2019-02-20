'''ABSTRAÇÃO'''
#criando uma classe mãe que deverá ser subclasseada por outras classes
class objetoGrafico(object):
    def __init__(self, cor):
        self.cor = cor
    #São criados dois métodos vazios, 
    #que serão preechidos pelas subclasses que herdarão essa classe
    def area(self): 
        pass
    def perimetro(self):
        pass
    def info(self):
        print('Área: {}m2\nCor: {}'.format(self.area(), self.cor))
'''Tanto o método área quanto o método perímetro, são métodos abstratos'''

'''ATRIBUTOS ESTÁTICOS'''
class Cachorro:
    nome = 'Rex'
    cor = 'Marrom'

#instanciando a classe Cachorro
Dog = Cachorro()

#Acessando atributos
Dog.nome
Dog.cor
#O nome e a cor, não são atributos do objeto Dog mas da Class Cachorro
Cachorro.nome
Cachorro.cor
'''Isso é chamado de atributos estáticos pois a partir 
de qual instancia é possivel acessar atributos da class'''
#Exemplo de uso
class Conta(object):
    #São criados os métodos estáticos
    total = 10000
    reserva = 0.1
    #Método construtor
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor

itau = Conta(123, 5000)
itau.deposito(1000)
itau.saque(5000)
print(itau.saldo)

class Conta_(object):
    #São criados os métodos estáticos
    total = 10000
    reserva = 0.1
    #Método construtor
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        Conta_.total += valor
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            Conta_.total -= valor

itau = Conta_(123, 5000)
itau.deposito(1000)
itau.saque(5000)
print(itau.saldo)
Conta.total
'''Isso seria útil no caso de várias contas, pois todas teriam 
acesso ao Total e a Reserva do banco por serem atributos estáticos'''
#Passando a instancia 'itau' e depositando um valor nela
Conta.deposito(itau, 4000)
print(itau.saldo)

class _Conta_(object):
    #São criados os métodos estáticos
    total = 10000
    reserva = 0.1
    #Método construtor
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        _Conta_.total += valor
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            _Conta_.total -= valor
    #Criando o método sem passar a instancia como parametro
    @staticmethod
    def imprimereserva():
        print(_Conta_.total * _Conta_.reserva)

itau = _Conta_(123, 4000)
#Ocasionará em um erro, pois o método foi criado 
#sem passar a instancia como parametro
itau.imprimereserva()
#Só quem tem acesso é a própria classe
_Conta_.imprimereserva()

'''ENCAPSULAMENTO'''
class banco(object):
    #São criados os métodos estáticos
    '''Transformando atributos como 'privados' e um atributo privado, 
    só pode ser acessado dentro de uma instancia ou classe e 
    para transformar um atributo privado basta adicionar dois 
    underlines antes de seu nome'''
    __total = 10000
    reserva = 0.1
    #Método construtor
    def __init__(self, id, saldo):
        self.__id = id
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        banco.__total += valor
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            banco.__total -= valor
    #Criando o método sem passar a instancia como parametro
    @staticmethod
    def imprimereserva():
        print(banco.__total * _Conta_.reserva)

itau = banco(123, 5000)
#Tetando acessar os atributos privados
banco.__total #Erro
itau.__id #Erro
#Sacando valor
itau.saque(1000)
#Acessando a reserva que é de 900 após saque de 1000
banco.imprimereserva() #Funciona, pois os atributos privados 
#só podem ser acessados de dentro da classe ou de uma instancia (por métodos)

class banco_(object):
    #São criados os métodos estáticos
    '''Transformando atributos como 'privados' e um atributo privado, 
    só pode ser acessado dentro de uma instancia ou classe e 
    para transformar um atributo privado basta adicionar dois 
    underlines antes de seu nome'''
    __total = 10000
    reserva = 0.1
    #Método construtor
    def __init__(self, id, saldo):
        self.__id = id
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        banco_.__total += valor
    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            banco_.__total -= valor
        #Mostrando a reserva toda vez em que um saque é feito
        banco_.__imprimereserva()
    #Criando o método sem passar a instancia como parametro
    '''Também é possivel tornar métodos privados'''
    @staticmethod
    def __imprimereserva():
        print(banco_.__total * _Conta_.reserva)

banco_.__imprimereserva() #Erro
itau = banco_(123, 5000)
itau.saque(1000) #Funciona, pois o método privado está sendo 
#acessado por outro método chamado pela instancia

