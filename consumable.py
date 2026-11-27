class consumable:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(f"Used one {self.name}. Remaining: {self.quantity}")
        else:
            print(f"No more {self.name} left to use.")

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {amount} {self.name}. Total: {self.quantity}")