import sys
sys.path.append('../')

from animals.animal import Animal
from interfaces.movements import ISwimming
from interfaces.habitats import IAquatic

class RiverDolphin(Animal, ISwimming, IAquatic):

    def __init__(self, gender):
        self.gender = gender
        self.active_hours = "morning"
