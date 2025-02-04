from math import *
number = eval(input('What is the number? '))
if(number==0):
    print('The number is not divisible by any number because it is zero.')
else:
    print('The number is divisible by:',end=' ')
    for i in range(1,abs(number)+1):
        if(abs(number)%i == 0):
            print(i,end=' ')