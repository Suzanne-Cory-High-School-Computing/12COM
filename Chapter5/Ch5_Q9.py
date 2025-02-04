from math import *
count = 1000
perfect = 0
for i in range(1,1001):
    perfect = 0
    for j in range(1,i):
        square = j**2
        cube = j**3
        fifth = j**5
        if(i==square):
            print('The number',i,'is a perfect square.')
            perfect = 1
        elif(i==cube):
            print('The number',i,'is a perfect cube.')
            perfect = 1
        elif(i==fifth):
            print('The number',i,'is a perfect fifth power.')
            perfect = 1
    if (perfect == 1):
        count -= 1
print('There are',count,'integers from 1 to 1000 that are not perfect squares, perfect cubes or perfect fifth powers.')
