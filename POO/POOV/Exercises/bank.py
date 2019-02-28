import shelve
data = shelve.open('data_bank')
'''SUPERCLASS'''
class Bank(object):
    __total_amount = 1000000
    booking_fee = 0.1
    __required_reserve = 10000
    def __calculateReserve(self):
        return self.__total_amount * self.booking_fee
    def __canLoan(self, value):
        reserve = self.__calculateReserve()
        if (reserve - value) > self.__required_reserve:
            return True
        else:
            return False
    def loan(self, value):
        if self.__canLoan(value):
            self.__total_amount -= value
            return value
        else:
            return None
    def setTotalAmount(self, value, tp):
        if tp == 1:
            self.__total_amount -= value
        elif tp == 2:
            self.__total_amount += value

'''SUBCLASS'''
class Account(Bank):
    def __init__(self, ID, name, password):
        self.__balance = 50.0
        self.__id = ID
        self.name = name
        self.__password = password
        self.bank = Bank()
    def correctPassword(self, password):
        if password == self.__password:
            return True
        else:
            return False
    def deposit(self, password, value):
        correct = False
        while correct != True:
            if self.correctPassword(password):
                print('The password is correct.')
                self.__balance += value
                self.setTotalAmount(value, 2)
                print('Deposit made succefull.')
                print('Balance value: {}'.format(self.__balance))
                print('')
                correct = True
            else:
                print('Password is incorrect.')
                password = input('Report the password again: ')
                correct = False
    def withdrawal(self, password, value):
        correct = False
        while correct != True:
            if self.correctPassword(password):
                if self.__balance > value:
                    print('The password is correct.')
                    self.__balance -= value
                    self.setTotalAmount(value, 1)
                    print('Withdrawal made succefull.')
                    print('Balance value: {}'.format(self.__balance))
                    print('')
                    correct = True
                    break
                else:
                    print('Sorry, insufficient balance.')
                    break
            else:
                print('Password is incorrect.')
                password = input('Report the password again: ')
                correct = False
    def canRecieveLoan(self):
        if self.__balance > 0.0:
            return True
        else:
            return False
    def getBalance(self):
        print('Your balance is {}'.format(self.__balance))
        print('')
    def getID(self):
        return self.__id
    def setTotalAmount(self, value, tp):
        super().setTotalAmount(value, tp)
    def loan(self, value):
        if self.canRecieveLoan():
            if super().loan(value) != None:
                self.__balance += value
                print('You recieve loan of: {}'.format(value))
                self.getBalance()
        else:
            print("You can't recieve loan.")

def askPassword():
    password = input('What is your password? ')
    return password
    
def back():
    awr = input('Do you want back to main? (y/n)')
    if awr == 'y':
        main()
    else:
        pass

def askValue(op):
    if op == 'deposit':
        value = input('What is the value of {}? '.format(op))
    elif op == 'withdrawal':
        value = input('What is the value of {}? '.format(op))
    elif op == 'loan':
        value = input('What is the value of {}? '.format(op))
    value = float(value)
    return value

def existsID():
    check = False
    while check != True:
        ID = input('Report the ID: ')
        if ID in data:
            check = True
            return ID
        else:
            print('This ID not exists, try another one.')
            check = False

def notExistsID():
    check = False
    while check != True:
        ID = input('Report your ID: ')
        if ID in data:
            print('This ID already exists, try another one.')
            check = False
        else:
            check = True
            return ID

def createID():
    ID = notExistsID()
    return ID

def accountCreate():
    name = input('Report your name: ')
    ID = createID()
    password = input("Report your password: ")
    print('')
    account = Account(ID, name, password)
    data[ID] = account
    back()

def accountBalance():
    ID = existsID()
    account = data[ID]
    account.getBalance()
    back()

def accountDeposit():
    op = 'deposit'
    ID = existsID()
    account = data[ID]
    value = askValue(op)
    password = askPassword()
    account.deposit(password, value)
    back()

def accountWithdrawal():
    op = 'withdrawal'
    ID = existsID()
    account = data[ID]
    value = askValue(op)
    password = askPassword()
    account.withdrawal(password, value)
    back()

def accountLoan():
    op = 'loan'
    ID = existsID()
    account = data[ID]
    value = askValue(op)
    account.loan(value)
    back()

def numberEmpty():
    awr = input('Please, report a valid operation: ')
    checkAnswer(awr)

def checkAnswer(awr):
    if awr == '1':
        accountCreate()
    elif awr == '2':
        accountBalance()
    elif awr == '3':
        accountDeposit()
    elif awr == '4':
        accountWithdrawal()
    elif awr == '5':
        accountLoan()
    elif awr == '0':
        accountExit()
    else:
        numberEmpty()

def main():
    print("=== BANK ===\n")
    answer = input("[ 1 ] Create account\n[ 2 ] Check balance\n[ 3 ] Deposit\n[ 4 ] Withdrawal\n[ 5 ] Loan\n[ 0 ] Exit.\n\nAwnser: ")
    checkAnswer(answer)

main()
