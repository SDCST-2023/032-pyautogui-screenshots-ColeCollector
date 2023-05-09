import pyautogui as p
import time
import random
import sys
import upgrades
import golden
import clicker

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
        p.moveTo(location) 

        for i in range (0,10):
            #autoclicker
            p.moveTo(location) 
            clicker.autoclicker()

            #golden cookie checker
            golden.golden()
            

        
        #using the store
        randomchoice = random.randint(1,3)
        
        #33% of the time it buys perks
        if randomchoice == 1:
            upgrades.perks()
        #66% of the time it buys upgrades
        else:
            upgrades.upgrades()

    #if cookie isn't found stop program
    elif location == None:
        break
    
    
print("Program finished")
    


