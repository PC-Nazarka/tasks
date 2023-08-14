class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(first, second):
    last = second.next
    prev, curr = first, second
    while curr != last:
        next_item = prev.next
        prev.next = curr
        curr = prev 
        prev = next_item
    return prev

    
def reverse_list(root):
    first, second = None, None
    prev = None
    while root:
        if root.value % 2 and first:
            root = reverse(first, second)
            first, second = None, None
        if not root.value % 2:
            if first is None:
                first = prev
                second = root
            else:
                second = root
        prev = root
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

while head:
    print(head.value)
    head = head.next

head = root

reverse_list(head)
print()
while root:
    print(root.value)
    root = root.next
