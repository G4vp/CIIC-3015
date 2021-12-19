# The dot product of two vectors is calculated by multiplying the corresponding elements of each vector together and summing those products. For example, the dot product of [2, 0, 1] and [6, 3, 4] = 2*6 + 0*3 + 1*4 = 12 + 0 + 4 = 16

# Write a function called Dot() which takes two lists as arguments and returns the dot product of those lists as a float. You may assume that both lists have equal length and contain only numeric values.

# Hint: Use a while-loop here, not a for-loop. (Why?)

# Also: We want you to roll your own loops here. Do not import a module like numpy to do the work for you.
def Dot(a,b):
    count = 0.0
    for i in range(len(a)):
        count += a[i]*b[i]
    return count