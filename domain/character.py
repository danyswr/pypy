# domain/character.py
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.physical = random.randint(5, 100)
        self.defense = random.randint(5, 10)

    def attack(self, enemy):
        damage = max(self.physical - enemy.defense, 0)
        enemy.hp -= damage
        return damage

    def is_alive(self):
        return self.hp > 0