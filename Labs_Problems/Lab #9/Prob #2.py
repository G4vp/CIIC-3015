# Write a function called CommonCharacters() which takes two strings and returns the number of distinct characters which appear at least once in both strings.
def CommonCharacters(str1,str2):
    str1 = set(str1)
    str2 = set(str2)
    return len(str1.intersection(str2))