# Create a class called Vector.

# Your __init__() constructor must accept any number of numeric arguments and copy them into an internal list. You are not required to verify that the values are actually numeric.

# Add the __str__() magic method to your Vector class which returns a string containing the elements of the Vector separated by a comma and a space, and surrounded by angle brackets <>. Which is to say, calling print() on your object should look exactly like printing a list or a tuple, except with angle brackets instead of square brackets or parentheses.

# Then add the __repr__() magic method, which is identical to __str__() except instead of angle brackets you use the name of the class as a function and the elements of the Vector as arguments. Which is to say, __repr__() shows the Python code that would be needed in order to recreate your Vector object. For example, in the interactive Python interpreter the behavior should be the following:

# > v = Vector(1,2,3)
# > print(v)
# <1, 2, 3>
# > v
# Vector(1, 2, 3)
class Vector:
    def __init__(self,*arg) -> None:
        self.arg = list(arg)
    def __str__(self) -> str:
        angle_brakets = '<'+str(self.arg)[1:-1]+'>'
        return angle_brakets
    def __repr__(self) -> str:
        return 'Vector'+ '('+str(self.arg)[1:-1]+')'