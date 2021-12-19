# We define the Collatz function, C(N), for any positive integer N to be the following:

#         if N is even, C(N) = N/2

#         if N is odd, C(N) = 3*N + 1

# We define the Collatz sequence for any positive integer N to be the following:

#         The first element in the sequence is N

#  All subsequent elements are the result of calling the Collatz function on the value of the previous element.

# So, the Collatz sequence for 3 would be 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, ...

# Notice that the sequence eventually loops forever at 4,2,1. The (unproven) Collatz conjecture famously asserts that the Collatz sequence will eventually converge to 1 for all positive integers. To date this has been shown to be true for all integers up to 295,147,905,179,352,825,856

# Write a function called Collatz() which takes a positive integer N and returns the number of times the Collatz function must be invoked in sequence, starting with N, until the result reaches a value of 1.

# Perform your development in the following embedded Repl.it IDE, but copy your final code into the text area further below labeled "Answer".

def Collatz(a):
    total = 0
    while(a > 1):
        if(a%2 == 0):
            a = a//2
        else:
            a = 3*a+1   
        total += 1
    return total
print(Collatz(931386509544713451))