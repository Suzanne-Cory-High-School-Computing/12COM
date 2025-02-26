usrResistance = eval(input("What is the resistance, R, of the water against the boat's motion (in Newtons)? "))
usrNumPropellers = eval(input("How many propellers would you like to have on your boat? "))
usrThrust = eval(input("What is the thrust, T, of each propeller (in Newtons)? "))
usrOption = input("Would you like to provide the mass [m] or the acceleration [a] of the boat? ")

if (usrOption.lower() == 'm' or usrOption.lower() == 'a'):
    if (usrOption.lower() == 'm'): # user has opted to provide masss
        usrMassVal = eval(input("What is the mass of the boat (in kilograms)? "))
        if (usrMassVal >= 0): # we can process the value because it is positive
            # acknowledge all user inputs
            usrErrorNotify = input("Would you like to set your error notification to True [t - default] or False [f]? ")
            print('You have provided the resistance of the water R of',usrResistance,'Newtons against the boat.')
            print('You have equipped your boat with',usrNumPropellers,'propellers.')
            print('You have provided a thrust T of',usrThrust,'Newtons for each propeller.')
            print('You have provided the mass of the boat as',usrMassVal,'kilograms.')
            # default for error notifications is true
            if (usrErrorNotify.lower() == 'f'):
                errorOn = 0
                print('Your warning notification setting is set to False.')
            else:
                errorOn = 1
                print('Your warning notification setting is set to True.')

            # calculate the acceleration
            print("Here are your results:")
            totalThrust = usrThrust * usrNumPropellers
            sumF = totalThrust - usrResistance
            acceleration = sumF / usrMassVal
            print('Total thrust, T =',round(totalThrust,2),'Newtons obtained using',usrNumPropellers,'propellers of thrust',usrThrust,'Newtons per propeller')
            print('Acceleration of the boat, a =',round(acceleration,2),'metres per second squared')
            if (acceleration < 0 and errorOn == 1):
                print('Warning: Your boat has negative acceleration.  Please recheck your inputs and try again.')
        else:
            print("You have entered a mass less than zero!")

    elif (usrOption.lower() == 'a'): # user has opted to provide acceleration
        usrAccVal = eval(input("What is the acceleration of the boat (in metres per second squared)? "))
        if (usrAccVal >= 0): # we can process the value because it is positive
            usrErrorNotify = input("Would you like to set your error notification to True [t - default] or False [f]? ")
            # acknowledge all user inputs
            print('You have provided the resistance of the water R of',usrResistance,'Newtons against the boat.')
            print('You have equipped your boat with',usrNumPropellers,'propellers.')
            print('You have provided a thrust T of',usrThrust,'Newtons for each propeller.')
            print('You have provided the acceleration of the boat as',usrAccVal,'metres per second squared.')
            # default for error notifications is true
            if (usrErrorNotify.lower() == 'f'):
                errorOn = 0
                print('Your warning notification setting is set to False.')
            else:
                errorOn = 1
                print('Your warning notification setting is set to True.')

            # calculate the mass
            print("Here are your results:")
            totalThrust = usrThrust * usrNumPropellers
            sumF = totalThrust - usrResistance
            mass = sumF / usrAccVal
            print('Total thrust, T =',round(totalThrust,2),'Newtons obtained using',usrNumPropellers,'propellers of thrust',usrThrust,'Newtons per propeller')
            print('Mass of the boat, m =',round(mass,2),'kilograms')
            if (mass < 0 and errorOn == 1):
                print('Warning: Your boat has negative mass.  Please recheck your inputs and try again.')

        else:
            print("You have entered an acceleration less than zero!")
else:
    #error condition where user does not select mass or acceleration
    print("That option is invalid!")

'''
approx reading time: 10 minutes
approx coding time: 15 minutes
approx testing time: 10 minutes
approx total time: 35 minutes
'''