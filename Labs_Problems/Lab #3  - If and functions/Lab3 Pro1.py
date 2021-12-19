# Write a function called IsWithinEpsilon() which takes three numeric arguments and returns True or False depending on whether the distance between the first number and the second number is less than or equal to the third number. Your function should give identical results regardless of the order of the first two arguments.

# Perform your development in the following embedded Repl.it IDE, but copy your final code into the text area further below labeled "Answer".

def IsWithinEpsilon(a,b,c):
    if((abs(a-b)) <= c):
        return True
    return False

	

