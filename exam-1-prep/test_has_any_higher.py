import unittest
from has_any_higher import *

class TestHasAnyHigherFast(unittest.TestCase):
    def test_same_results_smallL1_bigL2(self):
        L1 = [11, 4, 9]
        L2 = [1, 205, 66, 113, 4, 2, 1, 17, 73, 180, 95]
        self.assertFalse(has_any_higher(L1, L2))
        self.assertFalse(has_any_higher_fast(L1, L2))

    def test_same_results_bigL1_smallL2(self):
        L1 = [20, 9, 160, 48, 224, 18, 180, 44, 213, 456]
        L2 = [603, 112]
        self.assertEqual(has_any_higher(L1, L2), has_any_higher_fast(L1, L2))
        
    def test_same_results_two_small_lists(self):
        L1 = [1, 5, 9]
        L2 = [2, 8, 11]
        self.assertEqual(has_any_higher(L1, L2), has_any_higher_fast(L1, L2))