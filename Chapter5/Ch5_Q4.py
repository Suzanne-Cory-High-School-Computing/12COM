from math import *
sum = 0
for i in range(2001):
    if (i%2==1): # odd number
        sum += i
        print('Adding',i,'the current sum is',sum)
    else:    # even number
        sum -= i
        print('Subtracting',i,'the current sum is',sum)
print('The sum of 1-2+3-4+...+1999-2000 is',sum)