def binary_search_recr(L, item, left=0, right=None):
    """Recursively binary-searches a sorted list (L) for an item (item)."""
    if right is None: right=len(L)

    # base cases
    if right-left == 0:
        return False

    median_idx = (right+left) // 2
    if item > L[median_idx]:
        # must be to the right of the median
        return binary_search_recr(L, item, left=median_idx+1, right=right)
    elif item < L[median_idx]:
        # must be to the left of the median
        return binary_search_recr(L, item, left=left, right=median_idx)
    else:
        # must be a match
        return True
    

def binary_search_iter(L, item):
    """Iteratively binary-searches a sorted list (L) for an item (item)."""
    left=0
    right=len(L)
    
    while (right-left) > 0:
        median_idx = (right+left) // 2
        if item > L[median_idx]:
            # must be to the right of the median
            left=median_idx+1
        elif item < L[median_idx]:
            # must be to the left of the median
            right=median_idx
        else:
            # must be a match
            return True
    
    # Not found
    return False