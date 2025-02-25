number = eval(input('Enter an integer: '))
factors = []

for i in range(1,number):
    if (number%i == 0): #this is a factor
        factor1 = number
        factor2 = i

        #check first if the factors are already in there before adding them
        if factor1 not in factors:
            factors.append(factor1)
        if factor2 not in factors:
            factors.append(factor2)

factors.sort()
print('The list of sorted factors is',factors)