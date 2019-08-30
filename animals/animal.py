class Animal:

    def __init__(self, species, *months_present):
        self.species = species
        self.months_present = months_present


    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
