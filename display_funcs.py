import time

str = "Hi this is a test"


def slow_print(str):
    for  char in str:
        print(char, end="", flush= True)
        time.sleep(0.1)    
    print()

slow_print(str)