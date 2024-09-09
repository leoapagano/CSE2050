def ways_to_sum_memo(n, total, memo=None):
    """Calculates the number of different ways to sum up values on an "n"-sided die to "total".
    Uses memoization."""
    # Base cases:
    # Initialize empty memo if needed (don't use mutables as defaults!)
    if memo is None:
        memo = {}
    # Threshold met
    if total == 0:
        return 1
    # Threshold not met
    if total < 0:
        return 0
    # Already memoized
    if (n, total) in memo:
        return memo[(n, total)]
    
    # If base cases are not met, run the calculation...
    count = 0
    for i in range(1, min(n, total) + 1):
        count += ways_to_sum_memo(n, total-i, memo)
    
    # ...and memoize this value
    memo[(n, total)] = count
    return count


def ways_to_sum_tab(n, total):
    """Calculates the number of different ways to sum up values on an "n"-sided die to "total".
    Uses tabulation, but not memoization."""
    side_values = [i for i in range(1, total + 1)]

    # Initialize a 2D array to store the results
    # Array starts at 1, and is filled with zeroes the rest of the way
    results_tab = [1] + [0]*(total)

    # Fill in the results_tab array using bottom-up approach
    for current_total in side_values:
        i = 0
        for roll_value in range(1, min(n, current_total)+1):
            # Example: a six sided die has five rolls for the first side, four rolls for the second side, etc.
            i += results_tab[current_total - roll_value]
        results_tab[current_total] = i
    return results_tab[total]