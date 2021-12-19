# Add the __contains__() magic method to your Vector class, which returns True or False depending on whether a given value is contained within the Vector.
class Vector:
    def __init__(self,*arg) -> None:
        self.arg = list(arg)
    def __str__(self) -> str:
        angle_brakets = '<'+str(self.arg)[1:-1]+'>'
        return angle_brakets
    def __repr__(self) -> str:
        return 'Vector'+ '('+str(self.arg)[1:-1]+')'
    def __len__(self) -> int:
        return len(self.arg)
    def __contains__(self,n) -> bool:
        return n in self.arg