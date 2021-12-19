# Write a function called Inventory() which takes the name of a file and returns a dictionary. Each line in the file is a string, to be used as a dictionary key. The value associated with that key is the total number of times the key appears in the file. For example, if we have a file called food.txt:

# spam
# spam
# eggs
# spam

# Then calling Inventory('food.txt') should return a dictionary that looks something like:

# {'spam': 3, 'eggs': 1}

# Remember to strip the trailing newline character from each line before adding it to the dictionary.
def Inventory(file):
    fopen = open(file,'r')
    Items = {}
    for line in fopen:
        line = line.strip()
        if line in Items:
            Items[line] += 1
        else:
            Items[line] = 1
    return Items