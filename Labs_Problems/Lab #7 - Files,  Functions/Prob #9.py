# Write a function called ListIndex() which takes a list and a value as its arguments and duplicates the behavior of the index() list method without using it.
def ListIndex(x,y):
    for i in range(len(x)):
        if(y == x[i]):return i