class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def reverse_list(root):
    first, second = None, None
    while root:
        if not root.key % 2:
            if first is not None:
                second = root
            else:
                first = root
        root = root.next


root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(4)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)
root.next.next.next.next.next.next.next.next = Node(9)

head = root
reverse_list(head)
