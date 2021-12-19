# Write a non-destructive function called MergeSums() which takes two dictionaries as arguments and returns a new dictionary which is a combination of the first two. The two input dictionaries map keys to integers, where each integer represents a sum. The new dictionary contains all keys which appear in the union of both dictionaries, with the values being summed. Note that any given key may appear in either or both of the input dictionaries.
def MergeSums(D1,D2):
    D3 = D1.copy()
    for i in D2:
        if i in D3:
            D3[i] += D2[i]
        else:
            D3[i] = D2[i]
    return D3