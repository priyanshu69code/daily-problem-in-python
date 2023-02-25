def hasPathSum(root, targetSum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == targetSum
    left_sum = hasPathSum(root.left, targetSum - root.val)
    right_sum = hasPathSum(root.right, targetSum - root.val)
    return left_sum or right_sum