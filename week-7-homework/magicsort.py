import math
from enum import Enum

# Pre-defined constant; independent of list input sizes
# Test cases may break if you set this to below 3 or at or above 20
INVERSION_BOUND = 10  
MAX_INSERTIONS = 20


class MagicCase(Enum):
    """MagicCase(i)
    An object based on the Enum class.
    Set a value for i from 0 to 3 to represent;
    i value         Representation
    0               General
    1               List already sorted
    2               Less than INVERSION_BOUND inversions needed
    3               Sorted, but in reverse
    """
    GENERAL = 0
    SORTED = 1
    CONSTANT_NUM_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L):
    """linear_scan(L)
    Takes a list "L" and returns a MagicCase object indicating what to do with it.
    Refer to MagicCase's class for more detailed info on which cases are which.
    Mostly used as part of magicsort."""
    # Iterate
    inversions = 0
    samesies = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]: # Out of order
            inversions += 1
        elif L[i] == L[i+1]:
            samesies += 1
    
    # Determine
    if len(L) == 0 or len(L) == 1: # For simple lists
        return MagicCase.SORTED
    elif inversions + samesies == len(L)-1: # Entire list out of order
        return MagicCase.REVERSE_SORTED
    elif inversions == 0: # List in order
        return MagicCase.SORTED
    elif inversions < INVERSION_BOUND: # Constant inversions
        return MagicCase.CONSTANT_NUM_INVERSIONS
    else:
        return MagicCase.GENERAL


def reverse_list(L, alg_set=None):
    """reverse_list(L, alg_set=None)
    Reverses a list in place with O(1) memory overhead and O(n) time complexity.
    It returns a list of algorithms used."""
    if alg_set is None:
        alg_set = {"reverse_list"}
    else:
        alg_set.add("reverse_list")

    # The Sorting Algorithm(TM)
    num_swaps = len(L) // 2
    for i in range(num_swaps):
        L[i], L[len(L)-1-i] = L[len(L)-1-i], L[i]

    return alg_set


def magic_insertionsort(L, left, right, alg_set=None):
    """magic_insertionsort(L, left, right, alg_set=None)
    Sorts a list using the insertion sort algorithm.
    If left and right are both None, the entire list is to be sorted.
    Otherwise, use them as range bounds for the regions of the list you want sorted.
    O(1) memory overhead.
    O(n) time complexity when CONSTANT_NUM_INVERSIONS applies, otherwise O(n^2) worst-case.
    It returns a list of algorithms used."""
    if alg_set is None:
        alg_set = {"magic_insertionsort"}
    else:
        alg_set.add("magic_insertionsort")

    # The Sorting Algorithm(TM)
    for next_idx in range(left + 1, right):
        target = L[next_idx]
        curr_idx = next_idx - 1

        # Find intended spot for current item
        while curr_idx >= left and L[curr_idx] > target:
            # Shift
            L[curr_idx + 1] = L[curr_idx]
            curr_idx -= 1
            
        # Insert
        L[curr_idx + 1] = target

    return alg_set


def merge(L, left, pivot, right):
    """Merges two unsorted halves of a list together, into one sorted list.
    Assumes the left part (before the pivot) contains items less than or equal to the pivot,
    and that the right part (after the pivot) contains items greater than the pivot.
    Only merges within the given left and right bounds."""
    # Old lists: we'll overwrite the existing one
    LL = L[left:pivot]
    RL = L[pivot:right]

    # Counters! i is left list counter, j is right list counter, k is existing list counter
    i = j = 0
    k = left

    # Iterate through all affected indices
    while i < len(LL) and j < len(RL):
        if LL[i] <= RL[j]:
            # add from left list
            L[k] = LL[i]
            i += 1
            k += 1
        else:
            # add from right list
            L[k] = RL[j]
            j += 1
            k += 1

    # Dump what remains of left list
    while i < len(LL):
        # add from left list
        L[k] = LL[i]
        i += 1
        k += 1

    # Dump what remains of right list
    while j < len(RL):
        # add from left list
        L[k] = RL[j]
        j += 1
        k += 1



def magic_mergesort(L, left, right, alg_set=None):
    """magic_mergesort(L, left, right, alg_set=None)
    Sorts a list using the insertion sort algorithm.
    If left and right are both None, the entire list is to be sorted.
    Otherwise, use them as range bounds for the regions of the list you want sorted.
    O(n) memory overhead. O(nlogn) worst-case time complexity.
    It returns a list of algorithms used."""
    if alg_set is None:
        alg_set = {"magic_mergesort"}
    else:
        alg_set.add("magic_mergesort")

    # The Sorting Algorithm(TM)
    if right - left <= MAX_INSERTIONS:
        # Base case - if the list is less than ~20 items, insertion outperforms
        magic_insertionsort(L, left, right)
    else:
        # Middle pivot
        pivot_index = (right+left) // 2
        # Recursion, yay!
        magic_mergesort(L, left, pivot_index)
        magic_mergesort(L, pivot_index, right)
        merge(L, left, pivot_index, right)

    return alg_set


def partition(L, left, right):
    """Partition function for quicksort.
    Returns the index, in L, where the pivot will be."""
    # Pivot is always the last item in the sublist
    pivot = L[right - 1]

    # Move all items greater than (but not equal to) the pivot to the end
    # Shift all items in between in place
    smaller_items = left - 1
    for i in range(left, right - 1):
        if L[i] <= pivot:
            smaller_items += 1
            # Swap
            L[smaller_items], L[i] = L[i], L[smaller_items]
    L[smaller_items + 1], L[right - 1] = L[right - 1], L[smaller_items + 1]

    return smaller_items + 1


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """magic_quicksort(L, left, right, depth=0, alg_set=None)
    Sorts a list using the quicksort algorithm.
    If left and right are both None, the entire list is to be sorted.
    Otherwise, use them as range bounds for the regions of the list you want sorted.
    Uses the last item in a sublist as the pivot, and tracks the recursion depth.
    It returns a set of algorithms used."""
    if alg_set is None:
        alg_set = {"magic_quicksort"}
    else:
        alg_set.add("magic_quicksort")

    # The Sorting Algorithm(TM)
    if right - left <= MAX_INSERTIONS:
        # Base case - if the list is less than ~20 items, insertion outperforms
        magic_insertionsort(L, left, right)
    elif depth >= 2 * (math.log2(right - left) + 1):
        # Base case - don't go too deep
        magic_mergesort(L, left, right)
    else:
        # Recursion, yay!
        pivot_index = partition(L, left, right)
        magic_quicksort(L, left, pivot_index, depth + 1)
        magic_quicksort(L, pivot_index + 1, right, depth + 1)

    return alg_set


def magicsort(L):
    """The magicsort algorithm, which intelligently picks from one of three sorting algs.
    It returns a set of all algorithms used."""
    listcase = linear_scan(L)
    if listcase == MagicCase.SORTED:
        return
    elif listcase == MagicCase.CONSTANT_NUM_INVERSIONS:
        return magic_insertionsort(L, 0, len(L))
    elif listcase == MagicCase.REVERSE_SORTED:
        return reverse_list(L)
    else: # Short circuit to GENERAL
        return magic_quicksort(L, 0, len(L))