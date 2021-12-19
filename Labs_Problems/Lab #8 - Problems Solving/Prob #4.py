# Write a function called FileToRoman() which takes the names of two text files. The first file contains a list of Arabic numbers, one per line. Your function must read the contents of this file, translate each value into a Roman numeral in standard form, and write those Roman numerals in the same order (one per line) to the second file, which your function will create.

# Hint: If you use your ToRoman() function from earlier in the lab, this problem only requires seven or so new lines of Python.

from os import write


def ToRoman(n):
    text = ''
    asd = str(n)
    roman_numbers = [['M',1000],['D',500],['C',100],['L',50],['X',10],['V',5],['I',1]]

    for i in range(len(asd)):
        temp = int(asd[i])*10**(len(asd)-(i+1))
        j = 0
        while(j < len(roman_numbers)):
            if(int(asd[i])%4 == 0 and int(asd[i])//4 == 1):
                if(temp >= roman_numbers[j][1]):
                    text += roman_numbers[j][0] + roman_numbers[j-1][0]
                    temp -= roman_numbers[j][1]
                    break
            elif(int(asd[i])%9 == 0 and int(asd[i])//9 == 1):
                if(temp >= roman_numbers[j][1]):
                    text += roman_numbers[j+1][0] + roman_numbers[j-1][0]
                    temp -= roman_numbers[j][1]
                    break
            elif(temp >= roman_numbers[j][1]):
                text += roman_numbers[j][0]
                temp -= roman_numbers[j][1]
                j += -1
            j += 1
    return text
def FileToRoman(inp,out):
    finp = open(inp,'r')
    fout = open(out,'w')
    for line in finp:
        fout.writelines(str(ToRoman(int(line.strip()))) + '\n')
    finp.close()
    fout.close()
