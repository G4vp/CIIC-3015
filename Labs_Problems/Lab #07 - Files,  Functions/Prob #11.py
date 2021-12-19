# Write a function called StrJoin() which takes two arguments, a string and an iterable, and duplicates the behavior of the builtin join() string method without using it
def StrJoin(s,ls):
    j = ''
    for i in range(len(ls)):
        if i == len(ls) - 1:
            j += ls[i]
        else:
            j += ls[i] + s
    return j