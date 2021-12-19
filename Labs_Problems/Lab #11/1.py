# Write a function called ReadDict() which takes the name of a file as an argument and returns a dictionary containing the contexts of the file. The file contains a single line, which is a comma-delimited list of key:value pairs; each key and value is separated by a colon, and all keys and all values are strings.
def ReadDict(file):
    opFile = open(file,'r')
    line = opFile.readline().strip().split(',')
    Dic = {}
    for i in line:
        key, value = i.split(':')
        Dic[key] = value
    return Dic