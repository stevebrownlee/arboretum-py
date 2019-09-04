from animals import Animal
from interfaces import ISwimming
from interfaces import IAquatic

class RiverDolphin(Animal, ISwimming, IAquatic):

    def __init__(self, gender):
        self.gender = gender
        self.active_hours = "morning"
