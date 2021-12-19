# Run Length Encoding is a simple, lossless compression technique. For this lab we will be focusing only on strings, but in general RLE can also be used on other types of data. The idea behind RLE is to count the number of times the same value (in this case, characters) appears in sequence. Once we have our count, we output the repetition count of that character (as a character) followed by the character itself. Examples:

#     'A' -> '1A'
#     'AbbbC' -> '1A3b1C'
#     'aaaAAABBBBBBBB' -> '3a3A8B'
#     'ZZZZZZZZZZZZZZZZ' -> '9Z7Z'

# Note what is happening in the last example above: In this very simple algorithm we cannot directly encode a run with a length above nine because we cannot express values greater than nine with a single numeric digit. (We could extend our algorithm to interpret non-numeric characters for additional range but we are deliberately keeping things simple here.) So, a sequence of twelve 'A' characters could not be represented as '12A' because the decoder would see the leading '1' and then try to output a single '2'. Instead, for any run longer than nine, we just output encoded sequences of length nine until the entire run has been encoded in pieces.

# Write a function called RLE() which takes a string, encodes it using the run length encoding technique described above, and returns the encoded version of that string.

# Hint: I recently wrote a function in class (named after a certain brand of canned meat) which is coincidentally quite similar to what is needed here. You have my permission to use that function as a starting point for derivative work.


def RLE(text):
    text = list(text)
    new_text = ''
    k = 9
    for i in text:
        if(text.count(i) > 9):
            new_text += (f'{9}{i}')
            for j in range(k):
                text.remove(i)
        if not(i in new_text) or text.count(i) < k:
            new_text += (f'{text.count(i)}{i}')
            k = 0
    return new_text
