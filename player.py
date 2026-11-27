class player:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.score = 0
        self.character = []
        self.items = []

    def __repr__(self):
        return f"Player(name={self.name}, health={self.health}, strength={self.strength}, score={self.score})"

    def create_team(self, characters):
        self.character = characters

    def pick_character(self, character):
        if character not in self.character:
            self.character.append(character)

    def is_team_alive(self):
        return any(char.is_alive() for char in self.character)

    def check_inventory(self):
        return self.items

    def use_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"{self.name} used {item.name}."
        else:
            return f"{item.name} is not in inventory."
