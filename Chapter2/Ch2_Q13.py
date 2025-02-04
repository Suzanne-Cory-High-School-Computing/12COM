height = int(round(eval(input("How high would you like the triangle to be? "))))
for i in range(1, height+1):
    print('*'*(height-i+1))