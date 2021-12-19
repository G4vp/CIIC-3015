# Write a function called StrSplit() which takes two arguments, a string and a separator, and duplicates the behavior of the builtin split() string method without using it.
def StrSplit(text,sep):
    ls = list()
    asd = ''
    i = 0
    while(i < len(text[:])):
        if(i == text.find(sep,i)):
            ls.append(asd)
            i += len(sep)-1
            asd = ''
        else:
            asd += text[i]
        i += 1
    ls.append(asd)
    return ls