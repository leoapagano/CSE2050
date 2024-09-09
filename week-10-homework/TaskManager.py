class Entry:
	"""Represents an entry in the priority queue."""
	def __init__(self, priority, process_id):
		"""Initializes an Entry object with a given priority and process ID."""
		self.priority = priority
		self.process_id = process_id


	def __repr__(self):
		"""Returns a string representation of the Entry object."""
		return f"Entry(priority={self.priority}, process_id={self.process_id})"


    ####### Implement all Entry class methods under this line #######
	def __gt__(self, other):
		"""Compares the priority of this entry with another entry.
		Returns:bool: True if this entry has higher priority than the other, False otherwise."""
		return self.priority > other.priority

		
	def __eq__(self, other):
		"""Checks if this entry is equal to another entry based on priority.
		Returns:bool: True if the priorities are equal, False otherwise."""
		return self.priority == other.priority



class MaxHeap:
	"""Represents a max heap data structure."""
	def __init__(self):
		"""Initializes a MaxHeap object."""
		self._heap = []


    ####### Implement all MaxHeap class methods under this line #######
	def put(self, entry):
		"""Inserts an entry into the max heap."""
		# Add
		self._heap.append(entry)

		# Verify heap property and upheap last item as needed
		self._upheap(len(self) - 1)


	def remove_max(self):
		"""Removes and returns the entry with the maximum priority from the max heap.
		Returns: The process ID that was removed from the queue. Raise an IndexError if the heap is empty"""
		if len(self) == 0:
			raise IndexError("remove_max from empty MaxHeap")
		
		# Take out first item
		self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
		item = self._heap.pop()

		# Downheap
		self._downheap(0)
		return item.process_id


	def change_priority(self, process_id, new_priority):
		"""Changes the priority of a process in the max heap.
		Returns:bool: True if the priority change was successful, False otherwise."""

		# Find index in self._heap
		for curr_idx, curr_entry in enumerate(self._heap):
			if curr_entry.process_id == process_id:
				# Success!
				old_priority = curr_entry.priority
				curr_entry.priority = new_priority

				# Upheap or downheap as needed
				if new_priority > old_priority:
					self._upheap(curr_idx)
				else:
					self._downheap(curr_idx)

				return True
		
		return False


	def _upheap(self, index):
		"""Performs up-heap operation to maintain heap property after insertion."""
		# Conditions that cause stopping:
		# Index curr_idx is zero; you can't upheap further than the parent node
		# Priority at index curr_idx <= priority at index (curr_idx-1) // 2 - heap property
		# Make sure to update curr_idx!
		curr_idx = index
		while curr_idx > 0 and self._heap[curr_idx].priority > self._heap[(curr_idx-1) // 2].priority:
			self._heap[curr_idx], self._heap[(curr_idx-1) // 2] = self._heap[(curr_idx-1) // 2], self._heap[curr_idx]
			curr_idx = (curr_idx-1) // 2


	def _downheap(self, index):
		"""Performs down-heap operation to maintain heap property after removal."""
		# List out all subtree items
		subtree = []
		if (index) in range(len(self._heap)): subtree.append(self._heap[index]) # Parent (if present)
		if (2*index + 1) in range(len(self._heap)): subtree.append(self._heap[2*index + 1]) # Left (if present)
		if (2*index + 2) in range(len(self._heap)): subtree.append(self._heap[2*index + 2]) # Right (if present)

		# Base case: current node is a dead end
		if len(subtree) in (0, 1): return

		# Base case: heap property maintained (largest item is parent)
		if max(subtree) is self._heap[index]: return

		# Recursive case: left node is biggest
		elif max(subtree) is self._heap[2*index+1]:
			self._heap[index], self._heap[2*index+1] = self._heap[2*index+1], self._heap[index]
			self._downheap(2*index+1)

		# Recursive case: right node is biggest
		else:
			self._heap[index], self._heap[2*index+2] = self._heap[2*index+2], self._heap[index]
			self._downheap(2*index+2)


	def __len__(self):
		"""len is number of items in PQ"""
		return len(self._heap)  



class TaskManager:
	"""Manages the execution of processes using a priority queue."""
	def __init__(self):
		"""Initializes a TaskManager object."""
		self.processor_queue = MaxHeap()


	####### Implement all TaskManager class methods under this line #######
	def add_process(self, entry):
		"""Adds a process to the processor queue."""
		# Attempt to change priority; if that fails, add
		if not self.processor_queue.change_priority(entry.process_id, entry.priority):
			self.processor_queue.put(entry)


	def remove_process(self):
		"""Removes and returns the process with the highest priority from the processor queue."""
		return self.processor_queue.remove_max()
	

	def __len__(self):
		"""len is number of items in PQ"""
		return len(self.processor_queue)