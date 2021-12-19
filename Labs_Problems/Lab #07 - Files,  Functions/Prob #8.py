# Write a function called ListCount() which takes a list and a value as its arguments and duplicates the behavior of the count() list method without using it.
def ListCount(arr,num):
    x = 0
    for i in arr:
        if i == num: 
            x += 1
    return x