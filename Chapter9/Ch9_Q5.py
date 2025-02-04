score = eval(input("Enter a test score: "))
above90 = 0
total = 0
numscores = 0
while (score >= 0):
    total += score
    numscores += 1
    if (score >= 90):
        above90 += 1
    score = eval(input("Enter a test score: "))
print('Number of scores above 90: ',above90)
print('Average score: ',total/numscores)