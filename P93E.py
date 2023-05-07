class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res