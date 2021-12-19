#Write a recursive function called ListCount() which takes a list and a value as its arguments and duplicates the behavior of the count() list method without using it.
def ListCount(text,val,c = 0):
    if len(text) > 0:
        if text[0] == val:
            c += 1
        return ListCount(text[1:],val,c)
    else:
        return c