class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: TreeNode):
    if not root:
        return []
    result = [root.val]
    result += preorderTraversal(root.left)
    result += preorderTraversal(root.right)
    return result




