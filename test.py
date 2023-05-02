import pyautogui as p
import time

time.sleep(2)
mylist = location = p.locateAllOnScreen('assets/upgrade.png',confidence=0.9)
converted = list(mylist)
print("locate all found (as list):",converted)