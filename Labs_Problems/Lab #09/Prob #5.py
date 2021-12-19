# Any integer > 1 may be expressed as a product of prime numbers. Sometimes, the same prime number appears as a factor more than once. For example, 24 = 2*2*2*3.  So, 24 has four prime factors but only two unique prime factors. Similarly, 7 has one unique prime factor (itself) and 84 (=2*2*3*7) has three unique prime factors.

# Write a function called CountUniquePrimeFactors() which takes a positive integer > 1 as an argument and returns the number of unique prime factors for that integer. Your function must call the Primes() generator that you wrote earlier in this lab.
import math

def Primes():
    i = 2
    while(True):
        times = 0
        for j in range(2,i+1):
            if i%j == 0:
                times += 1
            if times > 2:
                break
        if(times < 2):
            yield i
        i+=1
def CountUniquePrimeFactors(n):
    count = 0
    for i in Primes():
        sq = math.sqrt(n)
        if i > sq: break
        if n%i == 0:
            count += 1
    if(count == 0): return 1 #If the count is 0 means that the number is Prime so we just return 1
    return count