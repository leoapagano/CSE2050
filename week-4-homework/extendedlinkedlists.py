from linkedlist import Node, LinkedList # get linkedlist.py from lab
 
# Create the classes for this assignment below.
class ReversableLinkedList(LinkedList):
    def reverse(self):
        """Reverses the node order in a linked list of type ReversableLinkedList.
        Returns nothing."""
        for i in range(len(self) - 1):
            # Remap last item in head to second to last item (or None, if it doesn't exist)
            # Find second to last node in linked list
            current_node = self._head
            for i in range(self._len - 2 - i):
                current_node = current_node.link
            # Change linked node's link to this node
            current_node.link.link = current_node
        
        # Play musical chairs with head and tail variables
        newhead = self._tail
        newtail = self._head
        self._tail = newtail
        self._head = newhead



class SortedLinkedList(LinkedList):
    # Non implemented methods
    def add_first(self, item):
        "Please use add_sorted(item) instead."
        raise NotImplementedError(f"Use add_sorted({item}) instead")
    def add_last(self, item):
        "Please use add_sorted(item) instead."
        raise NotImplementedError(f"Use add_sorted({item}) instead")

    def add_sorted(self, item):
        """Adds a new node with value 'item' in such a spot which would keep the list of node values in ascending order, within a linked list of type SortedLinkedList.
        Returns nothing."""
        new_node = Node(item, None)
        
        # First check (CURRENT NODE IS *AFTER* THE SELECTOR) - requires len>=1
        if self._len >= 1:
            current_node = self._head
            if item <= current_node.item:
                new_node.link = current_node
                self._head = new_node
                self._len += 1
                return

        # Middle checks (CURRENT NODE IS *BEFORE* THE SELECTOR) - requires len>=2
        if self._len >= 2:
            for i in range(len(self) - 1):
                if item <= current_node.link.item:
                    # Proceed with insertion
                    new_node.link = current_node.link
                    current_node.link = new_node
                    self._len += 1
                    return
                else:
                    # Proceed to next middle check(s)
                    current_node = current_node.link

        # Add to end (last check) - can be done at any len
        if self._len >= 1:
            self._tail.link = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._len += 1
        return
    
    def __init__(self, items=None): # Note that if we're blocking add_first() and add_last(), we must also change init
        "Initializes a new Sorted Linked List."
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_sorted(item)



class UniqueLinkedList(LinkedList):
    def remove_dups(self):
        """Removes duplicate entries from a linked list of type UniqueLinkedList.
        Returns a dictionary of pairs entry:count."""
        counts = {}
        current_node = self._head
        counts[current_node.item] = 0
        
        # Iterate through nodes
        for i in range(len(self)):
            # Check if the *next* node's item is a duplicate/not real
            if current_node.link is None:
                break
            elif current_node.link.item not in counts:
                counts[current_node.link.item] = 0
                current_node = current_node.link # Neeeext!
            else:
                counts[current_node.link.item] += 1
                # Delete that node
                if current_node.link.link == None:
                    self._tail = current_node # Update tail dynamically
                current_node.link = current_node.link.link
                self._len -= 1

        return counts