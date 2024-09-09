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

def count_failures(pred, t):
    """Given a predicate function/lambda {pred}, count the number of times
    the objects in a TreeNode object {t} fail this predicate."""
    tally = 0 if pred(t.data) else 1

    # Left hand
    if t.left is not None: tally += count_failures(pred, t.left)

    # Right hand
    if t.right is not None: tally += count_failures(pred, t.right)

    return tally

def tree_map(f, t):
    """Given a function/lambda {f}, returns a new tree with all objects
    in a TreeNode object {t} having had it applied to them."""
    # Left hand
    LeftTree = tree_map(f, t.left) if t.left is not None else None

    # Right hand
    RightTree = tree_map(f, t.right) if t.right is not None else None

    # Tree itself
    return TreeNode(f(t.data), left=LeftTree, right=RightTree)

def tree_apply(f, t):
    """Given a function/lambda {f}, recursively applies it to all items in a TreeNode object {t}."""
    # Left hand
    if t.left is not None:
        tree_apply(f, t.left)

    # Right hand
    if t.right is not None:
        tree_apply(f, t.right)

    # Tree itself
    t.data = f(t.data)
