width = int(round(eval(input("How wide would you like the box to be? "))))
height = int(round(eval(input("How high would you like the box to be? "))))
for i in range(0, height):
    if(i == 0 or i == (height-1)):
        print('*'*width)
    else:
        print('*'+' '*(width-2)+'*')