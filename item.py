class item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Item(name={self.name}, value={self.value})"

    def description(self):
        return f"{self.name} dégats: {self.value}"

    def drop_rate(self):
        return 0.1 

    def rarity(self):
        if self.value < 10:
            return "Common"
        elif self.value < 20:
            return "Uncommon"
        elif self.value < 30:
            return "Rare"
        else:
            return "Legendary"

    def item_type(self):
        if self.value < 10:
            return "Potion"
        elif self.value < 20:
            return "Weapon"
        elif self.value < 30:
            return "Armor"
        else:
            return "Artifact"

    def dictionary(self):
        return {
            "name": self.name,
            "value": self.value,
            "description": self.description(),
            "drop_rate": self.drop_rate(),
            "rarity": self.rarity(),
            "item_type": self.item_type()
        }
