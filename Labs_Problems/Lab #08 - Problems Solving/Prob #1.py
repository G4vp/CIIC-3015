# In Python (and also in quite a few other programming languages) a variable name may contain only letters, digits, or an underscore - and it may not have a digit as its first character. Write a function called IsValidVariableName() which takes a string as an argument and returns True or False depending on whether that string would be a valid name for a variable.

# Hint: The string methods isalpha() and isdigit() are your friends here.
def IsValidVariableName(s):
    if(len(s) == 0 or s[0].isdigit()): return False
    for i in s:
        if(not (i.isalpha() or i == '_' or i.isdigit())):
           return False
    return True