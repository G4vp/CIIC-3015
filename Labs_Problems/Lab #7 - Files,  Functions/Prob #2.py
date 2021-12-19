# Write a function called Max() which duplicates the behavior of Python's builtin max() without using it.
def Max(ls):
    Mls = ls[0]
    for i in ls:
        if Mls < i:
            Mls = i

    return Mls