class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def height(node: TreeNode) -> int:
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        return 1 + max(left_height, right_height)
    
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False
