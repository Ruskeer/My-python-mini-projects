class CreditCard:
    def pay(self, amount):
        return f"${amount} paid using CreditCard."

class Paypal:
    def pay(self, amount):
        return f"${amount} paid using Paypal."

class Gcash:
    def pay(self, amount):
        return f"${amount} paid using Gcash."


def payment(process, amount):
    print(process.pay(amount))


payment(Gcash(), 1000)
