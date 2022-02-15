import abc

class Shape(abc.ABC): # for abstract type it is compelsory to start class name with Shape.

    @abc.abstractmethod

    def area(self):
        pass
class square(Shape):

    def __init__(self,a,b):
        self.a =a
        self.b = b

    def area(self):
        print(self.b*self.a)

s = square(19,10)
m =s.area()
print(m)


