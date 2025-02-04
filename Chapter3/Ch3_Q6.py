from math import *
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
print('The numerator is the absolute value of ',num1,' minus ',num2,end=' ')
numerator = abs(num1 - num2)
print('which is ',numerator)
print('The denominator is ',num1,' plus ',num2,end=' ')
denominator = num1 + num2
print('which is ',denominator)
print('The answer is ',numerator/denominator)