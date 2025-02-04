lines = [line.strip() for line in open('class_scores.txt')]
f = open('scores2.txt', 'w')
for line in lines:
    entry = line.split(' ')
    name = entry[0]
    score = entry[-1]
    newscore = int(entry[-1])+5
    print(name,'current score is',score,'points, increased to',newscore,'points')
    print(name,newscore,file=f)