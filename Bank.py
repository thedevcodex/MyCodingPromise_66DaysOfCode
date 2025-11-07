#Write a class Bank that has a method deposit() and withdraw() to update the balance.
class Bank():
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        print("Deposited:",amount)
        print("Balance:",self.balance)
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("insufficient balance")
        print("withdrawn:",amount)
        print("Balance:",self.balance)
    def check_balance(self):
        print("Final Balance:",self.balance)
b1=Bank()
b1.deposit(500)
b1.withdraw(100)
b1.check_balance()
        
