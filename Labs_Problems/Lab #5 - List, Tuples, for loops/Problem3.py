# Write a function called Factors() which takes an int and returns a sorted list containing all of the prime factors (as ints) for that value.
# In general, any given prime factor may appear more than once. For example, 2*2*3 == 12 so the output for 12 would be [2, 2, 3].

# Hint: It sure would be useful to have a helper function which could generate a list of all prime numbers below a certain value!


def Factors(n):
    i = 2
    s = []
    while(i <= n):
        if(n%i == 0):
            n = n//i
            s.append(i)
            i = 1
        i += 1
    return(s)

