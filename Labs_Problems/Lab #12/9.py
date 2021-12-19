# Run Length Encoding is a simple, lossless compression technique. For this lab we will be focusing only on strings, but in general RLE can also be used on other types of data. The idea behind RLE is to count the number of times the same value (in this case, characters) appears in sequence. Once we have our count, we output the repetition count of that character (as a character) followed by the character itself. Examples:

#     'A' -> '1A'
#     'AbbbC' -> '1A3b1C'
#     'aaaAAABBBBBBBB' -> '3a3A8B'
#     'ZZZZZZZZZZZZZZZZ' -> '9Z7Z'

# Note what is happening in the last example above: In this very simple algorithm we cannot directly encode a run with a length above nine because we cannot express values greater than nine with a single numeric digit. (We could extend our algorithm to interpret non-numeric characters for additional range but we are deliberately keeping things simple here.) So, a sequence of twelve 'A' characters could not be represented as '12A' because the decoder would see the leading '1' and then try to output a single '2'. Instead, for any run longer than nine, we just output encoded sequences of length nine until the entire run has been encoded in pieces.

# Write a recursive function called RLD() which takes a string that corresponds to the output from a Run Length Encoder as described above and returns the original, unencoded version of that string.
def RLD(text,t = ''):
    if len(text) > 1:
        t += int(text[0])*text[1]
        return RLD(text[2:],t)
    return t