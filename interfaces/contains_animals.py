class IContainsAnimals():

    def __init__(self):
        self.animals = []

    def addAnimal(self, item):
      try:
        if self.move("foo", 2 ):
          self.animals.append(item)
      except AttributeError:
        raise AttributeError(f"{item} is not an animal. Meow")
