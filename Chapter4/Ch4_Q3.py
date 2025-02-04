from math import *
tempC = eval(input('Enter a temperature in Celsius: '))
if (tempC < -273.15):
    print('Temperature is invalid; below absolute zero.')
elif (tempC == -273.15):
    print('Temperature is absolute zero.')
elif (-273.15 < tempC < 0):
    print('Temperature is below freezing.')
elif (tempC == 0):
    print('Temperature is at the freezing point.')
elif (0 < tempC < 100):
    print('Temperature is in the normal range.')
elif (tempC == 100):
    print('Temperature is at the boiling point.')
else: #anything above 100
    print('Temperature is above the boiling point.')