import random
import time
import os

# Clears the screen.
def clear():
    os.system('cls')

while True:
    try:
        clear()

        #Asks the user for input.
        seasons = int(input("How many seasons?: "))
        episodes = int(input("How many episodes in each season?: "))
        
        #Randomly selects numbers based on input.
        randseason = random.randint(1, seasons)
        randepisode = random.randint(1, episodes)

        #Displays the randomly selected numbers.
        print(f"I have chosen \033[1mseason {randseason} episode {randepisode}\033[0m.")
        time.sleep(1)

        #Asks the user if they would like to retry.
        redo = input("Would you like to try again? (y/n): ")

        #If the user wants to retry, the program will restart. If not, the program will end.
        if(redo.lower() != 'y'):
            clear()
            print("Goodbye!")
            time.sleep(1)
            break

    except ValueError:
        clear()
        print("Invalid input. Please enter a valid number.")
        time.sleep(1)
