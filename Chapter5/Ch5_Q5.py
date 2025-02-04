from math import *
number = eval(input("Enter a number: "))
sum = 0
for i in range (1,number+1):
    if (number%i==0):
        print(i,'is a divisor of the number',number)
        sum += i
print('The sum of the divisors of',number,'is',sum)