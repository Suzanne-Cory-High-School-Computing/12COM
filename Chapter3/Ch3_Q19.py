from math import *
height = int(input('Specify the height of the modular rectangle: '))
width = int(input('Specify the width of the modular rectangle: '))
num = 0
for i in range(height):
    for j in range(width): 
       print(num%10,end=' ')
       num+=1
    print('');