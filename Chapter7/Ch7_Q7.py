L = eval(input('Enter your first list: '))
M = eval(input('Enter your second list: '))
SUM = L

lenL = len(L)
lenM = len(M)
if(lenL == lenM):
    for i in range(lenL):
        SUM[i] = L[i] + M[i]
    print('The sum of the two lists is',SUM)
else:
    print("The length of the two lists don't match.  Please try again.")