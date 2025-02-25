L = [] #initial list
#incrementing integers and adding to a list
for i in range(50):
    L.append(i)
print('The list of integers is',L)

L2 = [] #initial list
#incrementing integers and squaring
for i in range(1,51):
    L2.append(i**2)
print('The list of squares of the integers is',L2)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

L3 = []
for i in range(26):
    newWord = alphabet[i]*(i+1)
    print('The new word is',newWord)
    L3.append(newWord)
print('The list is',L3)