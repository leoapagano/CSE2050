
def breakdown(word):
    '''breakdown(word)
    Returns a dictionary containing each letter (keys) in input word,
    paired to the amount of times it appears in that word (values).

    Example use:
        > breakdown("helloworld")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}'''

    instances = {} # Empty list of character occurrances
    for character in word: 
        if character in instances:
            instances[character] += 1 # Increment existing character
        else:
            instances[character] = 1 # Add new character
    return instances


def is_anagram(word1, word2):
    '''is_anagram(word1, word2)
    A simple function. Checks if word1 and word2 are anagrams.
    Do I really need to say anything else?
    Essentially a reference implementation of breakdown().

    Example use:
        > is_anagram("shale", "leash")
        True
        > is_anagram("hello", "world")
        False'''
    
    # Anagrams have the same characters as each other in a different order.
    # Therefore, their breakdowns will be the same.
    return breakdown(word1) == breakdown(word2)