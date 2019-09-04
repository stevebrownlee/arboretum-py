def build_facility_report(arboretum):
    # Show all habitats with all their animules and plaunts
    for river in arboretum.rivers:
        print(f"river{river.id}: Animals: ")
        for animal in river.animals:
            print(f"{animal.id} ")
