import unittest
from contains_permutation import contains_permutation

class TestContainsPermutation(unittest.TestCase):
    '''Test cases for contains_permutation().'''

    def test_true_cases(self):
        """Test cases which should be true"""
        self.assertTrue(contains_permutation('deteriorate', 'rate'))
        self.assertTrue(contains_permutation('accumulation', 'umlaut'))
        self.assertTrue(contains_permutation('hospitality', 'tailspit'))
        self.assertTrue(contains_permutation('taxicab', 'cab'))
        self.assertTrue(contains_permutation('vegetarian', 'etag'))

    def test_false_cases(self):
        """Test cases which should be false"""
        self.assertFalse(contains_permutation('liability', 'label'))
        self.assertFalse(contains_permutation('nationalism', 'state'))
        self.assertFalse(contains_permutation('credibility', 'red zone'))
        self.assertFalse(contains_permutation('refrigerator', 'administrator'))
        self.assertFalse(contains_permutation('manufacturer', 'factual man'))


if __name__ == "__main__":
    unittest.main()