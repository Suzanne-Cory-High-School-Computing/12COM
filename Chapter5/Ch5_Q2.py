from random import randint
count4 = 0
count9 = 0
square = 0
for i in range(1,101):
    square = i**2
    if(square%10==4):
        count4 += 1
        print('The number',i,'squared is',square,'which ends in 4.')
    elif(square%10==9):
        count9 += 1
        print('The number',i,'squared is',square,'which ends in 9.')
print('There are',count4,'numbers from 1 to 100 whose squares end in 4.')
print('There are',count9,'numbers from 1 to 100 whose squares end in 9.')