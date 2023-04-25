class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def traverse(node):
            nonlocal max_count, curr_count, curr_val, modes
            if node is None:
                return
            traverse(node.left)
            if node.val == curr_val:
                curr_count += 1
            else:
                curr_val = node.val
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
                modes = [curr_val]
            elif curr_count == max_count:
                modes.append(curr_val)
            traverse(node.right)
        
        max_count = 0
        curr_count = 0
        curr_val = None
        modes = []
        traverse(root)
        return modes