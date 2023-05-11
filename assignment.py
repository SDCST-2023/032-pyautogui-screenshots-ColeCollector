import pyautogui as p
import time
import random
import sys
import upgrades
import golden
import clicker

#waits 2 seconds
time.sleep(3)

#finds cookie and the store
location = p.locateOnScreen('assets/cookie.png')
store = p.locateOnScreen('assets/store.png')


#Makes the program stop looping if its been more than 60 seconds
start = time.time()
end = (start + 60)

#loop
while end > start:
    start = time.time()

    #if cookie is found start program
    if location != None:
        for i in range (0,20):
            #autoclicker
            p.moveTo(location) 
            clicker.autoclicker()

            #golden cookie checker
            golden.golden()
            

        
        #using the store
        randomchoice = random.randint(1,2)
        
        #33% of the time it buys perks
        if randomchoice == 1:
            upgrades.perks()
        #66% of the time it buys upgrades
        else:
            upgrades.upgrades()

    #if cookie isn't found stop program
    elif location == None:
        print("Cookie not found")
        break
    
    
print("Program finished")
    


