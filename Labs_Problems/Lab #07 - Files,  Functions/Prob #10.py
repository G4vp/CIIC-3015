# Write a function called ListReverse() which takes a list as its argument and duplicates the behavior of the reverse() list method without using it.
def ListReverse(x):
    asd = x[:]
    for i in range(len(x)):
        x[i] = asd[-i-1]