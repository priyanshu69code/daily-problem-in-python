def binary_tree_paths(root):
    if not root:
        return []
    paths = []
    dfs(root, "", paths)
    return paths

def dfs(node, path, paths):
    if not node.left and not node.right:
        paths.append(path + str(node.val))
    if node.left:
        dfs(node.left, path + str(node.val) + "->", paths)
    if node.right:
        dfs(node.right, path + str(node.val) + "->", paths)