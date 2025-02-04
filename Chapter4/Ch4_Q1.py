from math import *
lengthInCm = eval(input('Enter the length in centimetres: '))
if (lengthInCm < 0):
    print('Invalid entry!')
else:
    print('The length in inches is',lengthInCm/2.54)