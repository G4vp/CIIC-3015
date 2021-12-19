# Write a function called IsSorted() which takes a list as a parameter and returns True if all of the elements in that list are in sorted order, False if they are not. The elements in the list may be of any type. Two sequential values (a,b) are defined to be in sorted order if and only if a <= b.
def IsSorted(n):
    a = n.copy()
    a.sort()
    return a == n
    