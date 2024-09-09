class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link
 
    #######################################################
    # All methods below should be implemented recursively #
    #######################################################
 
    def __len__(self):
        """Recursively returns the number of nodes including and after this node"""
        # Base case
        if self.link is None:
            return 1
        else:
            # Recursion
            return len(self.link) + 1
 
    def __repr__(self):
        """Recursively prints out the nodes including and after this node"""
        # Base case
        if self.link is None:
            return f"Node({self.data})"
        else:
            # Recursion
            return f"Node({self.data}) -> {repr(self.link)}"
 
    def get_tail(self):
        """Finds the tail node's data and returns it, finding it with recursion"""
        if self.link is None:
            return self.data
        else:
            return (self.link).get_tail()

    def add_last(self, item):
        """Appends an item to the tail node, finding it with recursion"""
        if self.link is None:
            self.link = LLNode(item)
        else:
            (self.link).add_last(item)
 
    # sum_all should return the sum of all items in the linked list
    def sum_all(self):
        """Sums up all items including and after this node with recursion"""
        if self.link is None:
            return self.data
        else:
            return self.data + (self.link).sum_all()
 
    def contains(self, item):
        """Recursively looks for an item in this linked list chain (including or after this node) with data (item)"""
        if self.data == item:
            return True
        elif self.link is None:
            return False
        else:
            return (self.link).contains(item)
 
    # remove_all should remove all nodes that contain a given item
    def remove_all(self, item):
        """Removes all nodes including/after this node with data (item) with recursion"""
        if self.link is not None:
            self.link = (self.link).remove_all(item)
        if self.data == item:
            return self.link
        else:
            return self
 
    def reverse(self):
        """Reverses the current linked list with recursion. Returns the new head."""
        # Recursion - do this first
        if self.link is not None:
            x = self.link.reverse()
            # Only when not dealing with the last item in the list do you do add_last and removal

            # Add to end
            x.add_last(self.data)

            # Pass it on to the next recursion back up
            return x
        else:
            return self


 
#########################################################
# No changes below this point - all your work should be #
# in LLNode.                                            #
#########################################################
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
