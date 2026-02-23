import random

def __init__(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power

def __str__(self):
        return f"{self.name}: {self.description} (Power: {self.power})"

class Sheild:
    def __init__(self, name, description, defense):
        self.name = name
        self.description = description
        self.defense = defense
    def __str__(self):
        return f"{self.name}: {self.description}. Power: {self.power}"

    class Monster:
        def __init__(self, name, description, health, attack, defense):
            self.name = name
            self.health = health
            self.attack = attack
            self.defense = defense
            self.description = description