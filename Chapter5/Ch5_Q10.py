from math import *
num = eval(input('Enter a number: '))
highest = num
nexthighest = num
lowest = num
nextlowest = num
count = 1
sum = num
warning = 0
for i in range(9):
    num = eval(input('Enter a number: '))
    if (num > highest):
        nexthighest = highest
        highest = num
        if (lowest == nextlowest):
            nextlowest = nexthighest
    elif (num < lowest):
        nextlowest = lowest
        lowest = num
        if (highest == nexthighest):
            nexthighest = nextlowest
    count += 1
    sum += num
    if (num > 100):
        warning = 1
print('The highest score is',highest)
print('The lowest score is',lowest)
print('The next lowest score is',nextlowest)
print('The average of the scores is',sum/count)
print('The second largest score is',nexthighest)
if (warning == 1):
    print('Warning: You have entered a value greater than 100')
print('Dropping the two lowest scores of',lowest,'and',nextlowest,'the average is',(sum-nextlowest-lowest)/(count-2))