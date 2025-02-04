from math import *
seconds = int(input('Enter the number of seconds you want to convert: '))
minutes = seconds // 60
convertedseconds = seconds % 60
print('The converted value is ',minutes,' minutes and ',convertedseconds,' seconds.')