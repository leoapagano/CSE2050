import unittest
from find_factors import find_factors as ff

class TestFindFactors(unittest.TestCase):
    def test_single_list(self):
        self.assertEqual(ff([3]), {3: [1, 3]})

    def test_triple_list(self):
        self.assertEqual(ff([4, 11, 24]), {4: [1, 2, 4], 11: [1, 11], 24: [1, 2, 3, 4, 6, 8, 12, 24]})

    def test_large_integers(self):
        self.assertEqual(ff([252, 160]), {252: [1, 2, 3, 4, 6, 7, 9, 12, 14, 18, 21, 28, 36, 42, 63, 84, 126, 252], 160: [1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 80, 160]})

unittest.main()