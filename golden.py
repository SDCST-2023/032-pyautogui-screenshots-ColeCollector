import pyautogui as p
import time


def golden():
    golden2 = p.locateOnScreen('assets/golden2.png', confidence = 0.4)
    golden3 = p.locateOnScreen('assets/golden3.png', confidence = 0.4)

    if golden2 != None:
        p.moveTo(golden2)
        p.click()
        print('golden cookie2')

    elif golden3 != None:
        p.moveTo(golden3)
        p.click()
        print('golden cookie3')

            
