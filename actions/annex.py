from environments import River

def annex_habitat(arboretum):
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
