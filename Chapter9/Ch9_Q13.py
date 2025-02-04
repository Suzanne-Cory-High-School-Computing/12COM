from random import randint

winsPlayerA = 0 # user
winsPlayerB = 0 # computer

computer = 0
playerA = ""
playerB = ""

while (winsPlayerA < 3 and winsPlayerB <3):
    user = input("Rock [R or r - default], Paper [P or p], or Scissors [S or s]? ")

    computer = randint(0,4) # 1 - rock, 2 - paper, 3 - scissors
    if (computer >= 3):
        playerB = "scissors"
    elif (computer >= 2):
        playerB = "paper"
    else:
        playerB = "rock"

    if (user == "p" or user == "P"):
        playerA = "paper"
    elif (user == "s" or user == "S"):
        playerA = "scissors"
    else:
        playerA = "rock"        

    print('Computer: ',playerB,'\t\t You: ',playerA)
    if (playerA == playerB):
        print("It's a tie, no point is awarded.")
    elif (playerA == "rock"):
        if (playerB == "paper"):
            winsPlayerB += 1
            print('Computer wins this round.')
        else: # scissors
            winsPlayerA += 1
            print('You win this round.')
    elif (playerA == "paper"):
        if (playerB == "rock"):
            winsPlayerA += 1
            print('You win this round.')
        else: # scissors
            winsPlayerB += 1
            print('Computer wins this round.')
    else: # scissors
        if (playerB == "rock"):
            winsPlayerB += 1
            print('Computer wins this round.')
        else: # paper
            winsPlayerA += 1
            print('You win this round.')

if (winsPlayerA  >= 3):
    print('You have won the game, the score is',winsPlayerA,'vs. ',winsPlayerB)
elif (winsPlayerB >= 3):
    print('The computer has won the game, the score is',winsPlayerB,'vs. ',winsPlayerA)
else:
    print('The final score is: You - ',winsPlayerA,'\tComputer - ',winsPlayerB)