class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width            
x = Shape()
xy = Rectangle(4, 3)
print(x.area())
print(xy.area())
