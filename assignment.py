import pyautogui as p
import time
import upgrades

#waits 2 seconds
time.sleep(2)

#finds cookie and the store
location = p.locateOnScreen('assets/cookie.png')
store = p.locateOnScreen('assets/store.png')


#Gives the program a lifetime of 10 seconds
start = time.time()
end = (start + 15)

#loop
while end > start:
    start = time.time()

    #if cookie is found start program
    if location != None:
        golden = p.locateOnScreen('assets/golden.png', confidence = 0.8)
        upgrade = p.locateOnScreen('assets/upgrade.png', confidence = 0.5)
        
        for i in range (0,100):
            #autoclicker
            p.moveTo(location) 
            p.tripleClick()

            #golden cookie finder
            if golden != None:
                p.moveTo(golden)
                p.leftClick
                print("found a golden cookie")
        
        #store perks
        upgrades.perks()
        upgrades.upgrades()

    elif location == None:
        break

        
    
    
print("done")
    


