from random import randint
correct = 0
for i in range(10):
    print('Question',i+1,' : ',end=' ')
    randnum1 = randint(0,10)
    randnum2 = randint(0,10)
    print(randnum1,'x',randnum2,end=' ')
    answer = eval(input("= "))
    if (answer == randnum1 * randnum2):
        print('Right!')
        correct += 1
    else:
        print('Wrong.  The answer is',randnum1*randnum2,'.')
print('Your score is',correct,'out of 10.')
if (correct >= 10):
    print('Excellent, you got a perfect score!')
elif (correct >= 8):
    print('Well done, you got High Distinction!')
elif (correct >= 7):
    print('Great, you have achieved a Distinction mark.')
elif (correct >= 6):
    print('You have achieved a Credit, keep going!')
elif (correct >=4):
    print('You have achieved a Pass, keep going!')
else:
    print('You have not yet achieved a Pass, keep on practicing!')