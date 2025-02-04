lines = [line.strip() for line in open('grades.txt')]
print(lines)
count = 0
for line in lines:
    entry = line.split(' ')
    name = entry[0]
    score1 = entry[1]
    score2 = entry[2]
    score3 = entry[3]
    if (int(score1) >= 40 and int(score2) >= 40 and int(score3) >= 40):
        print(name,'passed all three tests with the following scores:',score1,score2,score3)
        count += 1