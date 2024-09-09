###############################################################
# PLEASE DO NOT SUBMIT THESE TEST CASES TO GRADESCOPE         #
# FOR TESTING USE ONLY - DO NOT REDISTRIBUTE		          #
# I DON'T FEEL LIKE REFACTORING THIS MESS SO STFU BC IT WORKS #
###############################################################

from copy import deepcopy
from random import randint, choices
from string import ascii_lowercase
import unittest
from simple_tree_functions import TreeNode, height, size, find_min, find_max, contains, in_order, pre_order, post_order
from higher_order_tree_functions import count_failures, tree_map, tree_apply

class TestTrees(unittest.TestCase):
	"""Test cases for our TreeNode class and its many compatible functions."""

	def setUp(self):
		"""Test building six different trees; four are predetermined,
		and two are randomly-generated with a predetermined number of items."""
		# Build first predetermined tree:
		# This is a very simple all-integer tree. It should look like;
		#        0
		#      /   \
		#     4     6
		#      \
		#		2
		self.Tree1 = TreeNode(
			0,
			left=TreeNode(
				4,
				right=TreeNode(2)
			),
			right=TreeNode(6)
		)

		# Build second predetermined tree:
		# This is a more complex all-integer tree. It should look like;
		#        131
		#       /   \
		#      15   143
		#     / \     \
		# 	 9  113    5
		#             / \
		#            13  3
		self.Tree2 = TreeNode(
			131,
			left=TreeNode(
				15,
				left=TreeNode(9),
				right=TreeNode(113)
			),
			right=TreeNode(
				143,
				right=TreeNode(
					5,
					left=TreeNode(13),
					right=TreeNode(3)
				)
			)
		)

		# Build third predetermined tree:
		# This is a simpler tree, but with chars instead of ints. It should look like;
		#        'k'
		#       /   \
		#     't'    'm'
		#       \      \ 
		#	    'a'    'h'
		self.Tree3 = TreeNode(
			'k',
			left=TreeNode(
				't',
				right=TreeNode('a')
			),
			right=TreeNode(
				'm',
				right=TreeNode('h')
			)
		)

		# Build fourth predetermined tree:
		# This is a more complex tree with both ints, floats, and chars. It should look like;
		#       86400
		#      /     \
		#    'r'   365.2422
		#    / \       \
		#  'k'  'm'    1440
		#      /   \     \
		#     67  9.22   60.0
		self.Tree4 = TreeNode(
			86400,
			left=TreeNode(
				'r',
				left=TreeNode('k'),
				right=TreeNode(
					'm',
					left=TreeNode(67),
					right=TreeNode(9.22)
				)
			),
			right=TreeNode(
				365.2422,
				right=TreeNode(
					1440,
					right=TreeNode(60.0)
				)
			)
		)

		# Build first randomized tree:
		# This is a medium-sized, random-int tree. It resembles;
		#          RI1
		#        /     \
		#     RI2       RI5
		#    /   \     /   \ 
		#  RI3   RI4 RI6   RI7
		# RI5 and its children will always be negative; the rest will always be positive.
		self.Tree5Items = RI1, RI2, RI3, RI4, RI5, RI6, RI7 = [randint(1, 100) for i in range(4)] + [randint(-100, -1) for j in range(3)]
		self.Tree5 = TreeNode(
			RI1,
			left=TreeNode(
				RI2,
				left=TreeNode(RI3),
				right=TreeNode(RI4)
			),
			right=TreeNode(
				RI5,
				left=TreeNode(RI6),
				right=TreeNode(RI7)
			)
		)

		# Build second randomized tree:
		# This is a medium-sized, random-string tree. It resembles;
		#          RS1
		#        /     \
		#     RS2       RS4
		#    /         /   \ 
		#  RS3       RS5   RS6
		# All strings are 6 characters long and contain random combos of lowercase letters.
		self.Tree6Items = RS1, RS2, RS3, RS4, RS5, RS6 = [''.join(choices(ascii_lowercase, k=6)) for i in range(6)]
		self.Tree6 = TreeNode(
			RS1,
			left=TreeNode(
				RS2,
				left=TreeNode(RS3)
			),
			right=TreeNode(
				RS4,
				left=TreeNode(RS5),
				right=TreeNode(RS6)
			)
		)



	def test_height(self):
		"""Asserts that the height of each tree is correct."""
		self.assertEqual(height(self.Tree1), 2)
		self.assertEqual(height(self.Tree2), 3)
		self.assertEqual(height(self.Tree3), 2)
		self.assertEqual(height(self.Tree4), 3)
		self.assertEqual(height(self.Tree5), 2)
		self.assertEqual(height(self.Tree6), 2)



	def test_size(self):
		"""Asserts that the size of each tree is correct."""
		self.assertEqual(size(self.Tree1), 4)
		self.assertEqual(size(self.Tree2), 8)
		self.assertEqual(size(self.Tree3), 5)
		self.assertEqual(size(self.Tree4), 9)
		self.assertEqual(size(self.Tree5), 7)
		self.assertEqual(size(self.Tree6), 6)



	def test_find_min(self):
		"""Asserts that the minimum value in each tree is correct or within reason (for RNG trees)."""
		self.assertEqual(find_min(self.Tree1), 0)
		self.assertEqual(find_min(self.Tree2), 3)
		self.assertEqual(find_min(self.Tree3), 'a')
		# Ignore Tree 4; you can't compare mixed types
		self.assertIn(find_min(self.Tree5), range(-100, 0)) # check that tree 5's min is acceptable
		self.assertIn(find_min(self.Tree5), self.Tree5Items) # check that tree 5's min is in the tree
		self.assertIn(find_min(self.Tree6), self.Tree6Items) # check that tree 6's min is in the tree



	def test_find_max(self):
		"""Asserts that the maximum value in each tree is correct or within reason (for RNG trees)."""
		self.assertEqual(find_max(self.Tree1), 6)
		self.assertEqual(find_max(self.Tree2), 143)
		self.assertEqual(find_max(self.Tree3), 't')
		# Ignore Tree 4; you can't compare mixed types
		self.assertIn(find_max(self.Tree5), range(1, 101)) # check that tree 5's max is acceptable
		self.assertIn(find_max(self.Tree5), self.Tree5Items) # check that tree 5's max is in the tree
		self.assertIn(find_max(self.Tree6), self.Tree6Items) # check that tree 6's max is in the tree



	def test_contains(self):
		"""Asserts that each tree does or doesn't contain specific items."""
		# Tree 1
		self.assertTrue(contains(self.Tree1, 0)) # Tree 1: test root item
		self.assertTrue(contains(self.Tree1, 4)) # Tree 1: test non-root non-leaf
		self.assertTrue(contains(self.Tree1, 2)) # Tree 1: test leaf
		self.assertFalse(contains(self.Tree1, 7)) # Tree 1: test non-item

		# Tree 2
		self.assertTrue(contains(self.Tree2, 131)) # Tree 2: test root item
		self.assertTrue(contains(self.Tree2, 5)) # Tree 2: test non-root non-leaf
		self.assertTrue(contains(self.Tree2, 113)) # Tree 2: test leaf
		self.assertFalse(contains(self.Tree2, 24)) # Tree 2: test non-item

		# Tree 3
		self.assertTrue(contains(self.Tree3, 'k')) # Tree 3: test root item
		self.assertTrue(contains(self.Tree3, 'm')) # Tree 3: test non-root non-leaf
		self.assertTrue(contains(self.Tree3, 'a')) # Tree 3: test leaf
		self.assertFalse(contains(self.Tree3, 'f')) # Tree 3: test non-item

		# Tree 4
		self.assertTrue(contains(self.Tree4, 86400)) # Tree 4: test root item
		self.assertTrue(contains(self.Tree4, 'm')) # Tree 4: test non-root non-leaf
		self.assertTrue(contains(self.Tree4, 9.22)) # Tree 4: test leaf
		self.assertFalse(contains(self.Tree4, 'gg')) # Tree 4: test non-item

		# Tree 5
		for item in self.Tree5Items: # Test all items in it
			self.assertTrue(contains(self.Tree5, item))
		
		for i in range(3):
			while True: # Find a string that's not already in there
				n = randint(-100, 100)
				if n not in self.Tree5Items: break
			self.assertFalse(contains(self.Tree5, n)) # Test it's not in there
  
		# Tree 6
		for item in self.Tree6Items: # Test all items in it
			self.assertTrue(contains(self.Tree6, item))
		
		for i in range(3):
			while True: # Find a string that's not already in there
				s = ''.join(choices(ascii_lowercase, k=6))
				if s not in self.Tree6Items: break
			self.assertFalse(contains(self.Tree6, s)) # Test it's not in there



	def test_in_order(self):
		"""Asserts that the in-order representation of each of the predetermined trees is correct."""
		self.assertEqual(in_order(self.Tree1), [4, 2, 0, 6])
		self.assertEqual(in_order(self.Tree2), [9, 15, 113, 131, 143, 13, 5, 3])
		self.assertEqual(in_order(self.Tree3), ['t', 'a', 'k', 'm', 'h'])
		self.assertEqual(in_order(self.Tree4), ['k', 'r', 67, 'm', 9.22, 86400, 365.2422, 1440, 60.0])



	def test_pre_order(self):
		"""Asserts that the pre-order representation of each of the predetermined trees is correct."""
		self.assertEqual(pre_order(self.Tree1), [0, 4, 2, 6])
		self.assertEqual(pre_order(self.Tree2), [131, 15, 9, 113, 143, 5, 13, 3])
		self.assertEqual(pre_order(self.Tree3), ['k', 't', 'a', 'm', 'h'])
		self.assertEqual(pre_order(self.Tree4), [86400, 'r', 'k', 'm', 67, 9.22, 365.2422, 1440, 60.0])



	def test_post_order(self):
		"""Asserts that the post-order representation of each of the predetermined trees is correct."""
		self.assertEqual(post_order(self.Tree1), [2, 4, 6, 0])
		self.assertEqual(post_order(self.Tree2), [9, 113, 15, 13, 3, 5, 143, 131])
		self.assertEqual(post_order(self.Tree3), ['a', 't', 'h', 'm', 'k'])
		self.assertEqual(post_order(self.Tree4), ['k', 67, 9.22, 'm', 'r', 60.0, 1440, 365.2422, 86400])



	def test_count_failures(self):
		"""Asserts that the number of times various lambda conditionals fail, for each tree, is correct."""
		# Define various useful lambdas
		is_int = lambda x: type(x) == int
		is_float = lambda x: type(x) == float
		is_string = lambda x: type(x) == str
		is_even_int = lambda x: is_int(x) and x % 2 == 0
		is_single_char = lambda x: len(str(x)) == 1

		# Test with each relevant tree - is_int
		self.assertEqual(count_failures(is_int, self.Tree1), 0)
		self.assertEqual(count_failures(is_int, self.Tree2), 0)
		self.assertEqual(count_failures(is_int, self.Tree3), 5)
		self.assertEqual(count_failures(is_int, self.Tree4), 6)
		self.assertEqual(count_failures(is_int, self.Tree5), 0)
		self.assertEqual(count_failures(is_int, self.Tree6), 6)

		# Test with each relevant tree - is_float
		self.assertEqual(count_failures(is_float, self.Tree1), 4)
		self.assertEqual(count_failures(is_float, self.Tree2), 8)
		self.assertEqual(count_failures(is_float, self.Tree3), 5)
		self.assertEqual(count_failures(is_float, self.Tree4), 6)
		self.assertEqual(count_failures(is_float, self.Tree5), 7)
		self.assertEqual(count_failures(is_float, self.Tree6), 6)

		# Test with each relevant tree - is_string
		self.assertEqual(count_failures(is_string, self.Tree1), 4)
		self.assertEqual(count_failures(is_string, self.Tree2), 8)
		self.assertEqual(count_failures(is_string, self.Tree3), 0)
		self.assertEqual(count_failures(is_string, self.Tree4), 6)
		self.assertEqual(count_failures(is_string, self.Tree5), 7)
		self.assertEqual(count_failures(is_string, self.Tree6), 0)

		# Test with each relevant tree - is_even_int
		self.assertEqual(count_failures(is_even_int, self.Tree1), 0)
		self.assertEqual(count_failures(is_even_int, self.Tree2), 8)
		self.assertEqual(count_failures(is_even_int, self.Tree3), 5)
		self.assertEqual(count_failures(is_even_int, self.Tree4), 7)

		# Test with each relevant tree - is_single_char
		self.assertEqual(count_failures(is_single_char, self.Tree1), 0)
		self.assertEqual(count_failures(is_single_char, self.Tree2), 5)
		self.assertEqual(count_failures(is_single_char, self.Tree3), 0)
		self.assertEqual(count_failures(is_single_char, self.Tree4), 6)



	def triple_tree_test(self, new_trees):
		"""Asserts that each tree provided in new_trees is correct when each item is tripled using a lambda."""

		# Test with Tree 1: should return the following tree;
		#        0
		#      /   \
		#     12   18
		#      \
		#		6
		TripledTree1 = new_trees[0]
		self.assertEqual(TripledTree1.data, 0)
		# Left
		self.assertEqual(TripledTree1.left.data, 12)
		self.assertEqual(TripledTree1.left.right.data, 6)
		# Right
		self.assertEqual(TripledTree1.right.data, 18)

		# Test with Tree 2: should return the following tree;
		#        393
		#       /   \
		#      45   429
		#     / \     \
		# 	27  339   15
		#            /  \
		#           39   9
		TripledTree2 = new_trees[1]
		self.assertEqual(TripledTree2.data, 393)
		# Left
		self.assertEqual(TripledTree2.left.data, 45)
		self.assertEqual(TripledTree2.left.left.data, 27)
		self.assertEqual(TripledTree2.left.right.data, 339)
		# Right
		self.assertEqual(TripledTree2.right.data, 429)
		self.assertEqual(TripledTree2.right.right.data, 15)
		self.assertEqual(TripledTree2.right.right.left.data, 39)
		self.assertEqual(TripledTree2.right.right.right.data, 9)

		# Test with Tree 3: should return the following tree;
		#       'kkk'
		#      /     \
		#   'ttt'   'mmm'
		#      \       \ 
		#	  'aaa'   'hhh'
		TripledTree3 = new_trees[2]
		self.assertEqual(TripledTree3.data, 'kkk')
		# Left
		self.assertEqual(TripledTree3.left.data, 'ttt')
		self.assertEqual(TripledTree3.left.right.data, 'aaa')
		# Right
		self.assertEqual(TripledTree3.right.data, 'mmm')
		self.assertEqual(TripledTree3.right.right.data, 'hhh')

		# Test with Tree 4: should return the following tree;
		#        259200
		#       /      \
		#     'rrr'  1095.7266
		#    /     \      \
		#  'kkk'  'mmm'   4320
		#         /   \      \
		#       201  27.66  180.0
		TripledTree4 = new_trees[3]
		self.assertEqual(TripledTree4.data, 259200)
		# Left
		self.assertEqual(TripledTree4.left.data, 'rrr')
		self.assertEqual(TripledTree4.left.left.data, 'kkk')
		self.assertEqual(TripledTree4.left.right.data, 'mmm')
		self.assertEqual(TripledTree4.left.right.left.data, 201)
		self.assertAlmostEqual(TripledTree4.left.right.right.data, 27.66)
		# Right
		self.assertAlmostEqual(TripledTree4.right.data, 1095.7266)
		self.assertEqual(TripledTree4.right.right.data, 4320)
		self.assertEqual(TripledTree4.right.right.right.data, 180.0)



	def test_tree_map(self):
		"""Asserts that each tree returned by tree_map() when a lambda is applied to all of its elements is correct."""
		# Define another lambda
		triple = lambda x: x * 3

		# Use it on each tree
		TripledTree1 = tree_map(triple, self.Tree1)
		TripledTree2 = tree_map(triple, self.Tree2)
		TripledTree3 = tree_map(triple, self.Tree3)
		TripledTree4 = tree_map(triple, self.Tree4)

		# Test that these are correct
		self.triple_tree_test((TripledTree1, TripledTree2, TripledTree3, TripledTree4))
		

	def test_tree_apply(self):
		"""Asserts that each tree is mutated correctly when a lambda is applied to all of its elements."""
		# Define another lambda
		triple = lambda x: x * 3

		# Use it on each tree
		TripledTree1 = deepcopy(self.Tree1)
		TripledTree2 = deepcopy(self.Tree2)
		TripledTree3 = deepcopy(self.Tree3)
		TripledTree4 = deepcopy(self.Tree4)
		tree_apply(triple, TripledTree1)
		tree_apply(triple, TripledTree2)
		tree_apply(triple, TripledTree3)
		tree_apply(triple, TripledTree4)

		# Test that these are correct
		self.triple_tree_test((TripledTree1, TripledTree2, TripledTree3, TripledTree4))

if __name__ == "__main__":
	unittest.main()