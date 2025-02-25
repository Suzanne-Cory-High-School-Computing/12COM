L = [8,9,10]

print('The starting list is',L)

#setting the second entry to 17
L[1] = 17
print('After changing the second entry, the new list is',L)

#adding entries
L.append(4)
L.append(5)
L.append(6)
print('After adding entries, the new list is',L)

#removing entries
del L[0]
print('After removing the first entry, the new list is',L)

#sorting entries
L.sort()
print('The sorted list is',L)

#doubling entries
L += L
print('After doubling, the new list is',L)

#insert at index
L.insert(3,25)
print('After inserting at index 3, the new list is',L)