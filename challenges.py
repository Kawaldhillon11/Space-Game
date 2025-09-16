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

def breaching_ship(choice):
    print(choice.name)

    door_structural_integrity = 180
    while (choice.energy and (door_structural_integrity >= 0)):
        slow_print("Hitting")
        door_structural_integrity = door_structural_integrity - choice.hit()
        choice.energy = choice.energy -1
        print(f"energy left {choice.energy}")
        print(f"door integrrity {door_structural_integrity}")

    if(choice.energy == 0):
        return False
    elif (door_structural_integrity <= 0):
        return True
    

def restoring_power(choice):

    clear_screen()
    print(choice.name)
    slow_print("Please use following steps in correct ordre to Restore Power ")
    restore_power_steps = [
        "Open Acess Pannel",
        "Connect Hacking Tool",
        "Enter Password",
        "Reboot System"
    ]
    password = "Admin"
    randomized_steps = random.sample(restore_power_steps, k= len(restore_power_steps))

    for index, step in enumerate(randomized_steps, start=1):
        slow_print(str(index) + ". " + step)

    time.sleep(choice.hacking/10)
    clear_screen()
    if ((input("Enter Correct Sequence(Example: 1234) : ")) == determine_sequence(randomized_steps, restore_power_steps)):
        return True
    else: 
        return False



def extracting_data(choice):
    print(choice.energy)
    return True

print(restoring_power(tubi))
