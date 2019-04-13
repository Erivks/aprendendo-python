#Métodos Especiais

# __str__
class Conta(object):
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        return "ID: %i\nSaldo: R$: %.2f"%(self.ID, self.saldo)

#Automaticamente, quando o objeto que tem um 
#método __str__ é printado, __str__ é executado
bradesco = Conta(333, 4000)
print(bradesco)

# __add__
class Conta(object):
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        return "ID: %i\nSaldo: R$: %.2f"%(self.ID, self.saldo)
    #Aqui, outra instância está sendo usada como parâmetro
    def __add__(self, other):
        self.saldo += other.saldo #E aqui, está sendo feita 
        #uma soma do saldo da instância dada como paramêtro
        #com o saldo da instâcia atual. 
        #Ou seja, soma do saldo entre dois objetos,

bradesco = Conta(333, 4000)
itau = Conta(334, 3000)
#Somando saldo de dois objetos
bradesco + itau
print(itau.saldo)

#Essa operação pode ser feitas com
#Subtração = __sub__
#Divisão = __div__
#Multiplicação = __mult__

#__dict__
class Conta(object):
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        return "ID: %i\nSaldo: R$: %.2f"%(self.ID, self.saldo)

bradesco = Conta(45, 4565)
#Transforma o objeto em um dicionário
dicionario = bradesco.__dict__

#__doc__
class Conta(object):
    '''
    Objeto do tipo conta referente a um banco
    '''
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
    '''
    Esse método irá retornar uma String da class
    '''
        return "ID: %i\nSaldo: R$: %.2f"%(self.ID, self.saldo)

bradesco = Conta(12, 4555)
#Irá mostrar o comentário feito na class acima
bradesco.__doc__
bradesco.__str__.__doc__
#Irá mostrar a descrição de todos os métodos que estão comentados
help(bradesco)