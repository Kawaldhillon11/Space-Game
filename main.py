import characters
import challenges
from display_funcs import slow_print
from display_funcs import clear_screen

"""
Main module that controls the flow of game.
"""

def game():
    """
    Game fuction creates two characters using Character Class and defines a choose_func to choose between characters for each challenge, loops through each challenge and asks user for another try if challenge fails. Returns True if all 3 challenges are sucessfull.
    """
    andy = characters.Character("Andy", 100, 40)
    dr = characters.Character("Dr. Aris", 10, 120)

    def choose_character(character1 = andy , character2 = dr, intro = ""):
        """
        function to choose between defined characters, asks user for input, checks if input is valid otherwise asks again.
        """
        slow_print(intro)
        slow_print("Choose One")
        # prints both characters stats
        slow_print(f"1. {character1.name}, Energy: {character1.energy}, Hacking: {character1.hacking}, Strength: {character1.strength}")
        slow_print(f"2. {character2.name}, Energy: {character2.energy}, Hacking: {character2.hacking}, Strength: {character2.strength}")

        while True:
            choice = int(input("Choose a Character: "))
            if(choice == 1 or choice == 2): #only 1 or 2 as input is accepted
                if(choice == 1):
                    return character1
                else:
                    return character2
            else:
                print("Invalid")

    challeneges_list = [challenges.breaching_ship, challenges.restore_power_setup, challenges.extract_data_setup]

    welcome_msg = "Welcome to Top Secret Mission, One of our Space Discovery ships got Stranded in Space near Mars, We think they might have been Attcked, They were comming back with valuable data, Your Mission is to Extract the Data and look for any Survivors \n"
    clear_screen()
    slow_print(welcome_msg)
    # loop for all the challenges
    for challenge in challeneges_list:
        running = True
        while running:
            if not (challenge(choose_character)):
                if (input("Try Again (Y/N)? ").casefold() == "n"):
                    running = False
                    return False
            else:
                slow_print("Challenge Passed!")
                running = False 
    return True
    
                

if game():
    slow_print("Great Job! We Thank you both for your Service.")
else:
    slow_print("Quest Failed!")
