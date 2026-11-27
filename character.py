class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.equipment = {}
        
        #+List~Equipable~ equipement
    def list_equipment(self):
        return list(self.equipment.values())
        
        #+/attack: int
    def attack(self):
        return self.strength
    
    #+/defense: int
    def defense(self):
        return 0  # Placeholder implementation

    #+EquipItem(item: Equipable)
    def equip_item(self, item):
        self.equipment[item.slot] = item

    #+UnequipItem(item: Equipable)
    def unequip_item(self, item):
        if item.slot in self.equipment:
            del self.equipment[item.slot]

        #+IsSlotAvailable(slot_name: String) bool
    def is_slot_available(self, slot_name):
        return slot_name not in self.equipment

        #+GetEquipment(slot_name: String) Equipable
    def get_equipment(self, slot_name):
        return self.equipment.get(slot_name)

        #+ProjectDamage(target: Entity) int
    def project_damage(self, target):
        return self.attack() - target.defense()

        #+PlayTurn() «override»
    def play_turn(self):
        enemy = self.choose_enemy()
        if enemy:
            damage = self.project_damage(enemy)
            enemy.take_damage(damage)
            return f"{self.name} attacks {enemy.name} for {damage} damage."