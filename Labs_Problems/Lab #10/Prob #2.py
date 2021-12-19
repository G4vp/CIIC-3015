# Write a function called merge() which takes two arguments, a container of keys and a container of values, and returns a dictionary that contains (exactly) those keys and values. You may assume that all keys are unique and immutable.
def merge(dic1,dic2):
    return dict(zip(dic1,dic2))