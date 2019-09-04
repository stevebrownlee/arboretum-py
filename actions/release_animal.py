from animals import RiverDolphin

def release_animal(arboretum):
    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        dolphin = RiverDolphin()
        arboretum.rivers.append(dolphin)
    if choice == "2":
        pass
