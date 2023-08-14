from collections import deque

class Node:
    def __init__(self, value):
        self.key = value
        self.left = self.right = None


root = Node(8)
root.left = Node(5)
root.left.right = Node(6)
root.left.left = Node(3)
root.right = Node(10)
root.right.left = Node(9)
root.right.right = Node(11)

q = deque([])
visited = set()

q.append(root)

while q:
    len_q = len(q)

    for _ in range(len_q):
        node = q.popleft()
        print(node.key)
        visited.add(node.key)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
    