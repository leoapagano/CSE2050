class Graph_ES:
	def __init__(self, vertices, edges):
		"""Constructor method for the edge set graph class."""
		self.vertices = set(vertices)
		self.edges = set(edges)

	
	def __len__(self):
		"""Determines the number of vertices in the graph."""
		return len(self.vertices)


	def __iter__(self):
		"""Iterates through the vertices in the graph."""
		for vertex in self.vertices:
			yield vertex


	def add_vertex(self, vertex):
		"""Add a vertex {vertex} to the graph."""
		self.vertices.add(vertex) # duh


	def remove_vertex(self, vertex):
		"""Remove a vertex {vertex} to the graph.
		If {vertex} is not found, raises a KeyError."""
		# Error handling
		if vertex not in self.vertices:
			raise KeyError(f"vertex {vertex} not found in edge set graph")

		# Remove relevant edges
		edges_to_remove = {edge for edge in self.edges if vertex in edge}
		self.vertices.remove(vertex)
		self.edges -= edges_to_remove


	def add_edge(self, edge):
		"""Add an edge {edge} to the graph."""
		self.edges.add(edge) # duh

	
	def remove_edge(self, edge):
		"""Remove an edge {edge} to the graph.
		If {edge} is not found, raises a KeyError."""
		# Error handling
		if edge not in self.edges and edge[::-1] not in self.edges:
			raise KeyError(f"edge {edge} not found in edge set graph")

		# Remove matching edge - we use discard instead of remove because only one may be present, and that's OK
		self.edges.discard(edge)
		self.edges.discard(edge[::-1])


	def _neighbors(self, vertex):
		"""In O(n) time, returns a set of the neighbors of vertex {vertex}."""
		# Check if all edges attach to that vertex, and if so, add them to neighbors
		neighbors = set()
		for edge in self.edges:
			if vertex in edge:
				# TO SUMMARIZE: remove the only item left when you turn that edge into a set and remove the relevant node
				neighbor = (set(edge) - {vertex}).pop()
				neighbors.add(neighbor)
		return neighbors



class Graph_AS:
	def __init__(self, vertices, edges):
		"""Constructor method for the adjacency set graph class."""
		# The core of this ADT is a dict {self.adjset} with keys (vertices) and values (the vertices they link to)
		self.adjset = {}

		# Add all vertices with empty sets
		for vertex in vertices:
			self.add_vertex(vertex)
		
		# Add all edges to their respective vertices
		for edge in edges:
			self.add_edge(edge)

	
	def __len__(self):
		"""Determines the number of vertices in the graph."""
		return len(self.adjset)


	def __iter__(self):
		"""Iterates through the vertices in the graph."""
		for vertex in self.adjset.keys():
			yield vertex


	def add_vertex(self, vertex):
		"""Add a vertex {vertex} to the graph."""
		# Add vertex if it's not there yet
		if vertex not in self.adjset:
			self.adjset[vertex] = set()


	def remove_vertex(self, vertex):
		"""Remove a vertex {vertex} to the graph.
		If {vertex} is not found, raises a KeyError."""
		# Error handling
		if vertex not in self.adjset:
			raise KeyError(f"vertex {vertex} not found in edge set graph")
		
		# Remove vertex
		self.adjset.pop(vertex)


	def add_edge(self, edge):
		"""Add an edge {edge} to the graph."""
		# Create set for the relevant vertex if the vertex does not exist yet
		if edge[0] not in self.adjset:
			self.adjset[edge[0]] = set()

		# Add edge
		self.adjset[edge[0]].add(edge[1])

	
	def remove_edge(self, edge):
		"""Remove an edge {edge} to the graph.
		If {edge} is not found, raises a KeyError."""
		# The relevant edge (2, 4), for example, would exist as an adjset entry as {2:{4,...}}
		from_vertex, to_vertex = edge[0], edge[1]

		# Error handling
		if from_vertex not in self.adjset:
			raise KeyError(f"edge {edge} not found in edge set graph")
		if to_vertex not in self.adjset[from_vertex]:
			raise KeyError(f"vertex {from_vertex} does not link to vertex {to_vertex}")
		
		# Remove vertex
		self.adjset[from_vertex].remove(to_vertex)


	def _neighbors(self, vertex):
		"""In O(1) time, returns a set of the neighbors of vertex {vertex}."""
		return self.adjset[vertex]