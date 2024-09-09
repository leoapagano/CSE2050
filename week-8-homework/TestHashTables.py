import unittest, random
random.seed(658)
from SeparateChainingHashTable import SeparateChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable

class TestHashTableFactory:
    def setUp(self, hash_table):
        """Set up test cases for use with a hash table object {hash_table}."""
        self.hash_table = hash_table
    

    def append_items(self, ht, refdict, n):
        """Given a dict {refdict} and a hash table object {ht}, adds {n} items and tests that it works."""
        # Generate up to 50 different random items to use as keys and values.
        # For each item;
        for i in range(n):
            # Get random key:value and save it for later
            key = random.randint(-100, 100)
            value = random.randint(-100, 100)

            # If key NOT in use, test it is not there yet (using 'in' and ht[key] - catch a KeyError for the latter)
            if key not in refdict:
                self.assertFalse(key in ht)
                with self.assertRaises(KeyError):
                    x = ht[key]

            # add it
            refdict[key] = value
            ht[key] = value

            # test that it is there (using 'in' and ht[i])
            self.assertTrue(key in ht)
            self.assertEqual(value, ht[key])

            # test that the length of ht is correct
            self.assertEqual(len(ht), len(refdict))
            
            # test that the load factor is in an acceptable range
            LF = ht.get_loadfactor()
            self.assertTrue(LF >= ht.min_lf) # above min
            self.assertTrue(LF <= ht.max_lf) # below max


    def remove_items(self, ht, refdict, n):
        """Given a populated dict {refdict} and a populated hash table object {ht}, removes {n} random items and tests that it works."""
        # Now, remove a random 30 items from this hash table.
        # For each item;
        for i in range(n):
            # pick a random item to remove
            key = random.choice(list(refdict))
            value = refdict[key]

            # test that removing it returns the right item
            rm = ht.pop(key)
            self.assertEqual(value, rm)
            del refdict[key]

            # test it is not there anymore (using 'in' and ht[key] - catch a KeyError for the latter)
            self.assertFalse(key in ht)
            with self.assertRaises(KeyError):
                x = ht[key]
            
            # test that the length of ht is correct
            self.assertEqual(len(ht), len(refdict))

            # test that the load factor is in an acceptable range
            LF = ht.get_loadfactor()
            self.assertTrue(LF >= ht.min_lf) # above min
            self.assertTrue(LF <= ht.max_lf) # below max


    def test_put_get_sequential(self):
        """Iteratively add items, and test that various dunder methods return the correct linked hash table."""
        ht = self.hash_table()
        refdict = {}
        self.append_items(ht, refdict, 50)


    def test_put_get_remove_sequential(self):
        """Iteratively add items, like in test_put_get_sequential, then pop items that do and don't exist, ensuring they return the correct results."""
        ht = self.hash_table()
        refdict = {}
        self.append_items(ht, refdict, 50)
        self.remove_items(ht, refdict, 30)


class TestSeparateChainingHashTable(TestHashTableFactory, unittest.TestCase):
    """Test cases for the separate chaining-based hash table"""
    def setUp(self):
        super().setUp(SeparateChainingHashTable)
    
class TestLinearProbingHashTable(TestHashTableFactory, unittest.TestCase):
    """Test cases for the linear probing-based hash table"""
    def setUp(self):
        super().setUp(LinearProbingHashTable)

if __name__ == '__main__':
    unittest.main()