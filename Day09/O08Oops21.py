
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass

    def withdraw(self):
        pass

class Savings(Account):
    def deposit(self):
        print('Credited......')

    def getBalance(self):
        print("the balance in the account is ######.##")


class Current(Account):
    def transfer(self):
        print("trasferred......")

    def getBalance(self):
        print("The balance in the account is ##########.##")

sav = Savings()
sav.getBalance()

cur = Current()
cur.transfer()
