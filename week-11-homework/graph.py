from stack2050 import Stack as Stack2050
from queue2050 import Queue as Queue2050

class Graph:
	"""A basic graph class for use solely for the AdjacencySetGraph and EdgeSetGraph to inherit from.
	Do not use otherwise."""
	def __init__(self):
		"""Initializes the Graph class. Do not initialize a Graph directly."""
		raise NotImplementedError


	def connected(self, v1, v2, memo=None):
		"""Checks if vertices {v1} and {v2} are connected. Returns a boolean."""
		# Memoization
		if memo is None: memo = set()
		if v1 in memo: return False
		memo.add(v1)

		# Base case: match
		if v1 == v2: return True

		# Check all neighbors recursively
		for neighbor in self.neighbors(v1):
			if self.connected(neighbor, v2, memo):
				return True
		
		# Dead end or all branches failed
		return False


	def bfs(self, v):
		"""Performs a queue2050-based, breadth-first search from vertex {v}.
		Returns a search tree (as a dict)."""
		# Initialize queue & search tree
		BFSQueue = Queue2050()
		BFSQueue.enqueue((v, None))
		SearchTree = {}
		
		# Keep going until queue is emptied
		while not BFSQueue.is_empty():
			vertex, parent = BFSQueue.dequeue()
			# Only check for neighbors in non-indexed nodes
			if vertex not in SearchTree:
				SearchTree[vertex] = parent
				for neighbor in self.neighbors(vertex):
					BFSQueue.enqueue((neighbor, vertex))

		return SearchTree


	def dfs(self, v):
		"""Performs a stack2050-based, depth-first search from vertex {v}.
		Returns a search tree (as a dict)."""
		# Initialize stack & search tree
		DFSStack = Stack2050()
		DFSStack.push((v, None))
		SearchTree = {}
		
		# Keep going until stack is emptied
		while not DFSStack.is_empty():
			vertex, parent = DFSStack.pop()
			# Only check for neighbors in non-indexed nodes
			if vertex not in SearchTree:
				SearchTree[vertex] = parent
				neighbors = [n for n in self.neighbors(vertex)][::-1]
				for neighbor in neighbors:
					DFSStack.push((neighbor, vertex))
		return SearchTree


	def shortest_path(self, v1, v2):
		"""Identifies the shortest path between vertices {v1} and {v2}.
		Returns a tuple with the distance, and all relevant edges listed in order (in a list).
		If no such path is found, returns (float("inf"), None)."""
		# Initialize queue & search tree
		BFSQueue = Queue2050()
		BFSQueue.enqueue((v1, None))
		SearchTree = {}
		
		# Keep going until queue is emptied
		while not BFSQueue.is_empty():
			vertex, parent = BFSQueue.dequeue()
			# Only check for neighbors in non-indexed nodes
			if vertex not in SearchTree:
				SearchTree[vertex] = parent
				for neighbor in self.neighbors(vertex):
					BFSQueue.enqueue((neighbor, vertex))
		
		# Handle if not possible
		if v2 not in SearchTree: return (float("inf"), None)

		# Find quickest route from v2 to v1
		route = []
		curr_vertex = v2
		while curr_vertex is not v1:
			# Connected
			route.append((SearchTree[curr_vertex], curr_vertex))
			curr_vertex = SearchTree[curr_vertex]
		return len(route), route[::-1]


	def has_cycle(self):
		"""Locates a cycle or loop in the graph.
		If one is found, returns a tuple with; True, and another tuple listing all of the relevant edges, in order.
		If one is not found, returns (False, None)."""
		for vert_x in self:
			for vert_y in self:
				if vert_x != vert_y:
					if self.connected(vert_x, vert_y):
						if self.connected(vert_y, vert_x):
							path1 = self.shortest_path(vert_x, vert_y)[1]
							path2 = self.shortest_path(vert_y, vert_x)[1]
							return (True, path1 + path2)
		return (False, None)



class AdjacencySetGraph(Graph):
	"""An adjacency-set graph (stores vertices alongside their links)."""
	def __init__(self, V=None, E=None):
		"""Initializes the AdjacencySetGraph class with {V} vertices and {E} edges."""
		self.adjacency_set = {}
		if V is not None:
			for vertex in V: self.adjacency_set[vertex] = set()
		if E is not None:
			for edge in E: self.adjacency_set[edge[0]].add(edge[1])


	def __iter__(self):
		"""Iterates through an AdjacencySetGraph's vertices, returning an iterator."""
		for vertex in self.adjacency_set.keys():
			yield vertex


	def add_vertex(self, v):
		"""Adds a new vertex {v} to the AdjacencySetGraph. It will not be linked to other vertices by default."""
		if v not in self.adjacency_set.keys(): self.adjacency_set[v] = set()


	def add_edge(self, u, v):
		"""Adds a new edge to the AdjacencySetGraph, connecting existing vertices {u} and {v}."""
		if v not in self.adjacency_set[u]: self.adjacency_set[u].add(v)


	def neighbors(self, v):
		"""Iterates through all neighbors of vertex {v}, returning an iterator."""
		for vertex in sorted(self.adjacency_set[v]):
			yield vertex



class EdgeSetGraph(Graph):
	"""An edge-set graph (stores vertices and edges)."""
	def __init__(self, V=None, E=None):
		"""Initializes the EdgeSetGraph class with {V} vertices and {E} edges."""
		self.vertices = set() if V is None else set(V)
		self.edges = set() if E is None else set(E)


	def __iter__(self):
		"""Iterates through an EdgeSetGraph's vertices, returning an iterator."""
		for vertex in self.vertices:
			yield vertex


	def add_vertex(self, v):
		"""Adds a new vertex {v} to the EdgeSetGraph. It will not be linked to other vertices by default."""
		if v not in self.vertices: self.vertices.add(v)


	def add_edge(self, u, v):
		"""Adds a new edge to the EdgeSetGraph, connecting existing vertices {u} and {v}."""
		if (u, v) not in self.edges: self.edges.add((u, v))


	def neighbors(self, v):
		"""Iterates through all neighbors of vertex {v}, returning an iterator."""
		for edge in sorted(self.edges):
			if edge[0] == v:
				yield edge[1]