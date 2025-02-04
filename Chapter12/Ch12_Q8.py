lines = [line.strip() for line in open('ncaascores.txt')]
numgames = 0
total = 0

# PROBLEM A
for line in lines:
    entry = line.split(',')
#    print(entry)
    total += int(entry[2])
    total += int(entry[4])
    numgames += 2

print('The total points for',numgames,'games is',total,'points.')
print('The average is',total/numgames)

# PROBLEM B
gameswon = 0
gameslost = 0
myteam = input('Pick your team [TeamA, TeamB, TeamC]: ')
for line in lines:
    entry = line.split(',')
    team1 = entry[1]
    team2 = entry[3]
    played = 0
    if (myteam == team1):
        myteamscore = int(entry[2])
        otherteamscore = int(entry[4])
        played = 1
    elif (myteam == team2):
        myteamscore = int(entry[4])
        otherteamscore = int(entry[2])
        played = 1

    if played == 1:
        if (myteamscore > otherteamscore):
            gameswon += 1
        else:
            gameslost += 1

print('Your team',myteam,'has won',gameswon,'games and lost',gameslost,'games.')