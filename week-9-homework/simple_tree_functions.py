class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"

############################################
### Please do not alter the above class. ###
############################################

def height(t):
    """Recursively determine the height of a tree rooted at a TreeNode object {t}."""
    # Base cases - get heights of children otherwise
    left_height = 0 if t.left is None else height(t.left) + 1
    right_height = 0 if t.right is None else height(t.right) + 1
    
    # Determine height of current node
    return max(left_height, right_height)

def size(t):
    """Recursively determine the size of a tree rooted at a TreeNode object {t}."""
    # Base cases - get heights of children otherwise
    left_size = 0 if t.left is None else size(t.left)
    right_size = 0 if t.right is None else size(t.right)
    
    # Determine height of current node
    return left_size + right_size + 1

def find_min(t):
    """Recursively determine the minimum value of a tree rooted at a TreeNode object {t}."""
    qualifiers = [t.data]
    
    # Left child present
    if t.left is not None:
        qualifiers.append(find_min(t.left))

    # Right child present
    if t.right is not None:
        qualifiers.append(find_min(t.right))

    return min(qualifiers)

def find_max(t):
    """Recursively determine the maximum value of a tree rooted at a TreeNode object {t}."""
    qualifiers = [t.data]
    
    # Left child present
    if t.left is not None:
        qualifiers.append(find_max(t.left))

    # Right child present
    if t.right is not None:
        qualifiers.append(find_max(t.right))

    return max(qualifiers)

def contains(t, k):
    """Recursively determine if a tree rooted at a TreeNode object {t} contains an object {k}."""
    qualifiers = [t.data == k]
    
    # Left child present
    if t.left is not None:
        qualifiers.append(contains(t.left, k))

    # Right child present
    if t.right is not None:
        qualifiers.append(contains(t.right, k))

    return any(qualifiers)

def in_order(t):
    """Recursively list the contents of a TreeNode object {t} using an in-order traversal."""
    qualifiers = []
    
    # Left child present
    if t.left is not None:
        qualifiers += in_order(t.left)
    
    qualifiers.append(t.data)

    # Right child present
    if t.right is not None:
        qualifiers += in_order(t.right)

    return qualifiers

def pre_order(t):
    """Recursively list the contents of a TreeNode object {t} using a pre-order traversal."""
    qualifiers = [t.data]

    # Left child present
    if t.left is not None:
        qualifiers += pre_order(t.left)

    # Right child present
    if t.right is not None:
        qualifiers += pre_order(t.right)

    return qualifiers

def post_order(t):
    """Recursively list the contents of a TreeNode object {t} using a post-order traversal."""
    qualifiers = []
    
    # Left child present
    if t.left is not None:
        qualifiers += post_order(t.left)

    # Right child present
    if t.right is not None:
        qualifiers += post_order(t.right)
    
    qualifiers.append(t.data)
    return qualifiers
