from random import randint

money = 100
toss = ""
player = ""

while (0 < money < 200):    
    guess = input("Head [h or H - default] or Tail [t or T]: ")
    turn = randint(0,3)

    if (turn == 1): # head
        toss = "head"
    else: # tail
        toss = "tail"
    
    if (guess == "t" or guess == "T"):
        player = "tail"
    else:
        player = "head"

    if (player == toss):
        money += 9
        print('Correct.  You have won $9.')

    else:
        money -= 10
        print('Incorrect.  You have lost $10.')

if (money <= 0):
    print("Sorry, you have run out of money.")
else:
    print('Congratulations!  You have accumulated',money)