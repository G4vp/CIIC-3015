# Write a function called IsLeapYear() which takes an integer as its only argument and returns True or False depending on whether the value of that integer corresponds to a leap year. The rule for determining this is as follows:

#  If a year is evenly divisible by 4, it is a leap year...

#  UNLESS it is also evenly divisible by 100, in which case it is not a leap year...

#  UNLESS it is also evenly divisible by 400, in which case it is a leap year.

# Perform your development in the following embedded Repl.it IDE, but copy your final code into the text area further below labeled "Answer".
def IsLeapYear(year):
    if ((year%4 == 0 and year%400 == 0 and year%100 == 0) or year%4 == 0):
        return True
    return False
    

print(IsLeapYear(2000))