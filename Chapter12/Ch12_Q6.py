lines = [line.strip() for line in open('namelist.txt')]
matchstring = "aeiou"

for line in lines:
    i = 0
    matchsuccess = 0
    for letter in range(0,len(line)):
        lettertomatch = matchstring[i%5]
#        print('Current letter: ',line[letter].lower(),'Letter to match: ',lettertomatch)
        if (line[letter].lower() == lettertomatch):
#            print(lettertomatch,'has been found.')
            i+=1
            if (i==5):
#                print('Matchsuccess!')
                matchsuccess = 1
    if(matchsuccess == 1):
        print(line)