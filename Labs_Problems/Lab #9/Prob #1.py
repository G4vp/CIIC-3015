# Write a non-destructive function called AlmostMin() which takes a container and returns the 2nd smallest unique value within it, and returns None if there is no such value. You may not use any form of sorting in your solution.
def AlmostMin(a):
    newA = set(a)
    secondMin = max(newA)
    if len(newA) < 2: return 
    for i in newA:
        if i <  secondMin and i != min(newA):
            secondMin = i
    return secondMin