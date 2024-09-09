class Node:
    """Node(item, link)
    A class for a single node as part of a linked list.
    Has two inputs;
    - 'item' - what data the node contains (mandatory)
    - 'link' - what the node points to (optional, defaults to None)
    Has two attributes;
    - 'item' - what data the node contains
    - 'link' - what the node points to
    Can be called as a string, which will return "Node(item)". """
    def __init__(self, item, link=None):
        "Initializes a new Node."
        self.item = item
        self.link = link

    def __repr__(self):
        "Prints a node as Node(item)."
        return f"Node({self.item})"
    


class LinkedList:
    """LinkedList(items)
    A class for a linked list which contains any number of linked nodes.
    Has one input;
    - 'items' - what data points the linked list will contain in any iterable variable (optional)
    Has no public attributes.
    Has six public methods;
    - 'get_head()' - returns first node's item (or None if linked list empty)
    - 'get_tail()' - returns last node's item (or None if linked list empty)
    - 'add_first(item)' - add item to the beginning of the linked list
    - 'add_last(item)' - add item to the end of the linked list
    - 'remove_first()' - remove the first item in the linked list and return it (or raises RuntimeError if linked list is empty)
    - 'remove_last()' - remove the last item in the linked list and return it (or raises RuntimeError if linked list is empty)
    Compatible with len()."""
    def __len__(self):
        "returns length of linked list (duh)"
        return self._len

    def add_last(self, item):
        "'add_last(item)' - add item to the end of the linked list"
        new_node = Node(item, None) # To be injected 
        if self._tail is None: # List empty
            self._head = new_node
            self._tail = new_node
        else: # List populated
            self._tail.link = new_node # Attach new node to list
            self._tail = new_node # Make readily available via _tail
        self._len += 1

    def add_first(self, item):
        "'add_first(item)' - add item to the beginning of the linked list"
        new_node = Node(item, None) # To be injected 
        if self._head is None: # List empty
            self._head = new_node
            self._tail = new_node
        else:
            new_node.link = self._head # Attach new node to list
            self._head = new_node # Make readily available via _head
        self._len += 1
    
    def get_head(self):
        "'get_head()' - returns first node's item (or None if linked list empty)"
        if self._head is None:
            return None
        else:
            return self._head.item
    
    def get_tail(self):
        "'get_tail()' - returns last node's item (or None if linked list empty)"
        if self._tail is None:
            return None
        else:
            return self._tail.item
    
    def remove_first(self):
        "'remove_first()' - remove the first item in the linked list and return it (or raises RuntimeError if linked list is empty)"
        if self._len == 0:
            raise RuntimeError
        elif self._len == 1: # List becomes empty when only item removed
            former_head_item = self._head.item
            self._head = None
            self._tail = None
        else:
            # Literally just make the node the first node links to (the second node) become the head node and the others will follow
            former_head_item = self._head.item
            self._head = self._head.link
        self._len -= 1
        return former_head_item

    def remove_last(self):
        "'remove_last()' - remove the last item in the linked list and return it (or raises RuntimeError if linked list is empty)"
        if self._len == 0:
            raise RuntimeError
        elif self._len == 1: # List becomes empty when only item removed
            former_tail_item = self._tail.item
            self._head = None
            self._tail = None
        else:
            former_tail_item = self._tail.item
            # Find the second to last node
            current_node = self._head
            for i in range(self._len - 2):
                current_node = current_node.link
            # Change this node's link to None
            current_node.link = None
            # Make this link the new tail
            self._tail = current_node
        self._len -= 1
        return former_tail_item

    def __init__(self, items=None):
        "Initializes a new Linked List."
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)