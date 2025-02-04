import pyautogui
import time

# Move Then Click
def MTC(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Open Chrome
MTC(75, 1050)
time.sleep(2)

# Redirect to Chumba Casino
pyautogui.hotkey("ctrl", "n")
time.sleep(0.5)
pyautogui.write("https://www.chumbacasino.com/")
pyautogui.press("enter")
time.sleep(5)

# Log in
MTC(1363, 153)
time.sleep(2)
MTC(280, 557)
time.sleep(5)

MTC(970, 149)
MTC(1748, 148)
MTC(1186, 234)
MTC(967, 934)

print("Process Complete")
input()