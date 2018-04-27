##PG 57
##Implement a program that requests the current temperature
##in degrees Fahrenheit from the user
##and prints the temperature in degrees Celsius using the formula
##celsius = 5/9 (fahrenheit − 32)
## (Perkovic 57)

Far = eval(input('enter the temperature in degrees Fahrenheit: '))
Cels = (5/9)*(Far - 32)
print('The temperature in degrees Celsius is', round(Cels,2))
