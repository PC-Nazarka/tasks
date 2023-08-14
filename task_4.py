class Node:
    def __init__(self, value):
        self.key = value
        self.left = self.right = None

result = []
root = Node(8)
root.left = Node(5)
root.left.right = Node(6)
root.left.left = Node(3)
root.right = Node(10)
root.right.left = Node(9)
root.right.right = Node(11)

def dfs(node: Node):
    if not node:
        return None
    left = dfs(node.left)
    if left:
        result.append(left)
    result.append(node.key)
    right = dfs(node.right)
    if right:
        result.append(right)

dfs(root)
print(result)
