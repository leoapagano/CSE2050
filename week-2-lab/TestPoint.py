import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(-3, 4)
        self.p2 = Point(-4, 3)
        self.p3 = Point(3, 4)
        self.p4 = Point(3.5, 4)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""        
        self.assertEqual(self.p1.x, -3)
        self.assertEqual(self.p1.y, 4)
        self.assertEqual(self.p2.x, -4)
        self.assertEqual(self.p2.y, 3)

    def test_eq(self):
        """Tests that the two points are NOT equal, but are equal to a third point"""
        self.assertNotEqual(self.p1, self.p2)
        self.assertEqual(self.p1, Point(-3, 4))

    def test_equidistant(self):
        """Tests that the two points are equal distance from the origin"""
        self.assertEqual(self.p1.equidistant(self.p2), True) # Different X and Y, same distance
        self.assertEqual(self.p1.equidistant(self.p1), True) # Same X and Y, same distance
        self.assertNotEqual(self.p1.equidistant(Point(7, 10)), True) # Different X and Y, different distance
        
    def test_within(self):
        """Checks that the two points are of distance 2**(1/2) and NOT 1"""
        self.assertNotEqual(self.p2.within((1), self.p1), True)
        self.assertEqual(self.p2.within((2**(1/2)), self.p1), True)
        # Another test case
        self.assertEqual(self.p3.within(1, self.p4), True)

unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects