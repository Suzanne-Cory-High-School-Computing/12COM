from math import *

usrXVal = eval(input('Enter the value for the x-axis: '))
usrYVal = eval(input('Enter the value for the y-axis: '))
usrCalcOption = input('Select whether to calculate the force [f - default] or acceleration [a]: ')
resultantVal = sqrt(usrXVal**2 + usrYVal**2)
if (usrCalcOption.lower() == 'a'): #calculate the resultant acceleration
    print('The resultant acceleration vector is a =',round(resultantVal,2),'metres per second squared')    
else: #calculate the resultant force
    print('The resultant force vector is F =',round(resultantVal,2),'Newtons')

'''
approx reading time: 5 minutes
approx coding time: 5 minutes
approx testing time: 5 minutes
approx total time: 15 minutes
'''