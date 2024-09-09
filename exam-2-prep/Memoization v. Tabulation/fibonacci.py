def fibonacci_memo(N, memo=None):
	"""Returns the Nth fibonacci number, determined with memoization."""
	if memo is None: memo = [None] * N 

	# base cases
	if N in (0, 1):
		return N
	
	# recursion
	# determine fib(n-1) w/ memoization
	before = memo[N-1] if memo[N-1] is not None else fibonacci_memo(N-1, memo=memo)
	memo[N-1] = before # log
	# determine fib(n-2) w/ memoization
	evenbefore = memo[N-2] if memo[N-2] is not None else fibonacci_memo(N-2, memo=memo)
	memo[N-2] = evenbefore # log
	
	# fib(N) = fib(n-1) + fib(n-2)
	return before + evenbefore

def fibonacci_tab(N):
	"""Returns the Nth fibonacci number, determined with tabulation."""
	tab = [None for i in range(N)] # preallocate

	for i in range(N):
		# Base cases
		if i in (0, 1):
			tab[i] = i
		else:
			tab[i] = tab[i-1] + tab[i-2]

	# Compute solution
	return tab[N-1] + tab[N-2]

