def remove_characters(input_string, to_remove):
    '''remove_characters(input_string, to_remove)
    Removes all characters in a string to_remove from another string input_string.
    It does not just remove instances of the full string, but instances of each individual char.
    Returns as a string.
    O(n) complexity (with respect to "input_string").'''
    # Conversion from string to set is O(1)
    denylist = set(to_remove)

    # Initialize output string
    output_string = ''
    # For each character in the input string (O(n))...is it in the denylist?
    # Checking if a set contains something is O(1) because it does not iterate sequentially; it iterates through a hash mapping
    for char in input_string:
        if char not in denylist:
            output_string += char

    return output_string