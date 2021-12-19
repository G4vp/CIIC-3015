# Write a program which asks the user for their name. Strip the leading and trailing whitespace from that name and then print all of the following:

# The (stripped) user’s name as it was entered.

# The (stripped) user’s name in all uppercase letters.

# The (stripped) user’s name in all lowercase letters.

# The (stripped) user’s name such that the first letter in each word of the name is in uppercase and all of the other letters are in lowercase.

name = input("Enter a name: ").strip()
print(name)
print(name.upper())
print(name.lower())
print(name.title())