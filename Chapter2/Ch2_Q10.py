width = int(round(eval(input("How wide would you like the box to be? "))))
height = int(round(eval(input("How high would you like the box to be? "))))
for i in range(0, height):
    print('*'*width)