import characters
import time
import random
from display_funcs import slow_print, clear_screen

"""
This module contains functions for all the challenges along with their helper and setup functions
"""

def determine_sequence(random_list : list, correct_list: list):
    """
    this function is a helper function to restore_power function, it calculates the correct sequence order for the randomized list by comapring each list item to the correct list 
    """
    seq = ''
    for item in correct_list:
        index = 0
        found = False
        while not(found):
            if(item == random_list[index]): # keeps checkeing each list item to match with random list item and tracks the index at which they matched
                seq = seq + str(index+1)
                found = True
            else:
                index = index + 1
    return seq

def breaching_ship(choose_func):

    """
    First Challenge function, introduces the challenge, calls choose_func to select a character for the challenege, creates a door_structural_integrity variable and then calls selected character's hit method to try to break the door, depending on the effectiveness of hit method keeps calling it until door_integrity becomes 0 or less than 0
    """

    challenge_intro = "The Ships Docking Mechanism have been Damaged and cannot be Used, We need to find another way of Entering the Ship, If you are Up to the Challeneg One of you could try to Brake Open the Entrance Door. Each hit will consume 1 energy unit. \n"
    choice = choose_func(intro = challenge_intro)

    door_structural_integrity = 180 
    while (choice.energy and (door_structural_integrity >= 0)): # keeps calling hit and decrementing door_structural_integrity unit it reached 0 or below 0
        slow_print("Hitting")
        door_structural_integrity = door_structural_integrity - choice.hit()
        choice.energy = choice.energy -1
        print(f"energy left {choice.energy}")
        print(f"door integrrity {int(door_structural_integrity)}")

    if(choice.energy == 0): # challenge fails if energy requirement not met
        return False
    elif (door_structural_integrity <= 0):
        return True
    
def restore_power_setup(choose_func):
    """
    setuo function for 2nd challenge, introduces the challenge, calls choose_func to select a character for the challenege, randomises the sequence list and takes input from player and then calls challeneg function to test the sequence entered by player
    """
    time.sleep(2)
    challenge_intro = "Nice Job! You have Entered the Ship, now we need to Restore Power so that Required Data could be Extracted, To Restore Power we need to execute some steps in correct order, on the screen you will see jumbled steps due to damage to the ship, the Time for which the steps will remain on the screen depends on your hacking abilities, This Challenge will use 4 units of Energy \n"
    clear_screen()
    choice = choose_func(intro = challenge_intro)

    if(choice.energy < 3):
        slow_print("Character Does not Have enough energy")
        return False
    choice.energy -= 4 

    slow_print("Please use following steps in correct ordre to Restore Power ")
    restore_power_steps = [
        "Open Acess Pannel",
        "Connect Hacking Tool",
        "Enter Password",
        "Reboot System"
    ]
    randomized_steps = random.sample(restore_power_steps, k= len(restore_power_steps))

    for index, step in enumerate(randomized_steps, start=1):
        slow_print(str(index) + ". " + step) #prints randomized list of steps

    time.sleep(choice.hacking/10)
    clear_screen()
    entered_sequence = input("Enter Correct Sequence(Example: 1234) : ")
    slow_print("Checking Sequence")
    if restore_power(choice,restore_power_steps, randomized_steps, entered_sequence):
        slow_print("Sequence Matched")
        return True
    else:
        slow_print("Sequence Mismatch")
        return False
    



def restore_power(choice, restore_power_steps, randomized_steps, entered_sequence):
    """
    Second challenge, compares sequence entered by player to computed sequence by calling determine_sequence funcion. Returns true if sequence matched and false otherwise.
    """
    return (entered_sequence == determine_sequence(randomized_steps, restore_power_steps))
        

def extract_data_setup(choose_func):
    """
    setup function for extraxt_data challenge, calls choose_func to select a character for the challenge, takes input from player regarding section of data to look into depending on the amount of energy left for each character also sanatizes and checks if user input is valid. Calls challeneg function to check for data in the selected section.
    """
    time.sleep(2)
    clear_screen()
    challenge_intro = "Great! You are now Entering Data Storage of the Ship, The Storage has 10 Sections and the data we are looking for could be in any one of the Sections, Looking into each Section uses 1 Energy unit, So choose accordingly \n"
    choice  = choose_func(intro = challenge_intro)
    if(choice.energy < 1): # challenge fails if energy requirement not met
        slow_print("Character Does not Have enough energy")
        return False
    slow_print(f"You can choose to look into {choice.energy} Sections")
    sections_to_look = input(f"Please Enter Maximum {choice.energy} Section numbers (e.g 0359) : ")
    if(sections_to_look.isnumeric()): # checks if all input digits are numeric
        sections_to_look_sanitized = sections_to_look[0:choice.energy] # only keeps the maximum allowed digits from input
        if extract_data(sections_to_look_sanitized,  choice):
            slow_print("Data Found!")
            return True
        else:
            slow_print("Data not Found")
    else:
        slow_print("Invalid Section number entered")
        return False


def extract_data(sections_to_look, choice):
    """
    Third challenge function, generates a list of 10 items(sections) and randomly sets one of the list item to True(data) and all other False(empty), uses player input to look for data in selected sections and returns true if found and false otherwise.  
    """
    data_section = random.randint(0,9)
    data_sections_list = []
    for x in range(10):
        data_sections_list.append(x == data_section) #sets value of one of the list items to True, others to False
    
    for index in sections_to_look:
        choice.energy -= 1
        if(data_sections_list[int(index)]== True):
            slow_print(f"Section {index}: Data")
            return True
        slow_print(f"Section {index}: Empty")
        
    return False
    
