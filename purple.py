import pyautogui

def MTC(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

### Start in menu ###
while True:
    # Click building
    MTC(1477, 526)
    
    # Select options
    MTC(1191, 176)
    MTC(1208, 320)
    MTC(1189, 449)
    MTC(1198, 579)
    MTC(1194, 682)
    
    # Check
    MTC(860, 749)
    
    # Menu
    MTC(50, 156)