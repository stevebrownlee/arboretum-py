from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def animal_count(self):
        return "This place has a bunch of animals in it"



    def __str__(self):
        return self.id
