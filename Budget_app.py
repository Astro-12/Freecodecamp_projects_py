class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Header line with category name centered in 30 '*' characters
        title = f"{self.name:*^30}\n"
        
        # Ledger entries formatted to fit 30 total columns (23 description, 7 amount)
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:.2f}"[:7]
            items += f"{desc}{amt:>7}\n"
            
        # Total line
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total


def create_spend_chart(categories):
    # 1. Calculate total withdrawals per category
    spent_per_category = []
    for cat in categories:
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent_per_category.append(spent)

    total_spent = sum(spent_per_category)

    # 2. Calculate percentages rounded down to the nearest 10
    percentages = []
    for spent in spent_per_category:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 100) // 10 * 10)

    # 3. Chart Header
    chart = "Percentage spent by category\n"

    # 4. Y-axis lines (100 down to 0)
    for p in range(100, -1, -10):
        chart += f"{p:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= p else "   "
        chart += "\n"

    # 5. Horizontal divider line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 6. Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i != max_len - 1:
            chart += "\n"

    return chart


# Example Usage & Testing
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for the month")
    
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55, "t-shirt")
    
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "car wash")

    print(food)
    print("\n")
    print(create_spend_chart([food, clothing, auto]))
