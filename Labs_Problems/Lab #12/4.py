#Write a recursive function called Min() which duplicates the behavior of Python's builtin min() without using it.



def Min(lst,m = None):
    if len(lst) > 0:
        if(m == None or lst[0] < m):
            m = lst[0]
        return Min(lst[1:],m)
    return m

