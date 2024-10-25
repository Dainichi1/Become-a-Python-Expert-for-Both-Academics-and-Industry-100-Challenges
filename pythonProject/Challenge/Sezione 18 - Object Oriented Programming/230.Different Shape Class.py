import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

r = Rectangle(10, 5)
print('Area of Rectangle:', r.area())

c = Circle(7)
print('Area of Circle:', c.area())
