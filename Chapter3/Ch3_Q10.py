from math import *
number = int(input('Enter a number: '))
exp = 2**number
print('You are looking for 2 raised to the power of ',number,end=' ')
print('which is ',exp)
print('The last digit of this number is ',exp%10)
print('The last two digits of this number are ',exp%100)
digits = int(input('How many digits would you like to show? '))
print('The last ',digits,'digits of this number are ',exp%(10**digits))