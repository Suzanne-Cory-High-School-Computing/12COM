L = eval(input('Enter a list:'))
print('Your list is',L)
print('The number of items in the list is',len(L))
print('The last item in the list is',L[-1])

#creating a new list to reverse
Lnew = L
Lnew.reverse()
print('The list in reverse order is',Lnew)

#checking the items on the list
flag5 = 0 #initial flag for 5 not found
numberToFind = 5 #setting the number to find
count5 = 0 #number of times the number 5 is found
for i in range(len(L)):
    if (L[i]==numberToFind):
        flag5 = 1 #list contains the number 5
        count5 += 1

#printing whether 5 is found
print('Does the list contain the number',numberToFind,'?',end=" ")
if (flag5 == 1):
    print("Yes")
else:
    print("No")

#printing the number of 5 found
print('The number',numberToFind,'has been found',count5,'times.',end=" ")

#removing the first and last items on the list
del L[0]
del L[-1]
print('\nThe new list is now',L)
L.sort()
print('The sorted list is',L)

countLessThan5 = 0 #number of integers less than 5 in the current list
#going through the list again to count integers less than 5
for i in range(len(L)):
    if(L[i] < numberToFind):
        countLessThan5 += 1
print('The number of integers less than the number',numberToFind,'is',countLessThan5)
    