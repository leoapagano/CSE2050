import unittest
import random
import linkedlist


class TestNode(unittest.TestCase):
    '''Test cases for class Node().'''
    def testNodeInitialization(self):
        # Initialize
        int_data = random.randint(-10000, 10000)
        int_node = linkedlist.Node(int_data)

        # Test standalone node (does it initialize? can it store an int?)
        self.assertEqual(int_node.item, int_data)
        self.assertEqual(int_node.link, None)

    def testNodeRepr(self):
        # Initialize more data
        str_data = "The quick brown fox jumps over the lazy dog.\n"
        byte_data = random.randbytes(16)

        # Initialize more nodes
        str_node = linkedlist.Node(str_data)
        byte_node = linkedlist.Node(byte_data)

        # Test that both nodes work (can they store a string? bytes?)
        self.assertEqual(repr(str_node), f"Node({str_data})")
        self.assertEqual(repr(byte_node), f"Node({byte_data})")


class TestLinkedList(unittest.TestCase):
    '''Test cases for class LinkedList().
    And yes, I know this isn't as DRY as it could be...'''
    def testLinkedListEmptyInitialization(self):
        # Initialize blank linked list
        LL1 = linkedlist.LinkedList()

        # Test len(), get_head() and get_tail() on LL1
        self.assertEqual(len(LL1), 0)
        self.assertEqual(LL1.get_head(), None)
        self.assertEqual(LL1.get_tail(), None)

    def testLinkedListAddLast(self):
        # Initialize blank linked list
        LL2 = linkedlist.LinkedList()

        # Generate 4 random numbers and use a boolean and a string
        randos = [random.randint(-100000, 100000) for i in range(4)]
        randos.append(False)
        randos.append("The quick brown fox jumps over the lazy dog.\n")

        # For each random item in randos, add it to the linked list and test
        # Initialize expected variables
        ExpectedLength = 0
        ExpectedHead = randos[0]
        for rando in randos:
            LL2.add_last(rando) # Append to linked list
            # Dynamically update expected variables 
            ExpectedLength += 1
            ExpectedTail = rando
            # Test len(), get_head() and get_tail()
            self.assertEqual(len(LL2), ExpectedLength)
            self.assertEqual(LL2.get_head(), ExpectedHead)
            self.assertEqual(LL2.get_tail(), ExpectedTail)

    def testLinkedListNonEmptyInitialization(self):
        # Initialize linked list with random chars
        items = [chr(i) for i in range(48, 123)]
        LL3 = linkedlist.LinkedList(items)

        # Test len(), get_head(), and get_tail()
        self.assertEqual(len(LL3), 75)
        self.assertEqual(LL3.get_head(), '0')
        self.assertEqual(LL3.get_tail(), 'z')

    def testLinkedListAddFirst(self):
        # Initialize blank linked list
        LL4 = linkedlist.LinkedList()

        # Generate a string and 2 random numbers
        randos = ["The quick brown fox jumps over the lazy dog.\n"]
        randos.append(random.randint(-100000, 100000) for i in range(2))

        # For each random item in randos, add it to the linked list and test
        # Initialize expected variables
        ExpectedLength = 0
        ExpectedTail = randos[0]
        for rando in randos:
            LL4.add_first(rando) # Insert in linked list
            # Dynamically update expected variables 
            ExpectedLength += 1
            ExpectedHead = rando
            # Test len(), get_head() and get_tail()
            self.assertEqual(len(LL4), ExpectedLength)
            self.assertEqual(LL4.get_head(), ExpectedHead)
            self.assertEqual(LL4.get_tail(), ExpectedTail)

    def testLinkedListRemoveFirst(self):
        # Initialize linked list with random numbers - I think we've tested strings enough
        items = [i for i in range(-40, 80)]
        LL5 = linkedlist.LinkedList(items)

        # For each random item in randos, add it to the linked list and test
        # Initialize expected variables
        ExpectedLength = 120
        ExpectedTail = 79
        for item in items:
            ExpectedHead = item
            # Test len(), get_head() and get_tail()
            self.assertEqual(len(LL5), ExpectedLength)
            self.assertEqual(LL5.get_head(), ExpectedHead)
            self.assertEqual(LL5.get_tail(), ExpectedTail)
            # Remove from linked list and repeat
            LL5.remove_first() 
            # Dynamically update expected variables 
            ExpectedLength -= 1
            

    def testLinkedListRemoveLast(self):
        # Generate 30 random booleans
        randos = [bool(random.randint(0, 1)) for i in range(30)]
        # Initialize linked list with randos
        LL6 = linkedlist.LinkedList(randos)

        # For each random item in randos, add it to the linked list and test
        # Initialize expected variables
        ExpectedLength = 30
        ExpectedHead = randos[0]
        for rando in randos[-2::-1]:
            LL6.remove_last() # Remove from linked list
            # Dynamically update expected variables 
            ExpectedLength -= 1
            ExpectedTail = rando
            # Test len(), get_head() and get_tail()
            self.assertEqual(len(LL6), ExpectedLength)
            self.assertEqual(LL6.get_head(), ExpectedHead)
            self.assertEqual(LL6.get_tail(), ExpectedTail)

        LL6.remove_last()
        self.assertEqual(len(LL6), 0)
        self.assertEqual(LL6.get_head(), None)
        self.assertEqual(LL6.get_tail(), None)
            


if __name__ == "__main__":
    unittest.main()