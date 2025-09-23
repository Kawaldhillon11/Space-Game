import characters
import time
import random
from display_funcs import slow_print, clear_screen


tubi = characters.Character("Tubi", 10, 50)

def determine_sequence(random_list : list, correct_list: list):
    seq = ''
    for item in random_list:
        index = 0
        found = False
        while not(found):
            if(item == correct_list[index]):
                seq = seq + str(index+1)
                found = True
            else:
                index = index + 1
    return seq

def breaching_ship(choose_func):
    challenge_intro = "The Ships Docking Mechanism have been Damaged and cannot be Used, We need to find another way of Entering the Ship, If you are Up to the Challeneg One of you could try to Brake Open the Entrance Door."
    choice = choose_func(intro = challenge_intro)

    door_structural_integrity = 180
    while (choice.energy and (door_structural_integrity >= 0)):
        slow_print("Hitting")
        door_structural_integrity = door_structural_integrity - choice.hit()
        choice.energy = choice.energy -1
        print(f"energy left {choice.energy}")
        print(f"door integrrity {int(door_structural_integrity)}")

    if(choice.energy == 0):
        return False
    elif (door_structural_integrity <= 0):
        return True
    
def restore_power_setup(choose_func):
    time.sleep(2)
    challenge_intro = "Nice Job! You have Entered the Ship, now we need to Restore Power so that Required Data could be Extracted, To Restore Power we need to execute some steps in correct order, on the screen you will see jumbled steps due to damage to the ship, the Time for which the steps will remain on the screen depends on your hacking abilities, This Challenge will use 4 units of Energy"
    clear_screen()
    choice = choose_func(intro = challenge_intro)

    if(choice.energy < 5):
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
        slow_print(str(index) + ". " + step)

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

    return (entered_sequence == determine_sequence(randomized_steps, restore_power_steps))
        

def extract_data_setup(choose_func):
    time.sleep(2)
    clear_screen()
    challenge_intro = "Great! You are now Entering Data Storage of the Ship, The Storage has 10 Sections and the data we are looking for could be in any one of the Sections, Looking into each Section uses 1 Energy unit, So choose accordingly"
    choice  = choose_func(intro = challenge_intro)
    if(choice.energy < 1):
        slow_print("Character Does not Have enough energy")
        return False
    slow_print(f"You can choose to look into {choice.energy} Sections")
    sections_to_look = input(f"Please Enter Maximum {choice.energy} Section numbers (e.g 12345) : ")
    if(sections_to_look.isnumeric()):
        sections_to_look_sanitized = sections_to_look[0:choice.energy]
        if extract_data(sections_to_look_sanitized,  choice):
            slow_print("Data Found!")
            return True
        else:
            slow_print("Data not Found")
    else:
        slow_print("Invalid Section number entered")
        return False


def extract_data(sections_to_look, choice):
    data_section = random.randint(0,9)
    data_sections_list = []
    for x in range(10):
        data_sections_list.append(x == data_section)
    
    for index in sections_to_look:
        choice.energy -= 1
        if(data_sections_list[int(index)]== True):
            return True
        
    return False
    
    

# restore_power_setup(tubi)
# extract_data_setup(tubi)