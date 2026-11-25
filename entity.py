class entity:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.max_hp = hp

    def __repr__(self):
        return f"Entity(name={self.name}, hp={self.hp}, atk={self.atk}, defense={self.defense})"

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, other):
        if not isinstance(other, entity):
            raise ValueError("Can only attack another entity.")
        damage = max(0, self.atk - other.defense)
        other.take_damage(damage)
        return damage

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp