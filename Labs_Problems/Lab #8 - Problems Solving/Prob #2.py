# Python divides the process of reading a file into separate parts: opening the file, reading the contents of the file, closing the file. This is a common model across many different software environments because it provides maximum flexibility. But sometimes we just want to read a file in a single chunk. So, write a function called Gimme() which takes the name of a text file as its argument and returns the entire contents of that file as a string
def Gimme(file):
    f1 = open(file,'r')
    f1.close()
    return(f1.read())