import characters
from display_funcs import slow_print 


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
    print(choice.name)
    return True

def extracting_data(choice):
    print(choice.energy)
    return True

