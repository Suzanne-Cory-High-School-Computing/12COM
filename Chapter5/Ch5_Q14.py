from random import randint
from math import *

numgames = 10000
winIfSwitch = 0
winIfNoSwitch = 0

print('Playing with three doors...')
for i in range(numgames):
    # new game
    winningdoor = randint(1,3)
    DoorA = 'Goat'
    DoorB = 'Goat'
    DoorC = 'Goat'
    if (winningdoor == 1):
        DoorA = 'Prize'
    elif (winningdoor == 2):
        DoorB = 'Prize'
    else:
        DoorC = 'Prize'

    #print('Doors: ',DoorA,DoorB,DoorC) # debug

    # asking the contestant to pick a door
#    guess = input('Which door would you like (a, b or c): ') #debug
    guess = randint(1,3)
    if (guess == 1):
        #print('Contestant picked Door A')
        if (DoorA == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    elif (guess == 2):
        #print('Contestant picked Door B')
        if (DoorB == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    elif (guess == 3):
        #print('Contestant picked Door C')
        if (DoorC == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    else:
        print('Invalid choice.')
print('Percentage of time you win if you switch: ',(winIfSwitch/numgames)*100,'%')
print("Percentage of time you win if you don't switch: ",(winIfNoSwitch/numgames)*100,'%')

print('Playing with four doors...')
winIfSwitch = 0
winIfNoSwitch = 0
for i in range(numgames):
    # new game
    winningdoor = randint(1,4)
    DoorA = 'Goat'
    DoorB = 'Goat'
    DoorC = 'Goat'
    DoorD = 'Goat'
    if (winningdoor == 1):
        DoorA = 'Prize'
    elif (winningdoor == 2):
        DoorB = 'Prize'
    elif (winningdoor == 3):
        DoorC = 'Prize'
    else:
        DoorD = 'Prize'

    #print('Doors: ',DoorA,DoorB,DoorC,DoorD) # debug

    # asking the contestant to pick a door
#    guess = input('Which door would you like (a, b or c): ') #debug
    guess = randint(1,4)
    if (guess == 1):
        #print('Contestant picked Door A')
        if (DoorA == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    elif (guess == 2):
        #print('Contestant picked Door B')
        if (DoorB == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    elif (guess == 3):
        #print('Contestant picked Door C')
        if (DoorC == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    elif (guess == 4):
        #print('Contestant picked Door D')
        if (DoorD == 'Prize'):
            winIfNoSwitch += 1
            #print("You will win if you don't switch.")
        else:
            winIfSwitch += 1
            #print("You will win if you switch.")
    else:
        print('Invalid choice.')
print('Percentage of time you win if you switch: ',(winIfSwitch/numgames)*100,'%')
print("Percentage of time you win if you don't switch: ",(winIfNoSwitch/numgames)*100,'%')