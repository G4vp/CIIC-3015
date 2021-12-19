# Write a function called Primes() which takes an int and returns a sorted list containing all prime numbers (as ints) which are less than that value.

# You are specifically required to implement an algorithm called the Sieve of Eratosthenes, which works as follows:

# 1) Let N be the value of the function argument. (You don't need to call your own variable N. This is merely for explanation purposes.)
# 2) Let S be a list of N bools. These represent potential primes. We have yet to eliminate any candidates so initially they are all set to True.
# 3) Let J be the current number that we wish to test for primality. Initially J=2.
# 4) Let P be the list of primes that we will be returning to the caller. Initially P is empty.
# 5) If J >= N then return P.
# 6) If S[J] is True then J is a prime number so do the following:
#         Append J to P
#         Set S[M] to False for all M that are multiples of J and less than N. (So for N=10 and J=2, set S[2], S[4], S[6], S[8] to False.)
# 7) Increment J by one and then go back to step 5.

# Note: Do not try to just blindly copy this algorithm exactly as it is written above line-by-line. Instead, understand how it all works and then translate that understanding into effective Python statements.

def Primes(n):
    S = [True]*n
    P = []
    for i in range(2,n):
        if(S[i]):
            P.append(i)
            for k in range(0,n,i):
                S[k] = False
    return(P)