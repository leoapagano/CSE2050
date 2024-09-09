# Wherever you keep your sorting algs
from MoreSortingAlgs import bubblesort, selectionsort, insertionsort, mergesort, quicksort
import random
import unittest

class SortingTestFactory:
	"""Test case factory for sorting algorithms."""

	def setUp(self, f):
		"""Specify a sorting algorithm with super().setUp(sorting_alg) in setUp()."""
		self.f = f

	def universal_test(self, L):
		"""Tests that a list L can be sorted properly against a known working sorting algorithm."""
		target = sorted(L)
		self.f(L)
		self.assertEqual(L, target)
	
	def test_empty_list(self):
		"""Tests the sorting alg self.f with an empty list."""
		L = []
		self.universal_test(L)

	def test_random_1_item_lists(self):
		"""Tests the sorting alg self.f with random, 1-item lists."""
		NUM_TRIALS = 5
		for i in range(NUM_TRIALS):
			L = [random.randint(-100, 100)]
			self.universal_test(L)

	def test_random_2_item_lists(self):
		"""Tests the sorting alg self.f with random, 2-item lists."""
		NUM_TRIALS = 5
		for i in range(NUM_TRIALS):
			L = [random.randint(-100, 100) for i in range(2)]
			self.universal_test(L)

	def test_random_fixed_lists(self):
		"""Tests the sorting alg self.f with random, fixed-length lists."""
		NUM_TRIALS = 5
		LENGTH_TO_TEST = 25
		for i in range(NUM_TRIALS):
			L = [random.randint(-100, 100) for i in range(LENGTH_TO_TEST)]
			self.universal_test(L)

	def test_random_arbitrary_lists(self):
		"""Tests the sorting alg self.f with random, random-length lists."""
		LENGTHS_TO_TEST = range(3, 20) # We have 0, 1, and 2 already
		for length in LENGTHS_TO_TEST:
			L = [random.randint(-100, 100) for i in range(length)]
			self.universal_test(L)

	def test_pre_sorted_lists(self):
		"""Tests the sorting alg self.f with random, pre-sorted, fixed-length lists."""
		NUM_TRIALS = 5
		LENGTH_TO_TEST = 25
		for i in range(NUM_TRIALS):
			L = [random.randint(-100, 100) for i in range(LENGTH_TO_TEST)]
			L.sort()
			self.universal_test(L)

	def test_pre_reversed_lists(self):
		"""Tests the sorting alg self.f with random, pre-reverse-sorted, fixed-length lists."""
		NUM_TRIALS = 5
		LENGTH_TO_TEST = 25
		for i in range(NUM_TRIALS):
			L = [random.randint(-100, 100) for i in range(LENGTH_TO_TEST)]
			L.sort()
			L.reverse()
			self.universal_test(L)

class TestBubbleSort(SortingTestFactory, unittest.TestCase):
	def setUp(self):
		super().setUp(bubblesort)

class TestSelectionSort(SortingTestFactory, unittest.TestCase):
	def setUp(self):
		super().setUp(selectionsort)

class TestInsertionSort(SortingTestFactory, unittest.TestCase):
	def setUp(self):
		super().setUp(insertionsort)

class TestMergeSort(SortingTestFactory, unittest.TestCase):
	def setUp(self):
		super().setUp(mergesort)

class TestQuickSort(SortingTestFactory, unittest.TestCase):
	def setUp(self):
		super().setUp(quicksort)

if __name__ == "__main__":
	unittest.main()