from math import *
numItems = eval(input('How many items are you buying? ' ))
if (numItems < 10):
    print('You are buying',numItems,'items.  The total cost is',numItems*12)
elif (numItems <= 99):
    print('You are buying',numItems,'items.  The total cost is',numItems*10)    
else:
    print('You are buying',numItems,'items.  The total cost is',numItems*7)