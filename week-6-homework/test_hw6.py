import random
import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    #####################################################################################
    ################## implement the common test scenarios  #############################
    ############## empty list, sorted list, reverse sorted list, random list ############
    #####################################################################################
        
    def test_empty_arr(self):
        """Given a sorting algorithm self.sorting_alg,
        tests it with an empty list."""
        initial_arr = []
        sorted_arr = list(self.sorting_alg(list(initial_arr))[0])
        self.assertEqual(sorted_arr, initial_arr)
    
    def test_pre_sorted_arr(self):
        """Given a sorting algorithm self.sorting_alg,
        tests it with a random-length list already in order."""
        initial_arr = sorted([random.randint(0, 1000) for i in range(random.randint(10, 100))])
        sorted_arr = list(self.sorting_alg(list(initial_arr))[0])
        self.assertEqual(sorted_arr, initial_arr)
    
    def test_pre_reverse_sorted_arr(self):
        """Given a sorting algorithm self.sorting_alg,
        tests it with a random-length list already in reverse order."""
        target_arr = sorted([random.randint(0, 1000) for i in range(random.randint(10, 100))])
        initial_arr = list(reversed(target_arr))
        sorted_arr = list(self.sorting_alg(list(initial_arr))[0])
        self.assertEqual(sorted_arr, target_arr)
    
    def test_randomized_arr(self):
        """Given a sorting algorithm self.sorting_alg,
        tests it with a random-length list."""
        initial_arr = [random.randint(0, 1000) for i in range(random.randint(10, 100))]
        target_arr = list(sorted(initial_arr))
        sorted_arr = list(self.sorting_alg(list(initial_arr))[0])
        self.assertEqual(sorted_arr, target_arr)

    def test_num_swaps(self, initial_arr, target_swaps):
        """Given a sorting algorithm self.sorting_alg,
        tests its' swap counting with a predetermined list."""
        actual_swaps = self.sorting_alg(list(initial_arr))[1]
        self.assertEqual(target_swaps, actual_swaps)



class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""
    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)
    
    def test_num_swaps(self):
        """Tests that num_swaps produces sane output with bubble sorting."""
        initial_arr = [14, 26, 80, 19, 4, 79]
        target_swaps = 7 # calculated by hand
        super().test_num_swaps(initial_arr, target_swaps)



class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""
    def setUp(self):
        """Set up the insertion sort algorithm for testing."""
        super().setUp(insertion_sort)

    def test_num_swaps(self):
        """Tests that num_swaps produces sane output with insertion sorting."""
        initial_arr = [98, 10, 37, 31, 26, 40]
        target_swaps = 5 # calculated by hand
        super().test_num_swaps(initial_arr, target_swaps)



class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""
    def setUp(self):
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)

    def test_num_swaps(self):
        """Tests that num_swaps produces sane output with selection sorting."""
        initial_arr = [66, 70, 91, 56, 29, 71]
        target_swaps = 4 # calculated by hand
        super().test_num_swaps(initial_arr, target_swaps)



if __name__ == "__main__":
    unittest.main()
