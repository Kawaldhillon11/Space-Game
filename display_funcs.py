import time
import os

"""
This module containes two functions, both are associated with interacting with Console window
"""

def slow_print(str):

    """
    Prints each character given to it as an argument with some delay to create a old games like feel
    """

    for  char in str:
        print(char, end="", flush= True)
        time.sleep(0.02)    
    print()

def clear_screen():
    """
    Uses OS module to clear console window, depending on the host system os, different commands are used. for windows it uses 'cls' and for linux and maxOS its 'clear'
    """
    if os.name == 'nt':  # for windows 
        _ = os.system('cls')
    else: 
        _ = os.system('clear') # for linux and macOS