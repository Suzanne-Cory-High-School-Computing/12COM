from math import *
num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))
if (abs(num1 - num2) < 0.001):
    print('Close')
else:
    print('Not close')