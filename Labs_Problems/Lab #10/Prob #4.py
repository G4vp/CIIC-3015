# Write a function called Checkout() which takes two dictionaries as arguments. The first dictionary maps strings to floats and contains prices for various items. So for example {'frozen pizza': 20.99} would mean that one frozen pizza costs $20.99. The second dictionary maps strings to ints and is your shopping list. So for example {'frozen pizza': 4} means that you need to buy four frozen pizzas.

# Your function must compare the shopping list to the list of prices and calculate the total amount spent. However, it is possible that the store does not have everything on the shopping list, in which case any missing item(s) are simply ignored and do not contribute to the total.
def Checkout(price,order):
    total = 0.0
    for i in order:
        total += price.get(i,0)*order[i]
    return total

