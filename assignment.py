import pyautogui as p
import time
import random
import sys
import upgrades

#waits 2 seconds
time.sleep(2)

#finds cookie and the store
location = p.locateOnScreen('assets/cookie.png')
store = p.locateOnScreen('assets/store.png')


#Makes the program stop looping if its been more than 30 seconds
start = time.time()
end = (start + 30)

#loop
while end > start:
    start = time.time()

    #if cookie is found start program
    if location != None:
        golden = p.locateOnScreen('assets/golden1.png', confidence = 0.7)
        upgrade = p.locateOnScreen('assets/upgrade.png', confidence = 0.5)
        
        for i in range (0,200):
            #autoclicker
            p.moveTo(location) 
            p.tripleClick()

            #golden cookie finder
            if golden != None:
                p.moveTo(golden)
                p.click
                time.sleep(0.5)
        
        #using the store
        randomchoice = random.randint(1,2)
        
        if randomchoice == 1:
            upgrades.perks()

        else:
            upgrades.upgrades()

    elif location == None:
        break
    
    
print("Program finished")
    


