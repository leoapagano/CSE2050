# Whatever file your algorithm is at (BinarySearch for me)
from BinarySearch import binary_search_iter as iter
from BinarySearch import binary_search_recr as recr
import unittest

class TestSearchFactory:
    """Test case factory for binary search algorithms."""

    def setUp(self, f):
        """When inheriting TestSearchFactory, specify the search function as f using super().setUp(function_name)."""
        self.f = f

    def universal_test(self, L, item, found):
        """Universal test case. Takes a list, an item to be searched, and a boolean "found"."""
        self.assertEqual(self.f(L, item), found)
    
    def test_empty_list(self):
        """Test if items can be found in empty lists."""
        self.universal_test([], 8, False)
        self.universal_test([], 0, False)
        self.universal_test([], 4, False)
        self.universal_test([], -16, False)
    
    def test_single_item_list(self):
        """Test if items can be found in 1-item lists."""
        self.universal_test([2], 14, False)
        self.universal_test([12], -12, False)
        self.universal_test([3], -1, False)
        self.universal_test([7], 7, True)
        self.universal_test([11], 1, False)

    def test_below_bounds(self):
        """Tests for items below an entire list."""
        L = [4, 6, 11, 17, 20]
        self.universal_test(L, -1, False)
        self.universal_test(L, -5, False)
        self.universal_test(L, 3, False)
        self.universal_test(L, 0, False)

    def test_in_bounds(self):
        """Tests for items between a list's items."""
        L = [18, 25, 29, 180, 181]
        self.universal_test(L, 21, False)
        self.universal_test(L, 95, False)
        self.universal_test(L, 27, False)

    def test_in_bounds_found(self):
        """Tests for items that match a list's items."""
        L = [20, 21, 34, 36, 100]
        self.universal_test(L, 21, True)
        self.universal_test(L, 100, True)
        self.universal_test(L, 34, True)

    def test_above_bounds(self):
        """Tests for items above an entire list."""
        L = [25, 55, 82, 83, 84]
        self.universal_test(L, 90, False)
        self.universal_test(L, 108, False)
        self.universal_test(L, 155, False)

class TestRecrBinSearch(TestSearchFactory, unittest.TestCase):
    """Test cases for recursive binary search."""
    def setUp(self):
        super().setUp(recr)

class TestIterBinSearch(TestSearchFactory, unittest.TestCase):
    """Test cases for iterative binary search."""
    def setUp(self):
        super().setUp(iter)

if __name__ == "__main__":
    unittest.main()