class Meu_Objeto(object):
    #Método construtor
    def __init__(self): #'self' é referência ao objeto criado e sempre que quisermos que uma instancia 
        #da classe (objeto) chame um método, é preciso passar 'self' como parametro
        self.nome = 'Erick'
        self.idade = '45'
        print('Construtor chamado.')
    #Método
    def imprime(self):
        print('Meu nome é {} e eu tenho {}'.format(self.nome, self.idade))

#Quando se cria um objeto, automáticamento o método construtor (__init__)
# é iniciado
Erick = Meu_Objeto()
#Para usar um método de um obejto instânciado, basta digitar o nome 
# do objeto e após um ponto (.) digitar o nome do método
Erick.imprime()

class Meu_Objeto_dois(object):
    #Método construtor
    def __init__(self, nome, idade): #Os parâmetros de um método não se limitam apenas ao 'self' podendo ser 
        #passados mais de um parâmetro ao instanciar um objeto
        self.nome = nome
        self.idade = idade
        print('Construtor chamado.')
    #Método
    def imprime(self, x):
        print('Meu nome é {} e eu tenho {}'.format(self.nome, self.idade))
        print(x)

#Criando outro objeto usando parâmetros
Anderson = Meu_Objeto_dois('Anderson', 23)
#Imprimindo o objeto
Anderson.imprime(3)