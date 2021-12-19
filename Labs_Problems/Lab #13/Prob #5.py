# Extend the __init__() constructor for your Vector class to also accept a single container as an argument; when given an iterable container such as a list or a tuple or another Vector, add each individual element within that container to the Vector. Note that you must perform a deep copy here.

# Hint: You can determine whether a value is iterable by calling len() on it and checking for an exception.
class Vector:
    def __init__(self,*values) -> None:
        self.values = values
        try:
            if len(values) >= 1:
                self.values = list(values[0])
        except:
            self.values = list(values)
        
    def __str__(self) -> str:
        angle_brakets = '<'+str(self.values)[1:-1]+'>'
        return angle_brakets

    def __repr__(self) -> str:
        return 'Vector'+ '('+str(self.values)[1:-1]+')'

    def __len__(self) -> int:
        return len(self.values)

    def __contains__(self,n) -> bool:
        return n in self.values
    
    def __getitem__(self,key):
        return self.values[key]
    
    def __setitem__(self,key,value):
        self.values[key] = value
        
    
        