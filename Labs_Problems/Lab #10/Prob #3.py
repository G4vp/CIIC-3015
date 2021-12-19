# Write a void function called Purge() which takes a dictionary and a value as it arguments, and removes every key from the dictionary that maps to the given value.

# Remember: Do not alter the contents of a container while using that same container as the target of a for-loop! The behavior is undefined!
def Purge(D,value):
    for i in D.copy():
        if D[i] == value:
            del D[i]