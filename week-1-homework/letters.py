from anagrams import breakdown
import string

def count_letters(file):
    '''count_letters(file)
    Given a file path at string file,
    it returns a dictionary containing each letter (keys) in input word,
    paired to the amount of times it appears in that word (values).

    This only counts lowercase characters (uppercase chars become lowercase),
    and does not count any other characters.

    Example use:
        > breakdown("helloworld.txt") # File helloworld.txt contains text "helloworld"
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}'''

    # Pull text from file
    with open(file) as f:
        filetxt = f.read()

    # Strip non-letters from text, converting uppercase to lowercase
    txt = ""
    for char in filetxt:
        if char in string.ascii_lowercase:
            txt += char
        elif char in string.ascii_uppercase:
            txt += char.lower()

    return breakdown(txt)

print(count_letters("frost.txt"))