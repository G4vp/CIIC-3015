# Write a function called NumVowels() which takes a single string as an input argument and returns the total number of characters in that string which are vowels. Which is to say, the number which are equal to 'a' or 'e' or 'i' or 'o' or 'u' (in either uppercase or lowercase). The returned value should be an integer.
def NumVowels(word):
    count = 0
    for c in word.lower():
        if(c in ['a','e','i','o','u']):
            count += 1
    return count
