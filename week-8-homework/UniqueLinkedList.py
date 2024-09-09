class UniqueRecursiveNode:
    def __init__(self, key, value, link=None):
        """Creates a new node with key:value pair"""
        self.key = key
        self.value = value
        self.link = link

    def __iter__(self):
        """Iterates over the linked list"""
        yield self.key, self.value                      # yield values from this node
        if self.link is not None: yield from self.link  # continue to yield from link

    def __eq__(self, other):
        """Tests equality for two nodes; if they have the same {key}, they're equal"""
        return self.key == other.key
    
    def __hash__(self):
        """Hashes a node by simply hashing its {key}."""
        return hash(self.key)
    
    def add(self, key, value):
        """Either updates the value of a matching-{key} node, or, if one is not found, adds a new {key}:{value} node.
        Returns the number of nodes added to the linked list which it is part of (always 0 or 1).
        O(n) worst-case time complexity."""
        if self.key == key:
            # Update node and return 0
            self.value = value
            return 0
        elif self.link is None:
            # Add new node and return 1
            self.link = UniqueRecursiveNode(key, value)
            return 1
        else:
            # Check next item
            return (self.link).add(key, value)

    def get(self, key):
        """Returns the value of a key in the linked list which this node is part of.
        Will raise a KeyError if such a node is not found.
        Returns the value associated with this new key.
        O(n) worst-case time complexity."""
        if self.key == key:
            # Return value
            return self.value
        elif self.link is None:
            # Raise KeyError
            raise KeyError(f"Key {key} not found in UniqueRecursiveNode object")
        else:
            # Check next item
            return (self.link).get(key)

    def _remove(self, key):
        """Helper function for remove()."""
        # Recursion, yay!
        # Find next usable node
        if self.link is None:
            link_to, popped_value = None, None
        else:
            link_to, popped_value = (self.link)._remove(key)

        # Update link
        self.link = link_to
        
        # Return either current node or next node (if current node matches),
        # ...along with the popped value
        if self.key == key:
            return (link_to, self.value)
        
        else:
            return (self, popped_value)
    
    def remove(self, key):
        """Removes a node from the linked list which this node is part of.
        Will raise a KeyError if such a node is not found.
        Returns a tuple containing:
            - the node which the preceding link should link to after this operation
            - the value associated with this key
        O(n) worst-case time complexity."""
        # Launch helper fn
        link_to, popped_value = self._remove(key)

        # Check if popped
        if popped_value is None:
            raise KeyError(f"Key {key} not found in UniqueRecursiveNode object")
        
        return link_to, popped_value
        
    def __contains__(self, key):
        """Membership testing for the UniqueRecursiveNode class.
        Returns a boolean that is True if {key} is found and False otherwise..
        O(n) worst-case time complexity."""
        if self.key == key:
            # Found
            return True
        elif self.link is None:
            # Not found
            return False
        else:
            # Check next item
            return key in self.link


##########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE #
##########################################
class UniqueLinkedList:
    def __init__(self, items=None):
        """Creates a new linked list with optional collection of items"""
        self._head = None
        self._len = 0

        # Sequentially add items if they were included
        if items is not None:
            for key, value in items:
                self.add(key, value)

    def __len__(self):
        """Returns number of nodes in ULL"""
        return self._len
    
    def get_head(self):
        """Returns key, value in head"""
        return (self._head.key, self._head.value) if self._head is not None else None
    
    def get_tail(self):
        """Returns key, value in tail"""
        # Edge case - empty ULL
        if len(self) == 0: return None

        # Find tail node
        tail = self._head
        while tail.link is not None:
            tail = tail.link
        
        # Return key, value pair
        return (tail.key, tail.value)
    
    def add(self, key, value):
        """Adds node with key:value pair, or updates value, as appropriate"""
        # Edge case - empty linked list
        if len(self) == 0:
            self._head = UniqueRecursiveNode(key, value)
            n_added = 1
        
        else:
            # Note how we use the return value from UniqueRecursiveNode.add()
            n_added = self._head.add(key, value)
        
        self._len += n_added
        return n_added

    def get(self, key):
        """Returns value associated with key"""
        if len(self) == 0: raise KeyError(f"key {key} not in ULL")
        return self._head.get(key)

    def remove(self, key):
        """Removes node with key and returns value"""
        if len(self) == 0: raise KeyError(f"key {key} not found")

        new_head, value = self._head.remove(key)
        self._head = new_head
        self._len -= 1
        return value

    def __contains__(self, key):
        """Returns True iff key in ULL"""
        return self._head is not None and key in self._head
    
    def __iter__(self):
        """Returns iterable over key:value pairs in ULL"""
        if self._head is not None: yield from self._head
