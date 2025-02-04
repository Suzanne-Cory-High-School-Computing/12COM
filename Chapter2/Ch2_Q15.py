height = int(round(eval(input("How large would you like the letter A to be? "))))
middle = int(height/2)
for i in range(0, height):
    if(i == middle):
        if (middle * 2 == height): # even number
            print(' '*(middle-1)+'*'*(height+1))
        else:
            print(' '*middle+'*'*height)
    elif(i ==0):
        print(' '*(height-i-1)+'*'+' '*(i*2-1))
    else:
        print(' '*(height-i-1)+'*'+' '*(i*2-1)+'*')