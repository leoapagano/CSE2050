def find_factors(list_of_numbers):
    """find_factors(list_of_numbers)
    Takes an iterable object (a list or tuple) "list_of_numbers" containing only positive integers,
    and returns a dictionary, where each key:value pair is;
        key: each input in list_of_numbers,
        value: a list of every factor of that number."""
    factor_table = {}

    for number in list_of_numbers:
        number = abs(number)
        factors = set()

        for i in range(1, number // 2 + 1): # Each pass looks for factors below and above number // 2
            if number % i == 0:
                factors.add(round(number/i))
                factors.add(i)

        factors.add(1)
        factors.add(number)
        factor_table[number] = sorted(factors)

    return factor_table