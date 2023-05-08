import pyautogui as p
import time


def golden():
    golden1 = p.locateOnScreen('assets/golden1.png', confidence = 0.4)
    golden2 = p.locateOnScreen('assets/golden2.png', confidence = 0.4)

    if golden1 != None:
        p.moveTo(golden1)
        p.click()


    elif golden2 != None:
        p.moveTo(golden2)
        p.click()

            
