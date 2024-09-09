def ascii_arrayify(text):
    '''ascii_arrayify(text)
    Converts a string "text" into an array of how much each ASCII character in it is used. 
    This is especially useful for checking if two pieces of text are definitely, certainly permutations of each other.
    Returns a list.
    O(n) complexity.'''
    array = [0] * 256
    for char in text:
        array[ord(char)] += 1
    return array

def contains_permutation(input_string, pattern):
    '''contains_permutation(input_string, pattern)
    Takes two inputs; a string "input_string" and another string "pattern".
    If any consecutive set of characters in "input_string" is any permutation of "pattern",
    e.g. if you put in "trex" and "extract" you will get true because "trex" is a permutation of "extr".
    Returns as a boolean.
    O(n) complexity (with respect to "input_string").'''
    # Length of "target" and "frame"
    len_target, len_frame = len(input_string), len(pattern)
    
    # Fastest check: are they literally the same?
    if input_string == pattern:
        return True # Short circuit

    # Catch bad length edge case - also ensures slowest check below is O(n) and not O(m+n)
    if len_target <= len_frame:
        return False # Short circuit
    
    # If you're still here, the pattern must be shorter than the frame; in which case any remaining complexity dependent on the pattern length is now instead dependent on the input string length. Thus, this algorithm is O(n) complexity.
    # In the event that the slowest check is needed, we use a simple ASCII array (I hope you don't use Unicode!) to store counts of each item in the pattern.
    pattern_array = ascii_arrayify(pattern)

    # Generate each "frame" of input_string
    for i in range(len_target-len_frame+1):
        current_frame = input_string[i:i+len_frame]

        # Faster check: is this frame the exact same as the pattern?
        if current_frame == pattern:
            return True # Short circuit

        # Slower check: are they sets with the same number of unique characters as their length (are there no duplicates?) 
        # Converting to a set strips duplicates, but if there are no duplicate characters in either the frame or the pattern, then the set will be the same length as the frames
        scf = set(current_frame)
        sp = set(pattern)
        if scf == sp and len(scf) == len(sp):
            return True # Short circuit

        # Slower check: are they permutations with repeating characters that are used the same number of times?
        # We use the same ASCII method we used in the original pattern, and compare the two. If they're permutations, they must be the same.
        if pattern_array == ascii_arrayify(current_frame):
            return True # Short circuit

    # If you've been through every frame and found nothing, there's no permutations.
    return False