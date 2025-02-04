print("This program approximates the value of the square root of 5 starting from your initial guess.")
guess = eval(input("Enter your initial guess: "))
prev_approx = 0
approx = 1
print('============================================')

while ( abs(prev_approx - approx) >= 10**-10):
    prev_approx = approx
    numerator = guess + (5 / guess)
    denominator = 2
    approx = numerator / denominator
    guess = approx
    print('prev_approx: \t',prev_approx)
    print('numerator: \t',numerator)
    print('denominator: \t',denominator)
    print('approx: \t',approx)
    print('============================================')
print('The approximate value of the square root of 5 is',approx)