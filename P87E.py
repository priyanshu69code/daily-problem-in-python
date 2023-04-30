class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Node) -> int:
        self.ans = 0
        def depth(node):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left+right)
            return max(left, right) + 1
        depth(root)
        return self.ans