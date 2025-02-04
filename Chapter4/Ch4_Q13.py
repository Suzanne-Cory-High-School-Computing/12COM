from random import randint
print('Welcome to Rock-Paper-Scissors.  There are five rounds in this game.')
playerscore = 0
computerscore = 0
for i in range(5):
    computer = randint(0,4)
    # 1 - rock
    # 2 - paper
    # 3 - scissors
    print('Round',i+1,'!')
    player = input('Do you want [R]ock [P]aper or [S]cissors? ')
    if (player=='R' or player=='r'):
        if (computer==3):
            print('Computer picked scissors.  You have won this round!')
            playerscore += 1
        elif (computer==2):
            print('Computer picked paper.  You have lost this round.')
            computerscore += 1
        else:
            print('Computer picked rock.  Neither of you has won this round.')
    elif (player=='P' or player=='p'):
        if (computer==3):
            print('Computer picked scissors.  You have lost this round.')
            computerscore += 1
        elif (computer==2):
            print('Computer picked paper.  Neither of you has won this round.')
        else:
            print('Computer picked rock.  You have won this round!')
            playerscore += 1
    elif (player=='S' or player=='s'):
        if (computer==3):
            print('Computer picked scissors, neither of you has won this round.')
        elif (computer==2):
            print('Computer picked paper.  You have won this round!')
            playerscore += 1
        else:
            print('Computer picked rock.  You have lost this round.')
            computerscore += 1
    else:
        print('Invalid turn, you lost this round.')
        computerscore += 1

if(playerscore==computerscore):
    print("You and the computer have both won',playerscore,'rounds.  It's a tie!")
elif(playerscore<computerscore):
    print('You have lost to the computer.  The score is',playerscore,'-',computerscore)
else:
    print('You have won against the computer.  The score is',playerscore,'-',computerscore)