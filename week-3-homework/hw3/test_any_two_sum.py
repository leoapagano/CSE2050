import unittest
from any_two_sum import any_two_sum

class TestAnyTwoSum(unittest.TestCase):
    '''Test cases for any_two_sum().'''

    def test_true_cases(self):
        """Test cases which should be true"""
        self.assertTrue(any_two_sum([4, 9, 11, 19, 23], 27)) # 4+23=27
        self.assertTrue(any_two_sum([11, 12, 19, 59, 40, 67, 82, 83, 88], 99)) # 11+88=99
        self.assertTrue(any_two_sum([11, 19, (7*5), 6], 54)) # 35+19=54
        self.assertTrue(any_two_sum([31, (6**2), 11, 30, 96], 66)) # 30+36=66
        self.assertTrue(any_two_sum([9, 15, (4*4), 46, (33*2)], 81)) # 15+66=81

    def test_false_cases(self):
        """Test cases which should be false"""
        self.assertFalse(any_two_sum([4, 11, 18, 25], 80))
        self.assertFalse(any_two_sum([5, 6, 7, 8, 11, 16], 25))
        self.assertFalse(any_two_sum([35, (7*10), 5, 51, 56, 66], 67))
        self.assertFalse(any_two_sum([11, 12, 13, (4**2)], 33))
        self.assertFalse(any_two_sum([2, 3, 5, 6, 11, 17, 28], 46))


if __name__ == "__main__":
    unittest.main()