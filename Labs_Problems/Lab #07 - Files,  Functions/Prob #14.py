# Write a function called Range() which duplicates the behavior of Python's builtin range() generator without using it.
def Range(start = 0,end = -1,suma = 1):
    if(end < 0):
        end = start
        start = 0
    while((suma > 0 and start < end) or (suma < 0 and start > end)):
        yield start
        start += suma