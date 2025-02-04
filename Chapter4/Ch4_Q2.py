from math import *
temp = eval(input('Enter the temperature: '))
celsiusFahrenheit = input('Is this temperature in Celsius or Fahrenheit? ')
if (celsiusFahrenheit == 'Celsius' or celsiusFahrenheit == 'celsius' or celsiusFahrenheit == 'c' or celsiusFahrenheit == 'C'):
    print(temp,'Celsius is equivalent to',((9/5)*temp)+32,'Fahrenheit.')
elif (celsiusFahrenheit == 'Fahrenheit' or celsiusFahrenheit == 'fahrenheit' or celsiusFahrenheit == 'f' or celsiusFahrenheit == 'F'):
    print(temp,'Fahrenheit is equivalent to',(5/9)*(temp-32),'Celsius.')
else:
    print('Cannot convert the temperature, please check your answers.')