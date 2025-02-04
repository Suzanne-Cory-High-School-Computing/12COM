from math import *
Y = int(input('Enter a year: '))
C = floor(Y / 100)
M = (15 + C - floor(C/4) - floor(((8*C)+13)/25))%30
N = (4 + C - floor(C/4))%7
A = Y % 4
B = Y % 7
C = Y % 19
D = ((19*C) + M)%30
E = (2*A + 4*B + 6*D + N) % 7
if (D==29 and E==6):
    print('Easter is April 19')
elif (D==28 and E==6 and 
      (M==2 or M==5 or M==10 or M==13 or M==16 or M==21 or M==24 or M==39)):
    print('Easter is April 18')
else:
    mardate = 22 + D + E
    aprdate = D + E - 9
    if (mardate > 31):
        print('Easter is April',aprdate)
    else:
        print('Easter is March',mardate)