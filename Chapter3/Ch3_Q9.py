from math import *
hour = int(input('Enter hour: '))
ahead = int(input('How many hours ahead? '))
print("New hour: ",(hour+ahead)%12,"o'clock")