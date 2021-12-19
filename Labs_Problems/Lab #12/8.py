# The dot product of two vectors is calculated by multiplying the corresponding elements of each vector together and summing those products. For example, the dot product of [2, 0, 1] and [6, 3, 4] = 2*6 + 0*3 + 1*4 = 12 + 0 + 4 = 16

# Write a recursive function called Dot() which takes two lists as arguments and returns the dot product of those lists as a float. You may assume that both lists have equal length and contain only numeric values.
def Dot(lst1,lst2,c=0,total = 0.0):
    if c < len(lst1):
        total += lst1[c] * lst2[c]
        return Dot(lst1,lst2,c+1,total)
    return total
    