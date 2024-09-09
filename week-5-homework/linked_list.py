
class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link

    # Recursive Example:
    # recursively call on self.link until tail node
    def __len__(self):
        """Recursively calculates how many items are in LL starting at this node"""
        # base case: tail node, len = 1
        if self.link is None:
            return 1
        # recursive case: len = 1 + len(link)
        return 1 + len(self.link)

    # Recursive example:
    # has helper function to create mutable collection
    # to store state at all levels of recursion
    def __repr__(self):
        """Recursively prints all nodes"""
        return ' -> '.join(self._repr([]))

    def _repr(self, item_list):
        """
        Helper function for __repr__.
        Allows item_list to be initialized as an empty mutable.
        """
        item_list.append(f"Node({self.data})")
        # If this node is not the tail, keep adding nodes
        if self.link is not None:
            self.link._repr(item_list)
        return item_list

    # Recursive example:
    # get the last item, then pass it back through all level of recursion
    def get_tail(self):
        """Recursively gets the item stored in the tail node"""
        if self.link is None:
            return self.data
        else:
            return self.link.get_tail()

    # TODO: Implement the methods below.
    # Use recursion.
    # Non-recursive solutions will not receive credit.

    def add_last(self, item):
        """Adds an item "item" to the end of a linked list head."""
        if self.link == None:
            self.link = LLNode(item)
        else:
            next_node = self.link
            next_node.add_last(item)

    def sum_all(self):
        """Calculates the sum of all items in a linked list head's links, assuming all nodes carry ints or floats only."""
        next_node = self.link
        if self.link != None:
            return self.data + next_node.sum_all()
        else:
            return self.data

    def contains(self, item):
        """Checks if a linked list head contains, in any of its links, an item "item"."""
        if self.data == item:
            return True
        elif self.link == None:
            return False
        else:
            next_node = self.link
            return next_node.contains(item)

    def remove_all(self, item):
        """Removes all instances of "item" in a linked list head's links."""
        # Base cases:
        # Does it point to None?
        if self.link is None:
            return self
        # Is it itself still a match? (Needed for first node matches)
        if self.data == item:
            return (self.link).remove_all(item)
        # Does it need to skip a node? (i.e. is the next node a match)
        if self.link.data == item:
            # If so, does that point to None?
            if self.link.link is None:
                # Skip next node
                self.link = None
                return self
            else:
                # Skip next node
                self.link = (self.link.link).remove_all(item)
                return self
        else: 
            # double it and give it to the next node
            self.link = (self.link).remove_all(item)
            return self

    def reverse(self):
        """Reverses the sequence of links in the head node of a linked list."""
        def _reverse_node(curr, prev):
            if not curr:
                return prev
            next = curr.link
            curr.link = prev
            prev = curr
            curr = next
            return _reverse_node(curr, prev)
 
        # update the head of the original linked list 
        return _reverse_node(curr=self, prev=None)



# Do not make any changes to LinkedList:
# all your code should be above in the LLNode class
class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering

    def add_first(self, item):
        """Adds to beginning of Linked List"""
        self._head = LLNode(item, self._head)

    def remove_first(self):
        """Removes and returns first item"""
        # Edge case
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty list.')
        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item

    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)

    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0

    def __contains__(self, item):
        """Returns True if item is in Linked List. Returns False otherwise."""
        if self._head is None:
            return False
        return self._head.contains(item)

    def add_last(self, item):
        """Adds item to end of Linked List"""
        if self._head is None:
            return self.add_first(item)
        self._head.add_last(item)

    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0

    def remove_all(self, item):
        """Removes all occurrences of item from Linked List"""
        if self._head is not None:
            self._head = self._head.remove_all(item)

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        if self._head is not None:
            self._head = self._head.reverse()

    def get_tail(self):
        """Returns the item stored in tail"""
        return self._head.get_tail() if self._head else None
