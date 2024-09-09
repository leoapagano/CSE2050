import unittest
from remove_characters import remove_characters

class TestRemoveCharacters(unittest.TestCase):
    '''Test cases for remove_characters().'''

    def test_equal_cases(self):
        """Test cases which should be equal"""
        self.assertEqual(remove_characters("credibility", "deck"), "ribility")
        self.assertEqual(remove_characters("negotiation", "lamp"), "negotition")
        self.assertEqual(remove_characters("operational", "dead"), "oprtionl")
        self.assertEqual(remove_characters("constituency", "flu"), "constitency")
        self.assertEqual(remove_characters("ambiguity", "worth"), "ambiguiy")

    def test_inequal_cases(self):
        """Test cases which should be inequal"""
        self.assertNotEqual(remove_characters("earthflax", "call"), "earthfax") # should be "erthfax"
        self.assertNotEqual(remove_characters("administration", "sick"), "admntration") # should be "admntraton"
        self.assertNotEqual(remove_characters("hypnotize", "spray"), "hymnotize") # should be "hnotize"
        self.assertNotEqual(remove_characters("ideology", "plug"), "ideally") # should be "ideooy"
        self.assertNotEqual(remove_characters("representative", "reprsntativ"), "res") # should be "rprsntativ"


if __name__ == "__main__":
    unittest.main()