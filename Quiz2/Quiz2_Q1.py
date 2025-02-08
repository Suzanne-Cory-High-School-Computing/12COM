selectFile = input('Which of the files would you like to process: plain [p - default], tab-delimited [t] or comma-delimited [c]? ')

# set default processing
fileName = "inputfile_plain.txt" # default file
betweenChars = " "
newFileName = "inputfile_plain_withcounts.txt"

if (selectFile.lower() == 't'): # process tab delimited
    fileName = "inputfile_tab.txt" 
    betweenChars = "\t"
    newFileName = "inputfile_tab_withcounts.txt"
elif (selectFile.lower() == 'c'): # process comma delimited
    fileName = "inputfile_comma.txt" 
    betweenChars = ","
    newFileName = "inputfile_comma_withcounts.txt"

print(f'Processing the file {fileName}')
issueWarning = 0 # initialise flag for word count length

lines = [line.strip() for line in open(fileName)]
f = open(newFileName, 'w')
for line in lines:
    entry = line.split(betweenChars)
#    print('The current line is',entry)
    lineChar = entry[0]
    lineWord = entry[-1]
    lineWordCnt = len(lineWord)
#    print('Processing: ',lineChar, lineWord)
#    print('Separated by: ',betweenChars)
#    print('Word count: ',lineWordCnt)
#    print('Writing to file',{newFileName})

    # writing to the new file with _counts.txt
    print(f'{lineChar}{betweenChars}{lineWord}{betweenChars}{lineWordCnt}',file=f)

    # running a check for word lengths
    if (lineWordCnt > 30):
        issueWarning = 1 # set flag for word count length

print(f'The new file has been written to {newFileName}')
if(issueWarning == 1):
    print('Warning: A word exceeds 30 characters.')