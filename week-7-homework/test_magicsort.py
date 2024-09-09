import random
import unittest
import magicsort

LARGE_LIST_SIZE_MIN, LARGE_LIST_SIZE_MAX = 50, 100
ITEM_VALUE_MIN, ITEM_VALUE_MAX = 0, 1000

##############################
# LINEAR SCAN ALG TEST CASES #
##############################

class TestLinearScan(unittest.TestCase):
    """Test cases for the linear_scan() function.
    The test cases for these differ from SortingTestFactory enough that I didn't use the same test factory for them."""

    def compare(self, case, list):
        self.assertEqual(magicsort.linear_scan(list), magicsort.MagicCase(case))

    def test_empty_list(self):
        """Tests an empty list."""
        # No items - in order
        L1 = []
        self.compare(1, L1)
    
    def test_unilist(self):
        """Tests lists with 1 item."""
        # 1 item - in order
        L1 = [3]
        self.compare(1, L1)
        # 1 item - in order
        L2 = [0]
        self.compare(1, L2)

    def test_duolist(self):
        """Tests lists with 2 items."""
        # 2 items - in order
        L1 = [12, 13]
        self.compare(1, L1)
        # 2 items - in reverse order
        L2 = [7, 6]
        self.compare(3, L2)

    def test_trilist(self):
        """Tests lists with 3 items."""
        # 3 items - in order
        L1 = [4, 7, 10]
        self.compare(1, L1)
        # 3 items - in reverse order
        L2 = [5, 2, 0]
        self.compare(3, L2)
        # 3 items - constant inversions
        L3 = [14, 6, 7]
        self.compare(2, L3)
    
    def test_general_case_list(self):
        """Tests lists with more than 10 out of order items.
        Note that this test case falls apart when you change out INVERSION_BOUND's value."""
        # 9 inversions - should NOT cause general case - spacing added for your convenience
        L1 = [3, 4,   2, 3, 11,   1,   0, 5, 6,   3, 4,   2,   1, 2, 5,   8, 11,   4,   2]
        self.compare(2, L1)
        # 10 inversions - should cause general case - spacing added for your convenience
        L2 = [5, 9, 9,   6,   4, 15,   11, 13,   9,   6,   0, 3, 9,   3,   2, 3, 12, 15,   7,   3]
        self.compare(0, L2)

    def test_reverse_sorted_list(self):
        """Tests lists that are sorted, but in reverse order."""
        # Lists with 4 items (below 10)
        L1 = [85, 59, 54, 3]
        self.compare(3, L1)
        L2 = [93, 73, 63, 7]
        self.compare(3, L2)
        # Lists with 16 items (above 10)
        L3 = [97, 89, 76, 67, 65, 63, 60, 58, 57, 42, 40, 21, 18, 13, 8, 4]
        self.compare(3, L3)
        L4 = [93, 93, 89, 89, 80, 74, 70, 57, 50, 41, 19, 18, 11, 5, 3, 1]
        self.compare(3, L4)

    def test_pre_sorted_list(self):
        """Tests lists that are already sorted."""
        # Lists with 8 items (below 10)
        L1 = [6, 37, 67, 68, 69, 72, 92, 94]
        self.compare(1, L1)
        L2 = [9, 15, 17, 19, 27, 66, 79, 96]
        self.compare(1, L2)
        # Lists with 20 items (above 10)
        L3 = [2, 4, 12, 15, 16, 18, 18, 20, 23, 34, 43, 44, 61, 62, 69, 70, 76, 79, 85, 88]
        self.compare(1, L3)
        L4 = [0, 4, 10, 13, 16, 18, 29, 30, 39, 45, 51, 62, 63, 69, 78, 78, 80, 89, 90, 96]
        self.compare(1, L4)



################################
# MAGIC SORTING ALG TEST CASES #
################################

class SortingTestFactory:
    """Prebuilt test cases for all sorting algorithms.
    Drop your algorithm of choice into setUp() and you're golden."""

    def setUp(self, sorting_alg):
        """Set up a test case factory, given a sorting alg of your choice"""
        self.sorting_alg = sorting_alg

    def universal_test(self, L, left=None, right=None):
        """Universal test definition for all tests,
        in terms of a starter list L, and left and right bounds"""
        if left is None: left = 0
        if right is None: right = len(L)

        L_intended = L[:left] + sorted(L[left:right]) + L[right:]
        self.sorting_alg(L, left, right)
        self.assertEqual(L, L_intended)

    def test_empty_list(self):
        """Tests an empty list"""
        # Generate list
        empty_list = []

        self.universal_test(empty_list)

    def test_random_unilist(self):
        """Tests a random list with one item"""
        # Generate list
        random_unilist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX)]

        # Test with whole list
        self.universal_test(random_unilist)

    def test_sorted_duolist(self):
        """Tests a random, pre-sorted list with two items"""
        # Generate list
        random_duolist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX) for i in range(2)]
        sorted_duolist = sorted(random_duolist)

        # Test with whole list
        self.universal_test(sorted_duolist)

    def test_reversed_duolist(self):
        """Tests a random, pre-reverse-sorted list with two items"""
        # Generate list
        random_duolist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX) for i in range(2)]
        sorted_duolist = sorted(random_duolist)
        reversed_duolist = list(reversed(sorted_duolist))

        # Test with whole list
        self.universal_test(reversed_duolist)

        # Test with fixed bounds (same as single list) on lower side
        lb = 0 # first half
        rb = 1 # second half
        self.universal_test(reversed_duolist, left=lb, right=rb)

        # Test with fixed bounds (same as single list) on upper side
        lb = 1 # first half
        rb = 2 # second half
        self.universal_test(reversed_duolist, left=lb, right=rb)

    def test_random_largelist(self):
        """Tests a random list with LARGE_LIST_SIZE_MIN/MAX items"""
        # Generate list
        random_largelist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX) for i in range(random.randint(LARGE_LIST_SIZE_MIN, LARGE_LIST_SIZE_MAX))]

        # Test with whole list
        self.universal_test(random_largelist)

        # Test with random left and right bounds
        lb = random.randint(0, len(random_largelist) // 2) # first half
        rb = random.randint(len(random_largelist) // 2 + 1, len(random_largelist)) # second half
        self.universal_test(random_largelist, left=lb, right=rb)

    def test_sorted_largelist(self):
        """Tests a random, pre-sorted list with LARGE_LIST_SIZE_MIN/MAX items"""
        # Generate list
        random_largelist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX) for i in range(random.randint(LARGE_LIST_SIZE_MIN, LARGE_LIST_SIZE_MAX))]
        sorted_largelist = sorted(random_largelist)

        # Test with whole list
        self.universal_test(sorted_largelist)

        # Test with random left and right bounds
        lb = random.randint(0, len(sorted_largelist) // 2) # first half
        rb = random.randint(len(sorted_largelist) // 2 + 1, len(sorted_largelist)) # second half
        self.universal_test(sorted_largelist, left=lb, right=rb)

    def test_reversed_largelist(self):
        """Tests a random, pre-reverse-sorted list with LARGE_LIST_SIZE_MIN/MAX items"""
        # Generate list
        random_largelist = [random.randint(ITEM_VALUE_MIN, ITEM_VALUE_MAX) for i in range(random.randint(LARGE_LIST_SIZE_MIN, LARGE_LIST_SIZE_MAX))]
        sorted_largelist = sorted(random_largelist)
        reversed_largelist = list(reversed(sorted_largelist))

        # Test with whole list
        self.universal_test(reversed_largelist)

        # Test with random left and right bounds
        lb = random.randint(0, len(reversed_largelist) // 2) # first half
        rb = random.randint(len(reversed_largelist) // 2 + 1, len(reversed_largelist)) # second half
        self.universal_test(reversed_largelist, left=lb, right=rb)


class TestMagicInsertionSort(SortingTestFactory, unittest.TestCase):
    """Test cases for magic_insertionsort()."""

    def setUp(self):
        """Set up all magic insertion sorting test cases."""
        super().setUp(magicsort.magic_insertionsort)

class TestMagicMergeSort(SortingTestFactory, unittest.TestCase):
    """Test cases for magic_mergesort()."""

    def setUp(self):
        """Set up all magic merge sorting test cases."""
        super().setUp(magicsort.magic_mergesort)

class TestMagicQuickSort(SortingTestFactory, unittest.TestCase):
    """Test cases for magic_quicksort()."""

    def setUp(self):
        """Set up all magic quick sorting test cases."""
        super().setUp(magicsort.magic_quicksort)

class TestMagicSort(SortingTestFactory, unittest.TestCase):
    """Test cases for magicsort()."""

    def setUp(self):
        """Set up all magic sorting test cases."""
        super().setUp(magicsort.magicsort)
    
    def universal_test(self, L, left=None, right=None):
        """Custom universal test definition for magicsort tests.
        In terms of a starter list L, without left or right params"""
        L_intended = sorted(L) 
        self.sorting_alg(L)
        self.assertEqual(L, L_intended)



############################
# LIST REVERSAL TEST CASES #
############################

class TestListReversal(SortingTestFactory, unittest.TestCase):
    """Test cases for reverse_list()."""

    def setUp(self):
        """Set up all list reversal test cases."""
        super().setUp(magicsort.reverse_list)

    def universal_test(self, L, left=None, right=None):
        """Custom universal test definition for list reversal tests in terms of a starter list L."""
        L_intended = list(reversed(L))
        self.sorting_alg(L)
        self.assertEqual(L, L_intended)



unittest.main()