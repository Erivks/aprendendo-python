'''SUPERCLASS'''
class Bank(object):
    __total_amount = 1000000
    booking_fee = 0.1
    __required_reserve = 10000
    def __calculateReserve(self):
        return Bank.__total_amount * Bank.booking_fee
    def __canLoan(self, value):
        reserve = self.__calculateReserve()
        if (reserve - value) > Bank.__required_reserve:
            return True
        else:
            return False
    def loan(self, value):
        if self.__canLoan(value):
            Bank.__total_amount -= value
            return value
        else:
            return None
'''SUBCLASS'''
class Account(Bank):
    def __init__(self, ID, password):
        self.__balance = 50.0
        self.__id = ID
        self.__password = password
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
                Bank.__total_amount += value
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
                print('The password is correct.')
                if self.__balance > value:
                    self.__balance -= value
                    Bank.__total_amount -= value
                    print('Withdrawal made succefull.')
                    print('Balance value: {}'.format(self.__balance))
                    print('')
                    correct = True
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
    def returnWithdrawal(self):
        ('Your balance is {}'.format(self.__balance))
        print('')
    def loan(self, value):
        if self.canRecieveLoan():
            if super().loan(value) != None:
                self.__balance += value
                print('You recieve loan of: {}'.format(value))
                self.returnWithdrawal()
        else:
            print("You can't recieve loan.")

def createAccount():
    ID = input('Report your name: ')
    password = input("Report your password: ")
    print('')
    account = Account(ID, password)
    return account


