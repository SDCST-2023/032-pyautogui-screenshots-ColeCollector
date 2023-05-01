import pyautogui as p
import time


time.sleep(2)
location = p.locateOnScreen('assets/cookie.png')


while True:
    if location != None:
        golden = p.locateOnScreen('assets/golden.png', confidence = 0.9)
        upgrade = p.locateOnScreen('assets/upgrade.png', confidence = 0.8)
        
        #autoclicker
        p.moveTo(location) 
        p.tripleClick()

        if a:
            p.moveTo(1152,188)
            p.click



        elif golden != None:
            p.moveTo(golden)
            p.click
            time.sleep(2)
        
        elif upgrade != 
    
    
print("done")
    


