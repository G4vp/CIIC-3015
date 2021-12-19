# The formula from converting from degrees Celsius to degrees Fahrenheit is: 

# F = (C * 9 / 5) + 32

# Write a program which asks the user for a temperature in degrees Celsius and print the equivalent temperature in degrees Fahrenheit. For this problem, both values should be ints. Specifically, the answer should be rounded to the nearest int. Note that this is not the same as merely dropping the decimal part of the value - for example, a result of 32.7 should be reported as a 33, not as a 32.

degreeC = int(input('Enter a temperature: '))
print(int(round((degreeC*9/5)+32,0)))