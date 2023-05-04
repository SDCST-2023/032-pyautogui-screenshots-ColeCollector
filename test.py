import pyautogui as p
import sys
import time

time.sleep(2)
golden = p.locateAllOnScreen('assets/golden.png', confidence = 0.4)
if golden !=None:
    converted = list(golden)
    print(converted)