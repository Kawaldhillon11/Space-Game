import characters
from display_funcs import slow_print
from display_funcs import clear_screen

def game():

    andy = characters.Character("Andy", 100, 10)
    dr = characters.Character("Dr. Aris", 10, 100)

    welcome_msg = "Welcome to Space Game"
    clear_screen()
    slow_print(welcome_msg)

game()