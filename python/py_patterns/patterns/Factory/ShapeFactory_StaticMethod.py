# a simple static factory method

from __future__ import generators
import random
import math

class Shape(object): #base abstract class

    def __init__(self,size):
        self._size = size

    def factory(type,size):
        #return eval(type + "()")
        if type == "Circle": return Circle(size)
        if type == "Square": return Square(size)
        assert 0, "bad shape cretion:" + type
    factory = staticmethod(factory)   #static method

    def showPerimeter(self):
        print("perimer is: {}".format(self.shapePerimeter()))

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")
    def shapePerimeter(self):
        return math.pi * self._size **2

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")
    def shapePerimeter(self):
        return 4 * self._size

#---- global func -----#

def shapeNameGen(n):
    types = Shape.__subclasses__()  # ['Square', 'Cirle']
    for i in  range(n):
        yield random.choice(types).__name__

if __name__ == '__main__':
    shapes = [ Shape.factory(i,1.0) for i in shapeNameGen(5) ]

    for shape in shapes:
        shape.draw()
        shape.erase()
        shape.showPerimeter()

