from shape import Shape
import math


class Circle(Shape):
    res = 0

    def __init__(self, r):
        self.r = r

    def getArea(self):
        return float(self.r *math.pi*math.pi)

