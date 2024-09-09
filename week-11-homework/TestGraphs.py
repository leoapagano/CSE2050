from graph import AdjacencySetGraph, EdgeSetGraph
import unittest

class GraphTestFactory:
	"""Graph test case factory."""
	def setUp(self, graph_type):
		"""Configure test case factory for use with the AdjacencySetGraph."""
		self.graph_type = graph_type
		self.build_graphs()
	

	def build_graphs(self):
		"""Build several graphs."""
		# An empty graph.
		# (empty)
		self.empty_graph = self.graph_type()
		
		# A 1-item graph.
		# 14
		V = {14}
		E = {}
		self.island = self.graph_type(V, E)
		
		# A 2-item linear graph.
		# 6 -> 13
		V = {6, 13}
		E = {(6, 13)}
		self.single_link = self.graph_type(V, E)
		
		# A 3-item linear graph.
		# "H1" <-> "O" <-> "H2"
		V = {"H1", "H2", "O"}
		E = {("H1", "O"), ("H2", "O"), ("O", "H1"), ("O", "H2")}
		self.h2o = self.graph_type(V, E)
		
		# A 4-item graph with many connections.
		# 4 - - - > 8
		# ^  \   /  |
		# |    X    |
		# | </   \> V
		# 2 < - - - 9
		V = {2, 4, 8, 9}
		E = {(2, 4), (4, 8), (4, 9), (8, 2), (8, 9), (9, 2)}
		self.cross_box = self.graph_type(V, E)
		
		# An 8-item, (mostly) tree-shaped graph.
		#       "A"
		#      /   \
		#     V     V
		#   "B"     "D" <- "X" <- "Y"
		#   /       / \
		#  V       V   V
		# "C"    "E"   "F"
		V = {"A", "B", "C", "D", "E", "F", "X", "Y"}
		E = {("A", "B"), ("B", "C"), ("A", "D"), ("D", "E"), ("D", "F"), ("Y", "X"), ("X", "D")}
		self.tree_graph = self.graph_type(V, E)
	

	def test_neighborhood(self):
		"""Test that the custom graph classes have a working neighborhood() implementation."""
		# Empty graph: SKIP

		# Island graph: test vertex 14 
		self.assertEqual(sorted([n for n in self.island.neighbors(14)]), [])

		# Single-link graph: test vertex 6
		self.assertEqual(sorted([n for n in self.single_link.neighbors(6)]), [13])

		# H2O graph: test vertices "O" and "H1"
		self.assertEqual(sorted([n for n in self.h2o.neighbors("O")]), ["H1", "H2"])
		self.assertEqual(sorted([n for n in self.h2o.neighbors("H1")]), ["O"])

		# Cross-box graph: test vertices 8 and 9
		self.assertEqual(sorted([n for n in self.cross_box.neighbors(8)]), [2, 9])
		self.assertEqual(sorted([n for n in self.cross_box.neighbors(9)]), [2])

		# Tree-like graph: test vertices "A" and "D"
		self.assertEqual(sorted([n for n in self.tree_graph.neighbors("A")]), ["B", "D"])
		self.assertEqual(sorted([n for n in self.tree_graph.neighbors("D")]), ["E", "F"])


	def test_iter(self):
		"""Test that the custom graph classes can be iterated through correctly."""
		# Empty graph
		self.assertEqual(sorted([n for n in self.empty_graph]), [])

		# Island graph
		self.assertEqual(sorted([n for n in self.island]), [14])

		# Single-link graph
		self.assertEqual(sorted([n for n in self.single_link]), [6, 13])

		# H2O graph
		self.assertEqual(sorted([n for n in self.h2o]), ['H1', 'H2', 'O'])

		# Cross-box graph
		self.assertEqual(sorted([n for n in self.cross_box]), [2, 4, 8, 9])

		# Tree-like graph
		self.assertEqual(sorted([n for n in self.tree_graph]), ["A", "B", "C", "D", "E", "F", "X", "Y"])


	def test_BFS(self):
		"""Test that the custom graph classes have a working breadth-first search."""
		# Cross-box graph: start from 2 - intended result (we sort neighbors before adding):
		# 4 - - - > 8
		# ^ \     
		# |    \    
		# |       > 
		# 2         9
		intended = {2:None, 4:2, 8:4, 9:4}
		actual = self.cross_box.bfs(2)
		self.assertEqual(intended, actual)


	def test_DFS(self):
		"""Test that the custom graph classes have a working depth-first search."""
		# Cross-box graph: start from 2 - intended result (we sort neighbors before adding):
		# 4 - - - > 8
		# ^         |
		# |         |
		# |         V
		# 2         9
		intended = {2:None, 4:2, 8:4, 9:8}
		actual = self.cross_box.dfs(2)
		self.assertEqual(intended, actual)


	def test_shortest_path(self):
		"""Test that the custom graph classes have a working shortest_path() implementation."""
		# Empty graph: SKIP

		# Island graph: test 14 -> 14 (test length only)
		self.assertEqual(self.island.shortest_path(14, 14)[0], 0)

		# Single-link graph: test 6 -> 13 and 13 -> 6
		self.assertEqual(self.single_link.shortest_path(6, 13), (1, [(6, 13)]))
		self.assertEqual(self.single_link.shortest_path(13, 6), (float("inf"), None))

		# H2O graph: test "H2" -> "H1"
		self.assertEqual(self.h2o.shortest_path("H2", "H1"), (2, [("H2", "O"), ("O", "H1")]))

		# Cross-box graph: test 4 -> 2 and 8 -> 2 and 9 -> 4 (multiple possible combos - test length only)
		self.assertEqual(self.cross_box.shortest_path(4, 2)[0], 2)
		self.assertEqual(self.cross_box.shortest_path(8, 2)[0], 1)
		self.assertEqual(self.cross_box.shortest_path(9, 4)[0], 2)

		# Tree-like graph: test "A" -> "F" and "A" -> "Y"
		self.assertEqual(self.tree_graph.shortest_path("A", "F"), (2, [("A", "D"), ("D", "F")]))
		self.assertEqual(self.tree_graph.shortest_path("A", "Y"), (float("inf"), None))


	def test_has_cycle(self):
		"""Test that the custom graph classes have a working has_cycle() implementation."""
		# Empty graph
		self.assertEqual(self.empty_graph.has_cycle(), (False, None))

		# Island graph
		self.assertEqual(self.island.has_cycle(), (False, None))

		# Single-link graph
		self.assertEqual(self.single_link.has_cycle(), (False, None))

		# H2O graph - many possible loops may appear
		response = self.h2o.has_cycle()
		self.assertEqual(response[0], True)
		self.assertIn(response[1], ([("H1", "O"), ("O", "H1")], [("O", "H1"), ("H1", "O")], [("H2", "O"), ("O", "H2")], [("O", "H2"), ("H2", "O")]))

		# Cross-box graph - many possible loops may appear
		response = self.cross_box.has_cycle()
		self.assertEqual(response[0], True)
		self.assertIn(response[1], ([(2, 4), (4, 8), (8, 2)], [(4, 8), (8, 2), (2, 4)], [(8, 2), (2, 4), (4, 8)], [(2, 4), (4, 9), (9, 2)], [(4, 9), (9, 2), (2, 4)], [(9, 2), (2, 4), (4, 9)]))

		# Tree-like graph
		self.assertEqual(self.tree_graph.has_cycle(), (False, None))


	def test_connected(self):
		"""Test that the custom graph classes have a working connected() implementation."""
		# Empty graph: SKIP

		# Island graph: SKIP

		# Single-link graph: test 6 -> 13 and 13 -> 6
		self.assertEqual(self.single_link.connected(6, 13), True)
		self.assertEqual(self.single_link.connected(13, 6), False)

		# H2O graph: test "H1" -> "H2"
		self.assertEqual(self.h2o.connected("H1", "H2"), True)

		# Cross-box graph: test 4 -> 8 and 8 -> 4
		self.assertEqual(self.cross_box.connected(4, 8), True)
		self.assertEqual(self.cross_box.connected(8, 4), True)

		# Tree-like graph: test "Y" -> "E" and "E" -> "Y"
		self.assertEqual(self.tree_graph.connected("Y", "E"), True)
		self.assertEqual(self.tree_graph.connected("E", "Y"), False)


	def test_add_to_graph(self):
		"""Test that the custom graph classes can have vertices and edges added correctly."""
		pass



class TestAdjacencySetGraph(GraphTestFactory, unittest.TestCase):
	"""Test cases for the AdjacencySetGraph."""
	def setUp(self):
		"""Configure test case factory for use with the AdjacencySetGraph."""
		super().setUp(AdjacencySetGraph)



class TestEdgeSetGraph(GraphTestFactory, unittest.TestCase):
	"""Test cases for the EdgeSetGraph."""
	def setUp(self):
		"""Configure test case factory for use with the EdgeSetGraph."""
		super().setUp(EdgeSetGraph)



if __name__ == "__main__":
	unittest.main()