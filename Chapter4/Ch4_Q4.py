from math import *
creditsTaken = eval(input('How many credits have you taken? '))
if (creditsTaken < 24):
    print('You must be a freshman.')
elif (creditsTaken < 54):
    print('You must be a sophomore.')
elif (creditsTaken < 84):
    print('You must be a junior.')
else:
    print('You must be a senior.')