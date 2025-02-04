word = input("Type in a word: ")
print('The length of word',word,'is',len(word))
print('Printing one character per line...')
i = 0
while (i < len(word)):
    print(word[i])
    i += 1
print('Printing every second character...')
i = 0
while (i < len(word)):
    if (i % 2 == 1):    # print only 2nd, 4th, 6th, etc charactere
        print(word[i])
    i += 1