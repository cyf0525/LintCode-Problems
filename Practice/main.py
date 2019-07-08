from right_triangle import RightTriangle
from rectangle import Rectangle
from circle import Circle


ans_h = float(raw_input("give me a side of tri: "))
ans_b = float(raw_input("give me a height of tri: "))
ans_r = float(raw_input("give me a r of circle: "))
ans_s1 = float(raw_input("give me a side of rect: "))
ans_s2 = float(raw_input("give me a side 2 of rect: "))



a = RightTriangle(ans_h, ans_b)
b = Circle(ans_r)
c = Rectangle(ans_s1,ans_s2)



print "Area of right triangle is %f" % a.getArea()
print "Area of circle is %f" % b.getArea()
print "Area of rectangle is %f" % c.getArea()

