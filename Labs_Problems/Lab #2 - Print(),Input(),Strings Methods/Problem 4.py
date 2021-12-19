# Write a program which asks the user to enter a birth year. Print the number of years remaining until someone born in that year may retire at age 70.

# You may assume that this program is being run in the year 2021. However, for those who are curious, it is possible to ask Python directly for the current year by putting the following two lines at the top of your program:

# import datetime
# year = datetime.datetime.now().year

# Now, the variable named ‘year’ should be an int set to the current year. (We will cover importing later in the semester, this is just a small taste of what is ahead.)

import datetime
year = datetime.datetime.now().year
birthDate = int(input('Enter a birth date: '))
print(birthDate-1951)