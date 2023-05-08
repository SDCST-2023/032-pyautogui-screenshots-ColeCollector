import pyautogui as p
import sys
import time

time.sleep(2)
golden1 = p.locateOnScreen('assets/golden1.png', confidence = 0.4)
golden2 = p.locateOnScreen('assets/golden2.png', confidence = 0.4)
if golden1 != None:
    print("1")
    p.moveTo(golden1)
    time.sleep(2)
if golden2 != None:
    print("2")
    p.moveTo(golden2)
    time.sleep(2)