import time
import os

def slow_print(str):
    for  char in str:
        print(char, end="", flush= True)
        time.sleep(0.1)    
    print()

def clear_screen():
    if os.name == 'nt':  
        _ = os.system('cls')
    else: 
        _ = os.system('clear')