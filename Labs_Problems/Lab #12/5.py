#Write a recursive function called Sum() which duplicates the behavior of Python's builtin sum() without using it.
def Sum(lst,s = 0):
    if len(lst) > 0:
        s += lst[0]
        return Sum(lst[1:],s)
    return s