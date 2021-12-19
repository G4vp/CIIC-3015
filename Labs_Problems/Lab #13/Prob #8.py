# Add the __mul__() and __rmul__() magic methods to your Vector class, to create and return a new Vector equal to the original with each of its elements multiplied by a given number.
class Vector:
    def __init__(self,*values) -> None:
        self.values = values
        try:
            if len(values) >= 1:
                self.values = list(values[0])
        except:
            self.values = list(values)
        
    def __str__(self) -> str:
        angle_brakets = '<'+str(list(self.values))[1:-1]+'>'
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
    
    def copy(self):
        return self.values.copy()
    
    def __add__(self,object2):
        newVector = list()
        for i in range(len(self.values)):
            newVector.append(self.values[i] + object2[i])
        return Vector(newVector)
        
    def __mul__(self,number):
        newVector = list()
        for i in self.values:
            newVector.append(i*number)
        return Vector(newVector)
        
    def __rmul__(self,number):
        newVector = list()
        for i in self.values:
            newVector.append(i*number)
        return Vector(newVector)