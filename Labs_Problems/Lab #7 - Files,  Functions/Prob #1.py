# Write a program that reads a file named cities.txt. Each line in the file contains a number, a comma, and the name of a city. Here are a few lines from the file:

# 45,Adjuntas
# 71,Aguada
# 69,Aguadilla
# 14,Aguas Buenas
# 29,Barceloneta
# Your program should print the shortest and longest city names. If there is a tie, use the name of the city which appears earlier in the file.

# Note: You should NOT assume that the cities will be cities in Puerto Rico.  You are not interested in the number, only in the names of the cities.

# Hint: Remember that a comma is what separates the distance from the city's name.

# Por ejemplo:

# Input files are already stored in Moodle server
fname = input('Enter file name: ')
fhand = open(fname,'r')

short = ' '*1000
longest = ''
for line in  fhand:
    city = line.strip().split(',')[1]
    if(len(city) < len(short)):
        short = city
    if(len(city) > len(longest)):
        longest = city 

print('Shortest city is', short)
print('Longest city is',longest)

fhand.close()
# Don't forget to close the file when you've finished