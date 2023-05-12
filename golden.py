import pyautogui as p
import time


def golden():
    golden1 = p.locateOnScreen('assets/golden1.png', confidence = 0.3)
    golden = p.locateOnScreen('assets/golden.png', confidence = 0.3)
    
    if golden1 != None:
        p.moveTo(golden1)
        p.click()
        print('golden cookie1')


    elif golden != None:
        p.moveTo(golden)
        p.click()
        print('golden cookie')
