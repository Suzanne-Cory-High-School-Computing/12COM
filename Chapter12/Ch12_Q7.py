lines = [line.strip() for line in open('baseball.txt')]

for line in lines:
    entry = line.split('\t')
    name = entry[0]
    homerun = int(entry[6])
    stolenbase = int(entry[10])

    if (homerun >= 20 and stolenbase >= 20):
        print(line)