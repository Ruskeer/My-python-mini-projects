class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, desc=""):
        self.ledger.append({'amount': amount, 'description': desc})

    def check_bal(self):
        total = 0
        for amount in self.ledger:
            total += amount['amount']
        return total

    def check_funds(self, amount):
        return amount <= self.check_bal()

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        return False

    def transfer(self, amount, destination):
        if self.withdraw(amount, f"Transfer to {destination.name}"):
            destination.deposit(amount, f'From: {self.name}')
            return True
        return False

    def __str__(self):

        total = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            desc = f"{item['description'][:26]:<26}"
            amt = f"{item['amount']:>7.2f}"
            total += f"{desc}{amt}\n"

        total += f"Total: {self.check_bal():.2f}"

        return total
            

def create_spend_chart(categories):
    spent_per_cat = []

    for cat in categories:
        cat_spent = 0
        for c in cat.ledger:
            if c['amount'] < 0:
                cat_spent += c['amount']
        spent_per_cat.append(cat_spent)
    total_spent = sum(spent_per_cat)

    percentage = [int((spent / total_spent) * 100 // 10) * 10 for spent in spent_per_cat]



    chart = "Percentages of each spent\n"
    for r in range(100, -1, -10):
        chart += f"{r:>3}| "
        for p in percentage:
            if p >= r:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "-" * (len(percentage) * 3 + 1)

    return chart
            
    

def draw_blueprint_row(label, value, max_width):
    text_length = len(label) + len(str(value)) + 2

    spaces_needed = max_width - text_length

    spaces = " " * spaces_needed

    print("| " + f"{label}: {value}" + spaces + " |")

def draw_blueprint_box(dict, max_width):
    print("+" + "-" * (max_width + 2) + "+")
    

    for label, value in dict.items():
        draw_blueprint_row(label, value, max_width)

    print("+" + "-" * (max_width + 2) + "+")

    

budget_data = {
    "Food": 250,
    "Rent": 1200,
    "Entertainment": 75
}

draw_blueprint_box(budget_data, 22)






clothing = Category("Clothing")
food = Category("Food")
food.deposit(1000, "initial")

food.transfer(500, clothing)
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant meal with friends")

print(food)
print("\nPercentages:", create_spend_chart([food, clothing]))




















