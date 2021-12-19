# Write a function called UniqueCapitalLetters() which takes a string and returns the number of different capital letters which appear in that string.
def UniqueCapitalLetters(string):
    newStr = set(string)
    total = 0
    for i in newStr:
        if i.isupper():
            total += 1
    return total