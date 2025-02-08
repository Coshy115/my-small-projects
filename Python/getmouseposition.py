import pyautogui

print("Place your mouse over the desired location and press Enter...\n")

input() # Wait for the user to press Enter

while True:
    print(pyautogui.position()) # Print the mouse position
    input()
