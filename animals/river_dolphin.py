import sys
sys.path.append('../')

from animals.animal import Animal
from interfaces.movements import ISwimming
from interfaces.habitats import IBrackish
from interfaces.habitats import ICoastal

class RiverDolphin(Animal, ISwimming, IBrackish, ICoastal):

    def __init__(self, gender):
        self.gender = gender
        self.active_hours = "morning"
