L = eval(input('Enter a list containing numbers between 1 and 12: '))
print('The list you entered is',L)

#replacing entries greater than 10
for i in range(len(L)):
    if (L[i] > 10):
        L[i] = 10

print('After replacing, the new list is',L)