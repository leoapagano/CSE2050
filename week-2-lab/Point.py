class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Checks if the x attribute and y attribute are the same for self and other"""
        return (self.x == other.x) and (self.y == other.y)

    def equidistant(self, other):
        """Checks that Point self and Point other are the same distance from 0, 0"""
        return (self.x**2 + self.y**2) == (other.x**2 + other.y**2)

    def within(self, distance, other):
        """Checks if point self and other are within a certain distance from each other"""
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2) <= distance