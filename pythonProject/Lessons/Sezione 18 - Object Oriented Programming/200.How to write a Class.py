class Cuboid:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea (self):
        return self.length * self.breadth

    def total (self):
        return 2 * (self.length * self.breadth + self.length * self.breadth + self.length * self.breadth + self.length * self.breadth + self.length * self.breadth + self.length * self.breadth)

    def volume(self):
        return self.length * self.breadth * self.height

c1 = Cuboid(10,5,3)
print(c1.volume())