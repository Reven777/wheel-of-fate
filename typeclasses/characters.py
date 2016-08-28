"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    Custom SoS-statted character. Todo: implement chargen.
    """
def at_object_creation(self):
    "Called only when first created"
    #race attribute creation
    self.db.race = "unassigned"
    #attribute attribute creation
    self.db.agility = 0
    self.db.endurance = 0
    self.db.health = 0
    self.db.willpower = 0
    self.db.wit = 0
    self.db.intelligence = 0
    #derived attribute creation
    self.db.adroitness = 0
    self.db.mobility = 0
    self.db.carry = 0
    self.db.toughness = 0
    self.db.charisma = 0
    self.db.grit = 0
    #skill attribute creation
    self.db.athletics = 0 
    self.db.chemistry = 0
    self.db.climbing = 0
    self.db.cooking = 0
    self.db.crafting = 0
    self.db.drill = 0
    self.db.engineering = 0
    self.db.gather_information = 0
    self.db.history = 0
    self.db.hunting = 0
    self.db.intimidate = 0
    self.db.navigation = 0
    self.db.observation = 0
    self.db.orate = 0
    self.db.perform = 0
    self.db.persuasion = 0
    self.db.politics = 0
    self.db.research = 0
    self.db.riding = 0
    self.db.sailing = 0
    self.db.stealth = 0
    self.db.strategy = 0
    self.db.subterfuge = 0
    self.db.surgery = 0
    self.db.swimming = 0
    self.db.tactics = 0
    #social class attribute creation
    self.db.social_class = "unassigned"
    #magic attribute creation
    self.db.magic = 0

    pass

