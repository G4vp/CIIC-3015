# Add the __len__() magic method to your Vector class, returning the number of elements in the Vector.
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
