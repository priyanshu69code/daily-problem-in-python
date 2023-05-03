class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTilt(root: TreeNode) -> int:
    tilt = [0]

    def getSum(node):
        if not node:
            return 0
        leftSum = getSum(node.left)
        rightSum = getSum(node.right)
        tilt[0] += abs(leftSum - rightSum)
        return node.val + leftSum + rightSum

    getSum(root)
    return tilt[0]