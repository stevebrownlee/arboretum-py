import sys
sys.path.append('../')

from environments.environment import Environment
from interfaces.habitats import IBrackish
from animals.river_dolphin import RiverDolphin


class River(Environment):

    def __init__(self, name):
      self.name = name
      self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IBrackish):
            raise TypeError(f"{item} is not of type IBrackish")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name
