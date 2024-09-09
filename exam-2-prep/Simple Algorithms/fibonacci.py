def fib_tab(num):
    """Implements fibonacci using tabulation."""
    # In general, for tabulation: index (input):value (output)
    # In our case: index (num): value (fib_tab(num))

    # Short circuits
    if num == 0: return 0
    if num == 1: return 1

    # We create a table that can store the values for all fibonacci numbers between 0 and num.
    tab = [None] * (num+1)

    # Recall that for a fibonacci number, it's the sum of the last 2 numbers.
    # To start: tab[0] always 0, tab[1] always 1
    tab[0], tab[1] = 0, 1
    for i in range(2, num+1):
        tab[i] = tab[i-1] + tab[i-2]
    
    return tab[-1]



def fib_recr(num):
    """Implements fibonacci using recursion and w/o memoization."""
    # Base cases
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fib_recr_memo(num-1) + fib_recr_memo(num-2)



def fib_recr_memo(num, memo=None):
    """Implements fibonacci using recursion and memoization."""
    if memo is None:
        memo = [None] * num

    # Base cases
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    if memo[num-1] is None: 
        memo[num-1] = fib_recr_memo(num-1, memo)
    if memo[num-2] is None: 
        memo[num-2] = fib_recr_memo(num-2, memo)
    return memo[num-1] + memo[num-2]

