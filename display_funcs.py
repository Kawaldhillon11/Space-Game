import time

def slow_print(str):
    for  char in str:
        print(char, end="", flush= True)
        time.sleep(0.1)    
    print()

