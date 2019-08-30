# Classes we need
# Arboretum
  # contains these properties
    # Enviroment
        # contains these things
          # Plant
          # Animal

#Plant
  # WildFlower
  # MangoTree
  # CoconutTree

# Animal
  # Butterfly
  # Dragonfly
  # RiverDolphin

# Environment
  # Swamp
  # Coastline
  # River
  # Grassland
import sys
sys.path.append('../')

from arboretum import Arboretum
from environments.river import River
from animals.river_dolphin import RiverDolphin

keahua = Arboretum("Keahua Arboretum", "123 HeyIwannaLeiya Lane")
brackish_river = River("Happy Salty River")
flipper = RiverDolphin("female")
brackish_river.addInhabitant(flipper)
keahua.environments.append(brackish_river)
print(keahua.__dict__)
print(keahua.environments[0].inhabitants)
