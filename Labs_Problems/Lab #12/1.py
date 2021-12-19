# Write a recursive function called NumVowels() which takes a single string as an input argument and returns the total number of characters in that string which are vowels. Which is to say, the number which are equal to 'a' or 'e' or 'i' or 'o' or 'u' (in either uppercase or lowercase). The returned value should be an integer.
def NumVowels(text,c = 0):
    if len(text) > 0 :  
        if text[0].lower() in ['a','e','i','o','u']:
            c += 1
        return NumVowels(text[1:],c)
    else:
        return c  