from math import *
number = eval(input("Enter an integer: "))
squarefree = 1
for i in range(2,number+1):
    square = i**2
    if(number%square == 0): # the square is a divisor
        print('The number',number,'is divisible by',square,'which is the square of',i)
        squarefree = 0
if (squarefree == 1):
    print('The number',number,'is squarefree.')
else:
    print('The number',number,'is not squarefree.')