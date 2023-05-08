import pyautogui as p
import time
import random
import sys
import upgrades
import golden

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
        
        for i in range (0,300):
            #autoclicker
            p.moveTo(location) 
            p.tripleClick()
            golden.golden()

        
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
    


