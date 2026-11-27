class wave:
    def __init__(self, vague, enemies):
        self.vague = int(vague)
        self.enemies = [enemies(name, health, strength) for name, health, strength in enemies]
        
    def __repr__(self):
        return f"Wave(vague={self.vague}, enemies={self.enemies})"
    
    def pick_ennemie(self, enemy_name):
        for enemy in self.enemies:
            if enemy.name == enemy_name:
                return enemy
        return None

    def play_vague(self):
        for enemy in self.enemies:
            if enemy.is_alive:
                damage = enemy.strength - self.defense()
                self.take_damage(damage)
                return f"{enemy.name} attacks for {damage} damage."

    def get_difficulty(self):
        return int(self.vague)
