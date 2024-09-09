import time

def time_function(func, args, n_trials=10):
    """time_function(func, args, n_trials)
    Takes a function "func" and its arguments "args",
    and runs it "n_trials" (integer) times",
    returning the minimum time in seconds it took to complete (as a float).
    Complexity dependent on "func"."""
    minTime = float('inf')
    for i in range(n_trials):
        start = time.time()
        func(args)
        stop = time.time() - start
        minTime = stop if stop < minTime else minTime
    return minTime
    
def time_function_flexible(func, args, n_trials=10):
    """time_function(func, args, n_trials)
    Takes a function "func" and its arguments "args" (inside a tuple),
    and runs it "n_trials" (integer) times",
    returning the minimum time in seconds it took to complete (as a float).
    Complexity dependent on "func"."""
    minTime = float('inf')
    for i in range(n_trials):
        start = time.time()
        func(*args)
        stop = time.time() - start
        minTime = stop if stop < minTime else minTime
    return minTime


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))