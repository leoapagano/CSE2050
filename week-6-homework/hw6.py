def bubble_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Bubble Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    # Initalize if first run
    if n is None:
        n = len(arr)
    
    # Empty?
    if n == 0:
        return [], 0

    # At the end?
    if n == 1:
        return arr, num_swaps
    
    # Run algorithm if none of the above - each pass is 1 recursion
    has_sorted = False
    for i in range(n-1):
        first = arr[i]
        second = arr[i+1]
        # Out of order?
        if first > second: 
            # Swap items
            arr[i+1] = first
            arr[i] = second
            has_sorted = True
            num_swaps += 1
    
    # Run another recursion if anything bubbled up
    if has_sorted:
        return bubble_sort(arr, n=n-1, num_swaps=num_swaps)
    else:
        return (arr, num_swaps)



def selection_sort(arr, end=None, num_swaps=0):
    """
    Sorts an array using the recursive Selection Sort algorithm based on the largest element each time.

    Parameters:
        arr (list): The unsorted list to be sorted.
        end (int): The index up to which the sorting process is done.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    # Initalize if first run
    if end is None:
        end = len(arr) - 1

    # Empty?
    if end == -1:
        return [], 0

    # At the end?
    if end == 0:
        return arr, num_swaps
    
    # Run algorithm if none of the above
    # Start by finding index of highest remaining value
    max_index = end
    for i in range(end):
        if arr[i] > arr[max_index]:
            max_index = i

    # Is a switching not needed?
    if max_index == end:
        # No swap - do another recursion
        return selection_sort(arr, end=end-1, num_swaps=num_swaps)
    else:
        # Do a swap - then do another recursion
        max_val = arr[max_index]
        end_val = arr[end]
        arr[max_index] = end_val
        arr[end] = max_val
        return selection_sort(arr, end=end-1, num_swaps=num_swaps+1)
    


def insertion_sort(arr, n=None, num_swaps=0):
    """
    Sorts an array using the recursive Insertion Sort algorithm.

    Parameters:
        arr (list): The unsorted list to be sorted.
        n (int, optional): The length of the unsorted portion of the array. 
            Defaults to None, which implies the entire array length.
        num_swaps (int): The number of swaps made during the sorting process.

    Returns:
        tuple: A tuple containing the sorted array and the number of swaps.

    """
    # Initialize if first run
    if n is None:
        n = len(arr)

    # Done?
    if n <= 1:
        return arr, num_swaps

    # Sort the first n-1 elements, starting bottom-up recursively
    arr, num_swaps = insertion_sort(arr, n-1, num_swaps)

    # Insert the last element at its correct position in the sorted array
    current_last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > current_last:
        arr[j + 1] = arr[j]
        j -= 1

    num_swaps += 1
    arr[j + 1] = current_last

    return arr, num_swaps