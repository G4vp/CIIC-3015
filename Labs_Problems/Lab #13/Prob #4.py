# Add the __getitem__() and __setitem__() magic methods to your Vector class, to enable the index operator []
class Vector:
    def __init__(self,*values) -> None:
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
    
    def __getitem__(self,key) -> int:
        return self.values[key]
    
    def __setitem__(self,key,value):
        self.values[key] = value