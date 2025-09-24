import random

"""
This module contains the Character class for creating Character objects
"""

class Character:
    def __init__(self, name, strength, hacking):
        """
        initilizer method, initilizes a Character instance with attributes name, energy, strength and hacking
        """
        self.name = name
        self.energy = 10
        self.strength = strength
        self.hacking = hacking
    
    def hit(self):

        """
        this method returns a hit effectiveness value depending on a random integer between 1 and 5 and character's strength attribute
        """

        effectiveness_factor = random.randint(1,5)
        return self.strength/effectiveness_factor

