import pyautogui
import time
from pathlib import Path

def image_path(image_name):
    return str(Path(__file__).parent / "Images" / "luckylandgrab" / image_name)

# Login Details
email = "codydls8988@gmail.com"
password = "**BlueFish11**"

# Open Chrome
chrome_location = pyautogui.locateCenterOnScreen(image_path("chrome.png"), grayscale=True, confidence=0.8)
pyautogui.click(chrome_location)

# Go to Lucky Land Slots
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://luckylandslots.com/loader")
pyautogui.hotkey('enter')
time.sleep(3)

# Log in if necessary
try:
    login_location = pyautogui.locateCenterOnScreen(image_path("login.png"), grayscale=True, confidence=0.8)
    if login_location:
        pyautogui.moveTo(login_location, duration=1)
        pyautogui.click(login_location)
    time.sleep(1)
    pyautogui.write(email, interval=0.05)
    passfield_location = pyautogui.locateCenterOnScreen(image_path("passfield.png"), grayscale=True, confidence=0.8)
    if passfield_location:
        pyautogui.moveTo(passfield_location, duration=1)
        pyautogui.click()
        pyautogui.write(password, interval=0.05)
        login2_location = pyautogui.locateCenterOnScreen(image_path("login2.png"), grayscale=True, confidence=0.8)
        if login2_location:
            pyautogui.moveTo(login2_location, duration=1)
            pyautogui.click()
except pyautogui.ImageNotFoundException:
    pass

# Collect Daily Bonus
time.sleep(5)
pyautogui.click(615, 595)
pyautogui.click(853, 588)
pyautogui.click(1092, 586)
pyautogui.click(618, 824)
pyautogui.click(853, 816)
pyautogui.click(1097, 808)
pyautogui.click(1323, 670)