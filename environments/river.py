from .environment import Environment
from interfaces import IAquatic
from animals import RiverDolphin


class River(Environment):

    def __init__(self):
      self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IAquatic):
            raise TypeError(f"{item} is not of type IAquatic")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name
