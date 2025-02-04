from random import randint
for i in range(10):
    print('Question',i+1,' : ',end=' ')
    randnum1 = randint(0,10)
    randnum2 = randint(0,10)
    print(randnum1,'x',randnum2,end=' ')
    answer = eval(input("= "))
    if (answer == randnum1 * randnum2):
        print('Right!')
    else:
        print('Wrong.  The answer is',randnum1*randnum2,'.')