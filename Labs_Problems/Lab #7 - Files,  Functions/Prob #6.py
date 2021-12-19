# Write a function called ListClear() which takes a list as its argument and duplicates the behavior of the clear() list method without using it.
def ListClear(z):
    for i in z[:]:
        z.remove(i)