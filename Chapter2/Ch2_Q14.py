height = int(round(eval(input("How high would you like the diamond to be? "))))
middle = int(height/2)
if (middle * 2 == height): # even number
    print("Please enter an odd number.")
else:
    for i in range(0, height):
        if(i == middle):
            print('*'*height)
        elif(i < middle):
            print(' '*(middle-i)+'*'*(i*2+1))
        else:
            print(' '*(i-middle)+'*'*((height-i)*2-1))