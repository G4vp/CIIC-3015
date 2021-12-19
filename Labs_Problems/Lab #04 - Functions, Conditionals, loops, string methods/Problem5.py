# You are given a treasure map, in the form of a list of strings. Each string in your list corresponds to one row on the map, with the first string in the list being the most northern row and the last string in the list being the most southern row. The first character in each string corresponds to the most western part of that row and the last character in each string corresponds to the most eastern part of that row.

# Somewhere in your map may be a 'X', which marks where a treasure is buried. Write a function called Treasure() which accepts as an argument a list like the one described above, and returns the coordinates of the treasure as a pair of integers. The first integer describes which row contains the 'X' (starting at 0 for the top row, 1 for the next row down, and so on), and the second integer describes the index of the character within that row which contains the 'X' (starting at 0 for the first character). If the map does not contain a 'X' then return -1 for the row and -1 for the column.

# Example: Assume we had a map which looked like the following:

# oooo
# ooXo
# ooo

# The parameter passed to the Treasure() function for the above map would be [ 'oooo', 'ooXo', 'ooo' ] and the result would be (1, 2).

# Review: To return multiple values from a function, separate the returned values by a comma: return 1,2

# When Python prints multiple returned values it will automatically wrap those values in parentheses: (1, 2)
# This is normal behavior that we get for free - you don't need to worry about it or make it happen yourself.

# Hint: Python has a built-in function called enumerate() which may be of use here. It is entirely possible to solve this problem without using enumerate(), however it may help you to simplify your solution. Look it up and decide for yourselves whether you wish to make use of it.

def Treasure(arra):
    a = ([x for x in arra if not(x.find('X') == -1)])
    if not(a):
        return(-1,-1)
    return(arra.index(a[0]),a[0].index('X'))