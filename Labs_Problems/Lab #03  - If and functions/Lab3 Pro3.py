# This is a variation of an infamous tech interview question. Write a function called FizzBuzz() which takes an integer argument. If that integer is evenly divisible by 3, return the string "Fizz". If that integer is evenly divisible by 5, return the string "Buzz". And if the integer is evenly divisible by both 3 and 5, return the string "FizzBuzz". Otherwise just return the integer.

# Note: This problem is all over the internet. It would take you three seconds to look up a solution. Please don't, this is a good test of your ability to think logically with conditionals.

# Perform your development in the following embedded Repl.it IDE, but copy your final code into the text area further below labeled "Answer".

def FizzBuzz(a):
    if(a%3 == 0 and a%5 == 0):return 'FizzBuzz'
    elif(a%3 == 0):return 'Fizz'
    elif(a%5 == 0):return 'Buzz'
    return a
