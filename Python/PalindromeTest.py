### Palindrome Test

import os

def clear():
    os.system('cls')

clear()

print("Input what you would like to test: ")
while(True):
    user_input = input()

    if(user_input[::-1] == user_input):
        print("Your input is a palindrome!\n")
    else:
        print("Your input is not a palindrome.\n")
