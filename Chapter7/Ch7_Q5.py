L = eval(input('Enter a list of strings: '))

print('Your list is ',L)

#removing first characters
for i in range(len(L)):
    currWord = L[i]
    wordLen = len(currWord) # length of current word
    print('The current string is',currWord,'with length',wordLen)
    newWord = currWord[1:wordLen]
    print('The new word is',newWord)
    L[i] = newWord

print('The new list is',L)