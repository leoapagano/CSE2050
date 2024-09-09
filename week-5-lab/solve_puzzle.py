def solve_puzzle(puzzle):
    """solve_puzzle(puzzle)
    Given a puzzle (list, tuple, or other iterable) containing a sequence of numbered "tiles",
    this algorithm attempts to find a solution to the puzzle. 
    (Puzzles start at the first tile, and move that many times clockwise OR counter clockwise;
    it should be possible to reach the last tile doing this.)
    Returns True if the puzzle can be solved, or False otherwise.
    Does NOT return the actual solution."""
    
    # Define branching function
    def _solve_both_branches(index):
        # Mark current branch as "in progress"
        in_progress_cache.add(index)

        # Branch exploration function: 
        def _explore_single_branch(single_index):
            single_value = puzzle[single_index]

            # Base cases: is there already a valid solution?
            if single_index in in_progress_cache: # Is this branch cached (either cache)? No need to recache if so
                return False
            elif single_index == len(puzzle) - 1: # Is this the end?
                return True
            elif single_value == 0: # Is this a stopping point not at the end?
                return False
            elif single_value == len(puzzle): # If this happens, there's an infinite loop: catch this
                return False
            else:
                # Recursively explore this branch; return True if a solution is found
                return _solve_both_branches(single_index)


        # Assign new indices (modulo needed to keep indices in bounds)
        index_CCW = (index - puzzle[index]) % len(puzzle)        
        status_CCW = _explore_single_branch(index_CCW) # Explore CCW branch

        if status_CCW:
            return True
        
        else: # Only compute CW branch if CCW branch fails - saves time
            # Assign new indices (modulo needed to keep indices in bounds)
            index_CW = (index + puzzle[index]) % len(puzzle)
            status_CW = _explore_single_branch(index_CW) # Explore CW branch

            return status_CW



    # QUICK EXITS
    # length is 0: invalid list
    if len(puzzle) == 0:
        return False
    # length is 1: automatically solved
    if len(puzzle) == 1:
        return True
    # first item is equal to length of list minus 1: automatically solved (go CW to solve)
    if len(puzzle) - 1 == puzzle[0]:
        return True
    # first item is equal to 1: automatically solved (go CCW to solve)
    if puzzle[0] == 1:
        return True


    # Memoization: both of these caches prevent infinite loops
    # Refer to memoization.png for an explanation
    in_progress_cache = set() # Indices that are currently in progress are here. 
    
    # Branch out from start, and see how it goes.
    return _solve_both_branches(0)