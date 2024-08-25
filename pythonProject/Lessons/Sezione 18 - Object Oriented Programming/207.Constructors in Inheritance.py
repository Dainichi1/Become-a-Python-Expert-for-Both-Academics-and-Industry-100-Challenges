class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getLength(self):
        return self.length

    def setLength (self, length):
        self.length = length

    def area (self):
        return self.length * self.breadth

    def perimeter (self):
        return 2 * (self.length + self.breadth)


class Cuboid (Rectangle):
    def __init__(self, height, length, breadth):
        super().__init__(length, breadth)
        self.height = height

    def volume (self):
        return self.length * self.height * self.breadth



r = Rectangle(10,5)
print(r.getLength())
r.setLength(15)
print(r.area())

c = Cuboid(10,5,6)
print (c.volume())


