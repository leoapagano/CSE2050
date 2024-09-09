def binary_search_recr(L, target, start=0, until=None):
	"""Checks if a PRE-SORTED list L contains an item target using a recursive binary search. Returns a boolean."""
	if until is None: until = len(L)

	if until-start == 0:
		return False

	median = (start+until) // 2

	if target > L[median]:
		# check right side
		return binary_search_recr(L, target, start=median+1, until=until)
	elif target < L[median]:
		# check left side
		return binary_search_recr(L, target, start=start, until=median)
	else:
		# It's a match!
		return True
