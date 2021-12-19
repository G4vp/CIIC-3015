# Write a function called FromRoman() which takes a string representing a valid Roman numeral less than 4000 in standard form and returns its value as an int. The behavior for inputs which are not valid Roman numerals is undefined so those may simply be ignored.

# Do not implement this as a single enormous lookup table. Parse the input string character-by-character with a for-loop.

# Hint: Don't try to solve this entire problem at once. First, solve for just the letter 'I'. Once that is working, add 'V'. Then 'X'. And so on. Look for common patterns to keep your code nice and simple.

# Reference: https://en.wikipedia.org/wiki/Roman_numerals

def FromRoman(n):
    conversion = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    count = 0
    for i in range(len(n)):
        if(conversion.get(n[i-1]) < conversion.get(n[i]) and i != 0):
            count -= (conversion.get(n[i-1])*2)
        count += conversion.get(n[i])
    return count