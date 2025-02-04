number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second number: "))

if (number1 < number2):
    smaller = number1
    larger = number2
elif (number1 > number2):
    smaller = number2
    larger = number1
else:
    smaller = larger = number1

while (smaller != 0):
    remainder = larger % smaller
    larger = smaller
    smaller = remainder

print('The GCD or greatest common divisor is: ',larger)