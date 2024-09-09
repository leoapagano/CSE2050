def bs(L, target, first=0, last=None):
    """bs(L, target)
    Binary searches a PRE-SORTED (ascending order) list L for an item target.
    Also accepts args first and last (used internally only) for fast slicing.
        Note: those are generally used internally only.
    If these are given, it will only search the list in that range.
    Returns True if target was found, or False if not."""
    # Is this the first time running? (i.e. default params)
    if last is None:
        last = len(L)

    print(f"Binary searching {L} for {target} on range {first} -> {last}")

    # Calculate size of list
    Lsize = last - first

    # Base cases:
    # Does the list have no items left?
    if Lsize == 0:
        return False
    
    # Does the list have one item left?
    elif Lsize == 1:
        return L[0] == target
    
    # Does the list have more than one item left?
    else:
        # Check middle item (floored if needed)
        middle = first + Lsize // 2
        print(f"Middle value: {middle} index = {L[middle]}")
        
        # Is this a match?
        if L[middle] == target:
            return True
        # Too big - search left hand side
        elif L[middle] > target:
            print(f"Too big - first={first}, last={middle}")
            return bs(L, target, first=first, last=middle)
        # Too small - earch right hand side
        elif L[middle] < target:
            print(f"Too little - first={middle}, last={last}")
            return bs(L, target, first=middle, last=last)