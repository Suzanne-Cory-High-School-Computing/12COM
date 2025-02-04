from math import *
for i in range(1,10000):
    sum = 0
    for j in range(1,i):
        if (i%j == 0): #finding the divisors of the number i
            sum += j
    if sum == i: # the sum of the divisors of i is equal to i
        print('The number',i,'is a perfect number.')