import random

class Character:
    def __init__(self, name, strength, hacking):
        self.name = name
        self.energy = 10
        self.strength = strength
        self.hacking = hacking
    
    def hit(self):
        effectiveness_factor = random.randint(1,5)
        return self.strength/effectiveness_factor

