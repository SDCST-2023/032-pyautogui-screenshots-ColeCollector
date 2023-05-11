import pyautogui as p
import time


def golden():
    golden2 = p.locateOnScreen('assets/golden2.png', confidence = 0.4)
    golden1 = p.locateOnScreen('assets/golden1.png', confidence = 0.4)

    if golden2 != None:
        p.moveTo(golden2)
        p.click()
        print('golden cookie2')

    elif golden1 != None:
        p.moveTo(golden1)
        p.click()
        print('golden cookie1')

            
