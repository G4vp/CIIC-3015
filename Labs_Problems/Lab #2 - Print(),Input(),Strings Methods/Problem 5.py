# Write a program which asks the user to input an integer. Print the digit which appears in the hundreds place for that number. So, for an input of 1234 you would print a 2. For an input of 987 you would print a 9. For an input of 36 you would print a 0. For an input of 1937560 you would print a five. (Hint: Review the list of Python arithmetic operators from last week. There are seven of them. You will need to use two.)
a = int(input('Enter a number: '))

if(a >= 100):print(str(a%1000)[0])
else:print(0)