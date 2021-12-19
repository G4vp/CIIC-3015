# Write a function called ListCopy() which takes a list as its argument and duplicates the behavior of the copy() list method without using it.
def ListCopy(x):
    ls = []
    for i in x:
        ls.append(i)
    return ls