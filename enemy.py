class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.dropables = []  # List of items that can be dropped by the enemy
        self.is_alive = True  # Indicates if the enemy is alive
        #+List~Item~ dropables
    def drop_loot(self):
        return self.dropables
        #+DropLoot() List~Item~
    def drop_loot(self):
        return self.dropables    
        #+PlayTurn() «override»
    def play_turn(self):
        character = self.choose_character()
        if character:
            damage = self.strength - character.defense()
            character.take_damage(damage)
            return f"{self.name} attacks {character.name} for {damage} damage."