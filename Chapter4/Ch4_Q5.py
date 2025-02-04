from random import randint
guess = eval(input('Guess the random number between 1 and 10: '))
randNum = randint(1,10)
if (guess == randNum):
    print('Your guess is correct! The number is',randNum)
else:
    print('You guessed',guess,'but the number is',randNum,'. Thanks for playing!')