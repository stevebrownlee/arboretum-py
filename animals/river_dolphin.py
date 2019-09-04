from animals import Animal
from interfaces import ISwimming
from interfaces import IAquatic

class RiverDolphin(Animal, ISwimming, IBrackish, ICoastal):

    def __init__(self):
        self.active_hours = "morning"
