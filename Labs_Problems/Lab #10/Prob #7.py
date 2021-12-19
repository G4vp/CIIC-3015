# Write a function called Passwords() which takes the name of a file containing usernames and passwords and returns a dictionary mapping the usernames to their passwords. Each line of the file contains one username and one password, separated by a colon ':'. Remember to remove the trailing newline character from the passwords. Also, the colon character ':' is not allowed to be part of a username but it is allowed to be part of a password. The space character is also allowed to be part of a password.
def Passwords(file):
    fop = open(file,'r')
    data = {}
    for line in fop:
        line = line.lstrip().replace('\n','')
        data[line[0:line.find(':')]] = line[line.find(':')+1:]
    return data   