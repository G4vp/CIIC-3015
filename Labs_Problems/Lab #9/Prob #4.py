# Write a generator function called Primes() which generates all prime numbers in increasing order.

# Hint: Don't try to use a Sieve of Eratosthenese here! A sieve is a poor fit for this problem because it requires an upper bound on the values of the primes that it finds.
def Primes():
    i = 2
    while(i):
        isNotPrime = 0
        for j in range(2,i):
            if i%j == 0:
                isNotPrime += 1
            if isNotPrime > 1:
                break
        if not(isNotPrime):
            yield i
        i+=1