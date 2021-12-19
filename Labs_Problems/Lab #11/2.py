# Write a void function called WriteDict() which takes a dictionary and the name of a file as its arguments. Each key in the dictionary is a string, and each value in the dictionary is a list of strings. Write the dictionary contents to the output file such that each line of the file consists of the dictionary key, followed by a colon, followed by each element of the value separated by a comma. For example, if the dictionary is the following:

# { 'spam' : ['spam', 'spam', 'spam', 'lovely', 'spam'], 'eggs' : ['Just', 'the', 'spam', 'please'] , 'dead parrot' : ['wrong', 'sketch'] }

# Then the output file should consist of:

# spam:spam,spam,spam,lovely,spam
# eggs:Just,the,spam,please
# dead parrot:wrong,sketch
def WriteDict(dic, file):
    fOpen = open(file,'w')
    for key,value in dic.items():
        fOpen.write(f"{key}:{','.join(value)}\n")