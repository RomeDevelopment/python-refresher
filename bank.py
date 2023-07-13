class bank:
    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, w):
        if w <= self.balance:
            self.balance = self.balance - w
            return self.balance
        else:
            return "ERROR"

    def deposit(self, d):
        self.balance = self.balance + d

    def printbal(self):
        print(self.balance)
