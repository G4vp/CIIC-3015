# At Facebook:
# All employees earn 20 days of vacation per year.

# At Amazon:
# New employees earn 10 days of vacation per year.
# After 1 year this is increased to 15 days

# At Google:
# New employees earn 15 days of vacation per year.
# After 3 years this is increased to 20 days.
# After 5 years this is increased to 25 days

# At Apple:
# New employees earn 12 days of vacation per year.
# After 3 years this is increased to 15 days.
# After 4 years, and every year after that, it is increased by 1 more day.

# At Microsoft:
# New employees earn 15 days of vacation per year.
# After every 5 years, this is increased by 5 more days, to a maximum of 30 days total per year.

# Write a function called Vacation() which takes a string and an integer. The string is the name of a company, the integer is the number of months someone has worked at that company. Return the number of vacation days that this person earns per year.

# (Disclaimer: I can only verify that the numbers above are current and correct for Google. The other numbers are true to the best of my knowledge. For entertainment purposes only.)

# Perform your development in the following embedded Repl.it IDE, but copy your final code into the text area further below labeled "Answer".

def Vacation(company,months):
    year = months//12
    if(company == 'Facebook'):
        return 20
    elif(company == 'Amazon'):
        if(year >= 1):
            return 15
        return 10
    elif(company == 'Google'):
        if(year >= 5):
            return 25
        elif(year >= 3):
            return 20
        return 15
    elif(company == 'Apple'):
        if(year >= 4):
            return (15 + (year - 3))
        elif(year >= 3):
            return 15
        return 12
    elif(company == 'Microsoft'):
        if(year >= 5):
            if(15 + ((year//5)) > 30):
                return 30
            return 15 + ((year//5)*5)
        return 15
print(Vacation('Microsoft',64))
