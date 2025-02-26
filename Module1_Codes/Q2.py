#declaring variables for user inputs
usrName = input("What is your name? ")
usrObject = input("What is the name of the object? ")
usrMass = eval(input("What is the mass of the object (in kg)? "))

if (usrMass >= 0):
    usrLoc = input("Where would you like to perform the calculation? ")
    if(usrLoc.lower() == 'e' or usrLoc.lower() == 'b'):
        # x-axis acceleration
        usrXAcc = input("Would you like to provide an acceleration for the x-axis? ")
        usrXAccVal = 0 #set default x acceleration to zero
        if(usrXAcc.lower() == 'y'):
            usrXAccVal = eval(input("Type in the acceleration for the x-axis (in metres per second squared)? "))

        # y-axis acceleration
        usrYAcc = input("Would you like to provide an acceleration for the y-axis? ")
        usrYAccVal = 0 #set default y acceleration to zero
        if(usrYAcc.lower() == 'y'):
            usrYAccVal = eval(input("Type in the acceleration for the y-axis (in metres per second squared)? "))
    
        # user outputs
        print('Welcome,',usrName,'!')
        usrZAccVal = 0
        if (usrLoc.lower() == 'e' or usrLoc.lower() == 'b'):
            if (usrLoc.lower() == 'e'): #calculating for Earth
                print('You have requested to perform the calculation for Earth.')
                usrZAccVal = 9.8 # setting the acceleration to 9.8 m/s2 for earth
            elif (usrLoc.lower() == 'b'): #calculating for Bylaw
                print('You have requested to perform the calculation for Bylaw.')
                usrZAccVal = 9.8 * 3 # setting the acceleration to 3x earth for bylaw, i.e., 29.4 m/s2

            #calculating the results
            forceX = round(usrMass * usrXAccVal,2)
            forceY = round(usrMass * usrYAccVal,2)
            forceZ = round(usrMass * usrZAccVal,2)
            print('Here are your results for',usrObject,'with a mass of',usrMass,'kgs:')
            print('\tFx =',forceX,'Newtons')
            print('\tFy =',forceY,'Newtons')
            print('\tFz =',forceZ,'Newtons')
    else: # error condition for world option
        print("That option is invalid!")
else:
    # error condition for non-positive mass
    print("You have entered a mass less than zero!")

'''
approx reading time: 10 minutes
approx coding time: 10 minutes
approx testing time: 5 minutes
approx total time: 25 minutes
'''