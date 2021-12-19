# Write a non-destructive function named invert_dict that receives a dictionary as a parameter and returns an “inve
def invert_dict(dictionary):
    return {dictionary[x]:x for x in dictionary}