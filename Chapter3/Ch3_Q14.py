from math import *
angle_deg = int(input('Enter angle in degrees: '))
angle_rad = radians(angle_deg)
print('This is equivalent to ',angle_rad)
print('The sine of ',angle_deg,'degrees is',round(sin(angle_rad),2))
