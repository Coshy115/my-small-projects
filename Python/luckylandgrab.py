import pyautogui
import time

# Move Then Click
def MTC(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Open Chrome
MTC(75, 1050)
time.sleep(2)

# Redirect to LuckyLand Slots
pyautogui.hotkey("ctrl", "n")
time.sleep(0.5)
pyautogui.write("https://luckylandslots.com/loader")
pyautogui.press("enter")
time.sleep(5)

