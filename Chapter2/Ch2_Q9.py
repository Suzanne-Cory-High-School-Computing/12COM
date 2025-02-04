printNum=int(round(eval(input("How many Fibonacci numbers would you like to print? "))))
prevFib = 1
currFib = 1
nextFib = 0
if (printNum == 1):
    print(prevFib)
elif (printNum == 2):
    print(prevFib," ",currFib)
else:
    print(prevFib, currFib, end=" ")
    for i in range(2,printNum):
        nextFib = prevFib + currFib
        prevFib = currFib
        currFib = nextFib
        print(currFib, end=" ")