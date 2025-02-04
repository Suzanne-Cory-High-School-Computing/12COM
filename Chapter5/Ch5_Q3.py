from math import *
value = eval(input('Enter a value n: '))
sum = 1
for i in range(2,value+1):
    sum += 1/i
print('The sum for the first term is',sum)
ln = log(value,e)
print('and ln of',value,'is',ln)
ans = sum - ln
print('The answer is',ans)