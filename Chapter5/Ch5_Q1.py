from random import randint
count = 0
square = 0
for i in range(1,101):
    square = i**2
    if (square%10 == 1):
        count += 1
        print('The number',i,'squared is',square,'which ends in 1.')
print('There are',count,'numbers from 1 to 100 whose squares end in 1.')