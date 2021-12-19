# The Python print() function assembles all of its arguments into a single string which it then sends to stdout (usually just the console window). Write a function called AlmostPrint() which accepts arguments like print() does (including the optional sep= keyword but not end=), assembles them into a string, and then returns that string to the caller.

def AlmostPrint(*a,sep =' '):
    asd = ''
    for i in range(len(a)):
        if i < len(a)-1:
            asd += str(a[i]) + sep
        else:
            asd += str(a[i])
    return asd