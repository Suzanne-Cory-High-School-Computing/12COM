hour = eval(input('Enter hour: '))
if(1<=hour<=12):
    ampm = input('am (1) or pm (2) ? ')
    if (ampm=='1' or ampm=='2'):
        hoursplus = eval(input('How many hours ahead? '))
        newhour = (hour + hoursplus)%12
        if (ampm=='1'):
            newampm = 'pm'
        else:
            newampm = 'am'
        print('New hour: ',newhour,newampm)
    else:
        print('Invalid time.')
else:
    print('Invalid time.')
