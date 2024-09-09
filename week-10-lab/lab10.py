class Entry:
	"""An entry for use inside a Priority Queue. Has an {item} and a {priority}."""
	def __init__(self, item, priority):
		"""Constructor method for the Entry class."""
		self.item = item
		self.priority = priority
	
	def __eq__(self, other):
		"""Equality checking magic method for the Entry class - compares priority *and* the item stored."""
		return self.priority == other.priority and self.item == other.item
	
	def __lt__(self, other):
		"""Comparison (less than) checking magic method for the Entry class - compares priority only."""
		return self.priority < other.priority



class PQ_UL:
	"""An Unordered Priority Queue object."""

	def __init__(self):
		"""Constructor method for the Unordered Priority Queue."""
		self._L = []
	
	def insert(self, item, priority):
		"""Add an item to the Unordered Priority Queue."""
		self._L.append(Entry(item, priority))
	
	def find_min(self):
		"""Return the lowest-priority item added to the Unordered Priority Queue."""
		if len(self) == 0: # Empty queue
			return
		else: # Queue with at least one item - proceed by starting at zero
			lowest_idx = 0
		
		# Find first lowest priority entry in queue
		for curr_idx, curr_entry in enumerate(self._L):
			if curr_entry < self._L[lowest_idx]:
				lowest_idx = curr_idx
		
		return self._L[lowest_idx]
  
	def remove_min(self):
		"""Return and remove the lowest-priority item added to the Unordered Priority Queue."""
		if len(self) == 0: # Empty queue
			return
		else: # Queue with at least one item - proceed by starting at zero
			lowest_idx = 0
		
		# Find first lowest priority entry in queue
		for curr_idx, curr_entry in enumerate(self._L):
			if curr_entry < self._L[lowest_idx]:
				lowest_idx = curr_idx
		
		return self._L.pop(lowest_idx)

	def __len__(self):
		"""Return the number of items in the Unordered Priority Queue."""
		return len(self._L)
  


class PQ_OL:
	"""An Ordered Priority Queue object."""

	def __init__(self):
		"""Constructor method for the Ordered Priority Queue."""
		self._L = []
	
	def insert(self, item, priority):
		"""Add an item to the Ordered Priority Queue."""
		self._L.append(Entry(item, priority))
		self._L.sort()
	
	def find_min(self):
		"""Return the lowest-priority item added to the Ordered Priority Queue."""
		return self._L[0]
  
	def remove_min(self):
		"""Return and remove the lowest-priority item added to the Ordered Priority Queue."""
		return self._L.pop(0)

	def __len__(self):
		"""Return the number of items in the Ordered Priority Queue."""
		return len(self._L)
