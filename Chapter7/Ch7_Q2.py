from random import randint

L = [] # initialising the list
for i in range(10):
    random = randint(1,100)
#    print('The random number is',random)
    L.append(random)

print('The list is: ',L)

#number of elements
print('The number of elements in the list is',len(L))

#average of the elements
print('The average of the elements in the list is',sum(L)/len(L))

#largest and smallest values
print('The largest value is',max(L))
print('The smallest value is',min(L))

#sorting the list to find the second largest and second smallest
tempList = L
tempList.sort()
print('The sorted list is',tempList)
print('The second largest value is',tempList[-2])
print('The second smallest value is',tempList[1])

#counting even numbers
countEven = 0
for i in range(len(L)):
    if (L[i]%2==0): #even numbers
        countEven += 1
print('The number of even numbers is',countEven)