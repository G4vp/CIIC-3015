

# Write a function called Enumerate() which duplicates the behavior of Python's builtin enumerate() generator without using it.
def Enumerate(ls):
    for i in range(len(ls)):
        yield i,ls[i]