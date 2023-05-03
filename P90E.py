class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.children:
        return 1
    max_child_depth = 0
    for child in root.children:
        child_depth = maxDepth(child)
        max_child_depth = max(max_child_depth, child_depth)
    return max_child_depth + 1