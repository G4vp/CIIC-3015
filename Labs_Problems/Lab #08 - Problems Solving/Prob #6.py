# Write a function called FileFromRoman() which takes the names of two text files. The first file contains a list of Roman numerals in standard form, one per line. Your function must read the contents of this file, translate each value into Arabic, and write those Arabic numbers in the same order (one per line) to the second file, which your function will create.

# Hint: If you use your FromRoman() function from earlier in the lab, this problem only requires seven or so new lines of Python.
def FromRoman(n):
    conversion = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    count = 0
    for i in range(len(n)):
        if(conversion.get(n[i-1]) < conversion.get(n[i]) and i != 0):
            count -= conversion.get(n[i-1])+conversion.get(n[i-1]) 
        count += conversion.get(n[i])
    return count


def FileFromRoman(inp,out):
    finp = open(inp,'r')
    fout = open(out,'w')
    for line in finp:
        fout.writelines(str(FromRoman(line.strip()))+'\n')
    finp.close()
    fout.close()