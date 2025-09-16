import characters
import challenges
from display_funcs import slow_print
from display_funcs import clear_screen

def choose_character(character1, character2):
    slow_print(f"1. {character1.name}")
    slow_print(f"2. {character2.name}")

    while True:
        choice = int(input("Choose a Character: "))
        if(choice == 1 or choice == 2):
            if(choice == 1):
                return character1
            else:
                return character2

def game():

    andy = characters.Character("Andy", 100, 10)
    dr = characters.Character("Dr. Aris", 10, 100)

    challeneges_list = [challenges.breaching_ship, challenges.restoring_power, challenges.extracting_data]

    welcome_msg = "Welcome to Space Game"
    clear_screen()
    slow_print(welcome_msg)

    for challenge in challeneges_list:
        choice = choose_character(andy, dr)
        challenge(choice)


game()