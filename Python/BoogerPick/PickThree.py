import time
import os
import random
from colorama import Fore
from tkinter import *

WINS_FILE = "wins.txt"

def get_wins():
    try:
        with open(WINS_FILE, "r") as file:
            wins = int(file.readline())
            return wins
    except FileNotFoundError:
        return 0

def save_wins(wins):
    with open(WINS_FILE, "w") as file:
        file.write(str(wins))

def clear():
    os.system('cls')


wins = get_wins()
redo = 'y'

while(redo == 'y'):

    clear()

    print("Welcome to Pick Three!")
    print("\nI've picked a number, now you try to guess it!")

    print(f"(Wins: {wins})")

    firstnum = random.randint(0, 9)
    secondnum = random.randint(0, 9)
    thirdnum = random.randint(0, 9)
    number = str(firstnum) + str(secondnum) + str(thirdnum)

    firstnumg = int(input("\nPick your first number: "))
    secondnumg = int(input("Pick your second number: "))
    thirdnumg = int(input("Pick your third number: "))
    guess = str(firstnumg) + str(secondnumg) + str(thirdnumg)

    if(guess != number):
        print(f"{Fore.RED}\nYou lost, sorry!{Fore.WHITE}")
        print(f"\nThe number was: {number}")
    else:
        print(f"{Fore.GREEN}\nYou won!{Fore.WHITE}")
        wins += 1
        save_wins(wins)

    redo = input("\nPlay again? (y/n): ")

    if(redo == 'y'):
        redo = 'y'
    elif(redo == 'n'):
        redo = 'n'
    else:
        print("\nInvalid option...exiting.")
