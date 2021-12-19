# Write a function called Sum() which duplicates the behavior of Python's builtin sum() without using it.
def Sum(ls):
    total = 0
    for i in ls:
        total += i
    return total