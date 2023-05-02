import pyautogui as p
import time
time.sleep(2)
def perks():
    p.moveTo(1275,500)
    p.scroll(900)
    store = p.locateCenterOnScreen('assets/store.png')

    if store != None:
        p.moveTo((store[0]-120),(store[1]+50))
        p.click()



def upgrades():
    p.moveTo(1275,500)
    p.scroll(900)
    time.sleep(0.5)
    p.scroll(-250)



upgrades()