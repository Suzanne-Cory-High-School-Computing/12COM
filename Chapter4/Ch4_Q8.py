from math import *
year = eval(input('What year are you looking at? '))
if (year%4 != 0): #not divisible by 4
    print(year,'is not a leap year.')
else: #divisible by 4
    if (year%100==0 and year%400!=0): #divisible by 100 but not divisible by 400
        print(year,'is not a leap year.')
    else:
        print(year,'is a leap year.')