from math import *
change = float(input('What is the amount of change needed that is less than $1.00? '))
changeInCents = floor(change*100)
quarters = changeInCents // 25
changeInCents -= quarters * 25
dimes = changeInCents // 10
changeInCents -= dimes * 10
nickels = changeInCents // 5
changeInCents -= nickels * 5
print('You should provide',quarters,'quarters,',dimes,'dimes,',nickels,'nickels, and',changeInCents,'pennies.')