from math import *
x = eval(input('Enter the first number, x: '))
y = eval(input('Enter the second number, y: '))
z = eval(input('Enter the third number, z: '))
print('The values of x, y and z are',x,y,z)
print('Swapping the values...')
x,y,z = y,z,x
print('The values of x, y and z are now',x,y,z)