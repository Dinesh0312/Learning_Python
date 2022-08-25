#6) Create a class for creating bank account, define functions for credit and debit printing the current balance in the account for
#three transactions of withdrawl and deposit.


class Bank_Account:

    def __init__(self):
        self.balance = 0
        print("Hello! Welcome to the PNB bank")

    def credit(self):
        amount = int(input("\nEnter amount to be deposit : "))
        self.balance += amount
        print("Amount Deposit",amount)

    def debit(self):
        amount = int(input("\nEnter the amount to be withdraw : "))
        if self.balance >= amount:
            self.balance -= amount
            print("Withdraw amount",amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAvailable Balance", self.balance)


cos1 = Bank_Account()
cos2 = Bank_Account()
cos3 = Bank_Account()



cos1.credit()
cos1.debit()
cos1.display()

cos2.credit()
cos2.debit()
cos2.display()

cos3.credit()
cos3.debit()
cos3.display()