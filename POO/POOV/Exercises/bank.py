'''SUPERCLASS'''
class Bank(object):
    __total_amount = 1000000
    booking_fee = .1
    __required_reserve = 10000
    def __calculateReserve(self):
        return Bank.__total_amount * Bank.booking_fee
    def canLoan(self, value):
        reserve = self.__calculateReserve()
        if reserve - value > Bank.__required_reserve:
            return True
        else:
            return False
    
'''SUBCLASS'''
class Account(Bank):
    def __init__(self, id, password):
        self.__balance = 50
        self.__id = id
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
                print('Deposit made succefull')
                correct = True
            else:
                print('Password is incorrect.')
                password = input('Report the password again: ')
                correct = False
