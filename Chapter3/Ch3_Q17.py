from math import *
y = int(input('Enter a year: '))
divby4 = (y-1600)//4
divby100 = (y-1600)//100
divby400 = (y-1600)//400
print('The number of years divisible by 4 from 1600 and',y,'is',divby4)
print('The number of years divisible by 100 from 1600 and',y,'is',divby100)
print('The number of years divisible by 400 from 1600 and',y,'is',divby400)
print('The number of leap years between 1600 and',y,'inclusive is',divby4-divby100+divby400+1)