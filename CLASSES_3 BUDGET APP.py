class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount' : amount,
            'description' : description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        total_money = 0
        for i in self.ledger:
            total_money += i['amount']
        return total_money
    
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items_str = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items_str += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items_str + total
    

def create_spend_chart(categories):
    # 1. Calculate withdrawal totals for each category and the grand total
    spent_per_category = []
    for cat in categories:
        cat_spent = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                cat_spent += abs(item['amount'])
        spent_per_category.append(cat_spent)
        
    total_spent = sum(spent_per_category)
    
    # Avoid division by zero if nothing was spent
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        # Calculate percentages rounded down to the nearest 10
        percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in spent_per_category]

    # 2. Build the top half of the chart (Y-axis and 'o' bars)
    chart = "Percentage spent by category\n"
    for r in range(100, -1, -10):
        chart += f"{r:>3}| "
        for p in percentages:
            if p >= r:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    # 3. Add the horizontal separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # 4. Build the bottom half of the chart (Vertical names)
    max_len = max([len(cat.name) for cat in categories])
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart
