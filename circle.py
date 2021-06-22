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
