class BankAccount:
    def __init__(self, accholder, balance=0.0):
        self.acc = accholder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return self.balance

        self.balance -= amount



class Savings(BankAccount):
    def __init__(self, accholder, balance=0.0, interest=0.05):
        super().__init__(accholder, balance)

        self.interest = interest


    def add_interest(self):
        interest = self.balance * self.interest

        return self.deposit(interest)


tomy = Savings('tomy', 1000, interest=0.05)

print(tomy.add_interest())

print(tomy.__dict__)
