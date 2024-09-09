def has_any_higher(L1, L2):
    """Returns True iff any item in L1 is greater than every item in L2"""
    for item1 in L1:
        # boolean flag: item1 > everything in L2
        has_max = True
        
        for item2 in L2:
            # if we find a bigger item, toggle the flag and break
            if item1 <= item2:
                has_max = False
                break

        # flag was never toggled - short circuit True
        if has_max:
            return True
    
    return False

def has_any_higher_fast(L1, L2):
    """O(m+n) version of has_any_higher(), which is O(mn)."""
    largestL2 = max(L2)

    for item in L1:
        if item > largestL2:
            return True
    
    return False