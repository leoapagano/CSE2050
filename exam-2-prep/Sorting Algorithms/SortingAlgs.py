import random

# DONE
def bubblesort(L, until=None):
	"""Bubblesort algorithm. Adaptive and stable.
	O(n^2) worst case time complexity. Sorts in place."""
	if until is None: until = len(L)

	# Base case
	if until in (0, 1):
		return

	# One pass
	for i in range(until-1):
		if L[i+1] < L[i]:
			L[i], L[i+1] = L[i+1], L[i]

	# Next recursion - one more item to the right is already sorted
	bubblesort(L, until=until-1)

# DONE
def selectionsort(L, until=None):
	"""Selectionsort algorithm. NOT adaptive and NOT stable.
	O(n^2) worst case time complexity. Sorts in place."""
	if until is None: until = len(L)

	# Base case
	if until in (0, 1):
		return

	# Find maximum element index
	max_idx = 0
	for i in range(1, until):
		if L[i] > L[max_idx]:
			max_idx = i

	# Swap the last element in the list with that element
	L[max_idx], L[until-1] = L[until-1], L[max_idx]

	# Insertion sort the list again but without the last element
	selectionsort(L, until=until-1)

# DONE
def insertionsort(L, start=0):
	"""Insertionsort algorithm. Adaptive and stable.
	O(n^2) worst case time complexity. Sorts in place."""
	# Base cases
	if start >= len(L):
		return

	elif start != 0:
		# The item to be moved is at the index {start}
		current_idx = start

		# Move it move it
		while (L[current_idx-1] > L[current_idx]):
			L[current_idx], L[current_idx-1] = L[current_idx-1], L[current_idx]
			current_idx -= 1
			if current_idx == 0: break

	# Recursion time
	insertionsort(L, start=start+1)

# DONE
def mergesort(L, start=0, until=None):
	"""Mergesort algorithm. NOT adaptive, but stable.
	O(nlogn) worst case time complexity. Sorts in place (excluding merging)."""
	if until is None: until = len(L)

	# Base case
	if until - start <= 1:
		return

	# Pick a random pivot
	pivot_idx = random.randint(start, until-1)

	# Sort left half
	mergesort(L, start=start, until=pivot_idx)
	# Sort right half
	mergesort(L, start=pivot_idx, until=until)
	# Merge halves
	# i: current index in left half
	# j: current index in right half
	# k: current index in final list
	i = j = 0
	k = start
	Lh = L[start:pivot_idx]
	Rh = L[pivot_idx:until]
	# Zipper dump
	while i < len(Lh) and j < len(Rh):
		if Lh[i] > Rh[j]:
			L[k] = Rh[j]
			j += 1
		else:
			L[k] = Lh[i]
			i += 1
		k += 1
	# Dump left half
	while i < len(Lh):
		L[k] = Lh[i]
		i += 1
		k += 1
	# Dump right half
	while j < len(Rh):
		L[k] = Rh[j]
		j += 1
		k += 1

# DONE
def quicksort(L, start=0, until=None):
	"""Quicksort algorithm. NOT adaptive and NOT stable.
	O(n^2) worst case time complexity. Sorts in place."""
	if until is None: until = len(L)

	def _quickpartition(L, pivot_idx, start, until):
		"""Partitions a list L where the pivot is pre-provided."""
		# Move pivot to the end
		L[pivot_idx], L[until-1] = L[until-1], L[pivot_idx]
		pivot_idx = until-1

		current_idx = start
		while current_idx in range(start, until) and current_idx < pivot_idx: # i: each index in the list
			if L[current_idx] > L[pivot_idx]:
				# Shift to end if out of order
				for i in range(current_idx, pivot_idx):
					L[i], L[i+1] = L[i+1], L[i]

				pivot_idx -= 1
			else:
				current_idx += 1

		return pivot_idx

	# Base case
	if until - start <= 1:
		return

	# Partition (handles pivot)
	pivot_idx = random.randint(start, until-1)
	updated_pivot_idx = _quickpartition(L, pivot_idx, start, until)

	# Quicksort left half
	quicksort(L, start=start, until=updated_pivot_idx)

	# Quicksort right half
	quicksort(L, start=updated_pivot_idx+1, until=until)

# DONE
def quickselect(L, k, start=0, until=None):
	"""Quickselect algorithm. O(n^2) worst case time complexity. Operates in place.
	Locates the kth smallest item in a list L.
	Note that this will shuffle the order of L around somewhat."""
	if until is None: until, k = len(L), k-1 # first run: subtract 1 from k so that, e.g., 2nd largest item will look at index 1

	def _quickpartition(L, pivot_idx, start, until):
		"""Partitions a list L where the pivot is pre-provided."""
		# Move pivot to the end
		L[pivot_idx], L[until-1] = L[until-1], L[pivot_idx]
		pivot_idx = until-1

		current_idx = start
		while current_idx in range(start, until) and current_idx < pivot_idx: # i: each index in the list
			if L[current_idx] > L[pivot_idx]:
				# Shift to end if out of order
				for i in range(current_idx, pivot_idx):
					L[i], L[i+1] = L[i+1], L[i]

				pivot_idx -= 1
			else:
				current_idx += 1

		return pivot_idx

	# Base cases
	if (until-start) <= 1:
		return L[start]

	# Partition (handles pivot)
	pivot_idx = random.randint(start, until-1)
	updated_pivot_idx = _quickpartition(L, pivot_idx, start, until)

	# Quicksort only whichever half we need
	if k == updated_pivot_idx:
		return L[k]
	elif k < updated_pivot_idx:
		# Left half
		return quickselect(L, k, start=start, until=updated_pivot_idx)
	else:
		# Right half
		return quickselect(L, k, start=updated_pivot_idx+1, until=until)
	
