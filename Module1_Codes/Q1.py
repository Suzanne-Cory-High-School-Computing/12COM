#declaring variables for user inputs
usrName = input("What is your name? ")
usrObject = input("What is the name of the object? ")
usrMass = eval(input("What is the mass of the object (in kg)? "))

#normal conditions, where mass is a positive value
if(usrMass >= 0):
    usrCalc = input("Select what calculation you would like to perform: ")
    #user has selected to calculate x direction through 'X' or 'x'
    if(usrCalc.lower() == 'x'):
        print('Welcome,',usrName,'!')
        print('You have requested to calculate only the x-direction.')
        print('Here is your result for',usrObject,'with a mass of',usrMass,'kgs:')
        print('Fx =',usrMass*9.8,'Newtons')
    #user has selected to calculate y direction through 'Y' or 'y'
    elif(usrCalc.lower() == 'y'):
        print('Welcome,',usrName,'!')
        print('You have requested to calculate only the y-direction.')
        print('Here is your result for',usrObject,'with a mass of',usrMass,'kgs:')
        print('Fy =',usrMass*9.8,'Newtons')
    #user has selected to calculate z direction through 'Z' or 'z'
    elif(usrCalc.lower() == 'z'):
        print('Welcome,',usrName,'!')
        print('You have requested to calculate only the z-direction.')
        print('Here is your result for',usrObject,'with a mass of',usrMass,'kgs:')
        print('Fz =',usrMass*9.8,'Newtons')
    #user has selected to calculate all directions through 'A' or 'a'
    elif(usrCalc.lower() == 'a'):
        print('Welcome,',usrName,'!')
        print('You have requested to calculate all directions.')
        print('Here are your results for',usrObject,'with a mass of',usrMass,'kgs:')
        print('Fx =',round(usrMass*9.8,2),'Newtons\tFy =',round(usrMass*9.8,2),'Newtons\tFz =',round(usrMass*9.8,2),'Newtons')
    else:
        print("That option is invalid!")
#error condition for non-positive mass
else:
    print("You have entered a mass less than zero!")

'''
approx reading time: 10 minutes
approx coding time: 10 minutes
approx testing time: 5 minutes
approx total time: 25 minutes
'''