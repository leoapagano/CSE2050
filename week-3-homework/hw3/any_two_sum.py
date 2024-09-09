def any_two_sum(numbers, total):
    '''any_two_sum(numbers, total)
    Given a list or tuple "numbers" containing integers,
    and an integer "total",
    any_two_sum() checks if any two numbers in "numbers" add up to "total".
    Returns as a boolean.
    O(n) complexity (with respect to "numbers").'''
    # For every item in numbers, it subtracts that from the total
    # If that difference is in a set containing all the original numbers
    # AND IS NOT ALSO THE ORIGINAL NUMBER THAT WAS SUBTRACTED, it returns True.
    set_of_numbers = set(numbers) # This also has the nice effect of removing redundancy/duplicates
    for number in set_of_numbers:
        diff = total - number
        if diff in set_of_numbers and diff != number:
            return True
    # If none are found...
    return False