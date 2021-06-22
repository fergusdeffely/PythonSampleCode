import math


class Circle:

    def __init__(self, x=0, y=0, radius=0):
        self.x = x
        self.y = y
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius


circle = Circle(10, 10, 5)
print(f"\n\ncircle is positioned at ({circle.x}, {circle.y}), it's radius is {circle.radius}")

circumference = circle.circumference()
area = circle.area()

print(f"The circumference is {circumference:.2f} and the area is {area:.2f}\n\n")
