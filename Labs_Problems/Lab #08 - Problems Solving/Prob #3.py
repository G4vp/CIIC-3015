# Write a function called ToRoman() which takes an int argument  less than 4000 and returns that value as a standard form Roman numeral string.

# Hint: Subtract successively smaller values of interest from your argument starting at M (1000) and work your way down to I (1).

# Reference: https://en.wikipedia.org/wiki/Roman_numerals
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