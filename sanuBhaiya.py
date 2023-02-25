class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("None")
    return " ".join(result)

def deserialize(data):
    data = data.split()
    root = TreeNode(int(data[0]))
    queue = [root]
    index = 1
    while queue:
        node = queue.pop(0)
        if node:
            if data[index] != "None":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1
            if data[index] != "None":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1
    return root