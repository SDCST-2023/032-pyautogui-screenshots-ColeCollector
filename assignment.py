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


#Makes the program stop looping if its been more than 20 seconds
start = time.time()
end = (start + 20)

#loop
while end > start:
    start = time.time()

    #if cookie is found start program
    if location != None:
        golden1 = p.locateOnScreen('assets/golden1.png', confidence = 0.4)
        golden2 = p.locateOnScreen('assets/golden2.png', confidence = 0.4)
        
        for i in range (0,300):
            #autoclicker
            p.moveTo(location) 
            p.tripleClick()

            #golden cookie finder
            if golden1 != None:
                p.moveTo(golden1)
                p.click()
                time.sleep(0.5)
                print("golden cookie1 found")

            if golden2 != None:
                p.moveTo(golden2)
                p.click()
                time.sleep(0.5)
                print("golden cookie2 found")

        
        #using the store
        #66% of the time it buys upgrades
        #33% of the time it buys perks
        randomchoice = random.randint(1,3)
        
        if randomchoice == 1:
            upgrades.perks()

        else:
            upgrades.upgrades()

    elif location == None:
        break
    
    
print("Program finished")
    


