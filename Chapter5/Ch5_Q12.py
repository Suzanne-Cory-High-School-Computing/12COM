from random import randint
from math import *
points = 0
for i in range(5):
    randnum = randint(1,10)
    guess = eval(input('Enter your guess: '))
    print('The number to guess is',randnum,'and your guess is',guess)
    if (randnum == guess):
        print('Correct.  You have gained 10 points!')
        points += 10
    else:
        print('Incorrect.  You have lost 1 point.')
        points -= 1
print('Your score is',points)
