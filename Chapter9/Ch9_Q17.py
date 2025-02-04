numerator = eval(input("Enter the numerator of a proper fraction: "))
denominator = eval(input("Enter the denominator of a proper fraction: "))
digit = eval(input("What digit would you like to know? "))

orignum = numerator
origdenom = denominator

i = 1
numerator *= 10
ans = "0."

while (i <= digit):
    quotient = numerator // denominator
    print(numerator,'divided by',denominator,'is',quotient)
    numerator -= quotient * denominator
    numerator *= 10
    print('The new numerator will be',numerator)
    print('Digit ',i,'is',quotient)
    i += 1
    ans += str(quotient)

print('The first',digit,'digits of the proper fraction',orignum,'/',origdenom,'are',ans)