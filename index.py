import os

from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")


def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Add Plant to Habitat")
    print("4. Display Facility Report")
    print("5. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        pass

    if choice == "4":
        build_facility_report(keahua)

    if choice != "5":
        main_menu()

main_menu()
