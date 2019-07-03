from shape import Shape

class RightTriangle(Shape):
    res = 0
    def __init__(self ,side1 ,side2):
        self.side1 = side1
        self.side2 = side2

    def getArea(self):
        return float(self.side1 * self.side2) / 2



