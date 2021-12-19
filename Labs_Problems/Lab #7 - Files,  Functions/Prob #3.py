# Write a function called Min() which duplicates the behavior of Python's builtin min() without using it.
def Min(ls):
    Mls = ls[0]
    for i in ls:
        if Mls > i:
            Mls = i

    return Mls