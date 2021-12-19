# Add a copy() method to your Vector class, which returns a new Vector object that is a deep copy of the original.
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
    
    def copy(self):
        
        return Vector(list(self.values).copy())
    
        