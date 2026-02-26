import random

class Weapon:
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

class Location:
    def __init__(self, name, description):
        self.name = name
        self.monster = 0
        self.description = description
        self.items = []
        self.exits = []

def link(self, other, direction):
        self.exits[direction] = other

def enter(self):
    pass

def examine(self, thing):
    print(f"There is no {thing} here")

def describe(self):
    print(f"\n== {self.name} here")
    print(self.description)
    if len(self.items) > 0:
        print("\nYou see:")
        for item in self.items:
            print(f" - {item}")
            if self.monster != 0:
                print(f"\nA {self.monster.name} is here! {self.description}")

class Player:
    def __init__(self, NAME, LOCATION, ATTACK , DEFENSE, HEALTH):
        self.inventory = []       
        self.name = NAME
        self.location = LOCATION
        self.attack = ATTACK
        self.defense = DEFENSE
        self.health = HEALTH

        def heal(self, amount):
            self.HEALTH = min(self.HEALTH + amount, self.max_HEALTH)

        def move(self, direction):
                if direction in self.location.exits:
                    self.location.exit()
                    self.location = self.location.exits[direction]
                    self.location.describe()
                    self.location.enter()
                else:
                      print("you cant go that way")
    
    def take(self, item_name):
        for item in self.location.items:
            if item.name.lower() == item_name.lower():
              if type(item) == Sheild or type(item) == Weapon:
                for inventory_item in self.inventory:
                    if type(item) == type(inventory_item):
                        self.drop(inventory_item.name)

            if type(item) == Sheild:
                self.defense = item.power
    
            if type(item) == Weapon:
                self.attack = item.power

            self.inventory.append(item)
            self.location.items.remove(item)
            print(f"you pick up the {item.name}.")
            return
    print(f"There is no such item here.")