#Write a recursive function called Max() which duplicates the behavior of Python's builtin max() without using it.
def Max(lst,m = None):
    if len(lst) > 0:
        if(m == None or lst[0] > m):
            m = lst[0]
        return Max(lst[1:],m)
    return m