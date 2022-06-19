class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None


# Initialise ll
ll = LinkedList()

# Create nodes, reference ll.head with Node(1)
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.next = third

