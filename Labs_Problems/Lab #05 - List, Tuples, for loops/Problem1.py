# The Fibonacci sequence is defined as follows:

#         F[0] = 0
#         F[1] = 1

#         For N>1, F[N] = F[N-1] + F[N-2]

# Which is to say, each element in the sequence is equal to the sum of the previous two elements in the sequence.
# The first twelve elements in the sequence are therefore: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# Write a function called Fib() which takes an int N and returns F[N].

# This is one of the most famous functions in all of Computer Science. So on one hand that means that there are hundreds if not thousands of examples of it to be found online. On the other hand, it is famous for good reasons - it is a simple example of a pattern that you will be seeing over and over again. Do not cheat yourselves out of the opportunity of solving this problem on your own. At the end of this lab, every one of you should be able to instantly crank out a perfect Fib() upon request.

def Fib(N):
    F = [0,1]
    for i in range(1,N):
        F.append(F[i-1]+F[i])
    return F