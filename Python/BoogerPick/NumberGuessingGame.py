import random
from colorama import Fore
import os
import time

def get_highscore():
    try:
        with open("highscore.text", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return float("inf")

def save_highscore(score):
    with open("highscore.text", "w") as file:
        file.write(str(score))

def clear():
    os.system("cls")

highscore = get_highscore()
target = random.randint(1, 100)

clear()

time.sleep(1)
print("I'm thinking of a number between 1 and 100...")
time.sleep(1)
print("Try to guess it!")

attempts = 0

while(True):
    guess = int(input())
    attempts += 1

    if(guess > target):
        print("Lower")
    elif(guess < target):
        print("Higher")
    else:
        print("You got it!")
        time.sleep(1)
        print(f"Your score: {attempts}")
        time.sleep(1)
        print(f"Highscore: {highscore}")
        
        if(attempts < highscore):
            print(f"{Fore.GREEN}New highscore!{Fore.WHITE}")
            save_highscore(attempts)
        break
