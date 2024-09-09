import random

# DONE
def bubblesort(L, until=None):
	"""Bubblesort algorithm. Adaptive and stable.
	O(n^2) worst case time complexity. Sorts in place."""
	if until is None: until = len(L)

	# Base case
	if until <= 1:
		return

	# Single pass - swap w/ invariant trick
	for i in range(until-1):
		if L[i+1] < L[i]:
			L[i], L[i+1] = L[i+1], L[i]

	# Next recursion: sort list until {until-1}
	bubblesort(L, until=until-1)

# DONE
def selectionsort(L, until=None):
	"""Selectionsort algorithm. NOT adaptive and NOT stable.
	O(n^2) worst case time complexity. Sorts in place."""
	if until is None: until=len(L) # first run

	# base case(s)
	if until <= 1:
		return
	
	# find largest item index
	max_idx = 0
	for i in range(until):
		if L[max_idx] < L[i]:
			max_idx = i

	# move it to {until}'s index
	for i in range(max_idx, until-1):
		L[i], L[i+1] = L[i+1], L[i]

	# repeat again for until={until-1}
	selectionsort(L, until=until-1)

# DONE
def insertionsort(L, start=0):
	"""Insertionsort algorithm. Adaptive and stable.
	O(n^2) worst case time complexity. Sorts in place."""
	# base case(s)
	if start >= len(L) - 1:
		return
	
	# when start is 0, we move item 1
	# so on and so forth
	# when start is len(L) - 2, we move len(L)-1 (last item)

	current_idx = start + 1 # index of item being moved
	while (current_idx > 0) and (L[current_idx] < L[current_idx-1]): # is this < or <=?
		L[current_idx], L[current_idx-1] = L[current_idx-1], L[current_idx]
		current_idx -= 1

	# next iteration: start={start+1}
	insertionsort(L, start=start+1)

# DONE
def mergesort(L, start=0, until=None):
	"""Mergesort algorithm. NOT adaptive, but stable.
	O(nlogn) worst case time complexity. Sorts in place (excluding merging)."""
	def merge(L, start, mid, until):
		"""Merge algorithm for mergesort. Assumes there are two sorted lists in L of the form L[start:mid] and L[mid:until]."""
		# Copy list segments in memory
		lefthand = L[start:mid]
		righthand = L[mid:until]

		# "Zipper" merge into L
		i = j = 0 # Lefthand and righthand counters
		k = start # L counter
		while (i < len(lefthand)) and (j < len(righthand)):
			if lefthand[i] > righthand[j]:
				# add from righthand
				L[k] = righthand[j]
				j += 1
			else:
				# add from lefthand
				L[k] = lefthand[i]
				i += 1
			k += 1
		
		# Dump remaining contents of lefthand
		while i < len(lefthand):
			# add from lefthand
			L[k] = lefthand[i]
			i += 1
			k += 1

		# Dump remaining contents of righthand
		while j < len(righthand):
			# add from lefthand
			L[k] = righthand[j]
			j += 1
			k += 1


	if until is None: until = len(L)

	# Base case(s)
	if until - start <= 1:
		return

	# Pick a pivot
	pivot_idx = random.randrange(start, until)

	# Mergesort left half (recursion, yay!)
	mergesort(L, start=start, until=pivot_idx)
	
	# Mergesort right half (more recursion, yay!)
	mergesort(L, start=pivot_idx, until=until)

	# Merge halves
	merge(L, start, pivot_idx, until)

# DONE
def quicksort(L, start=0, until=None):
	"""Quicksort algorithm. NOT adaptive and NOT stable.
	O(n^2) worst case time complexity. Sorts in place."""
	def partition(L, start, pivot_idx, until):
		"""Partition function for quicksort."""
		# Move pivot to end
		if pivot_idx != until-1:
			L[pivot_idx], L[until-1] = L[until-1], L[pivot_idx]
			pivot_idx = until-1
		
		# For each item: is it above the pivot value?
		current_idx = start
		while current_idx < pivot_idx:
			if L[current_idx] > L[pivot_idx]:
				for i in range(current_idx, pivot_idx):
					L[i], L[i+1] = L[i+1], L[i]
				pivot_idx -= 1
			else:
				current_idx += 1
		
		return pivot_idx

	if until is None: until = len(L)

	# Base case(s)
	if until - start <= 1:
		return
	
	# Pick a pivot
	pivot_idx = random.randrange(start, until)
	pivot_idx = partition(L, start, pivot_idx, until)

	# Recursion, yay!
	quicksort(L, start=start, until=pivot_idx)
	quicksort(L, start=pivot_idx, until=until)




