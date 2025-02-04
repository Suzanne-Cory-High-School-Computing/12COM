from random import randint
for i in range(1,51):
    print('Generating random numbers between 1 and', i+1)
    x = randint(1, i+1)
    print(x)