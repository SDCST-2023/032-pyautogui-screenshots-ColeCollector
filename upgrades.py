import pyautogui as p
import time
time.sleep(2)

def perks():
    p.moveTo(1275,500)
    p.scroll(900)
    time.sleep(0.5)
    store = p.locateCenterOnScreen('assets/store.png')

    if store != None:
        p.moveTo((store[0]-120),(store[1]+50))
        p.click()



def upgrades():
    maximum = 0
    p.moveTo(1275,500)
    p.scroll(900)
    time.sleep(0.5)
    p.scroll(-500)
    time.sleep(0.5)
    p.moveTo(1275,50)

    upgradeList = ['wizard','temple','bank','factory','mine','farm','grandma','cursor']
    
    for i in upgradeList:
        buy = p.locateCenterOnScreen(f"assets/{i}.png")

        if buy != None:
            #buys 3 most expensive items it can
            if maximum >= 3:
                break

            else:
                p.moveTo(buy)
                p.click()
                maximum = maximum + 1
                time.sleep(0.5)
