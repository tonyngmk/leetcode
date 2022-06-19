### Singly-linked list (SLL)

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index+1): curr = curr.next
        return curr.val
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0: return # Do nothing if index is invalid
        
        # change size
        self.size += 1

        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # Node to add
        to_add = Node(val)
        to_add.next = pred.next
        pred.next = to_add

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size: return # Do nothing if index is invalid
        self.size -=1 # change size
            
        pred = self.head
        for _ in range(index): pred = pred.next
        pred.next = pred.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ### Doubly linked-list (DLL)
# class Node():
#     def __init__(self, x):
#         self.val = x
#         self.prev, self.next = None, None

# class MyLinkedList:
#     def __init__(self):
#         self.size = 0
#         # sentinel nodes as pseudo-head and pseudo-tail
#         self.head, self.tail = ListNode(0), ListNode(0) 
#         self.head.next = self.tail
#         self.tail.prev = self.head
        

#     def get(self, index):
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         # if index is invalid
#         if index < 0 or index >= self.size:
#             return -1
        
#         # choose the fastest way: to move from the head
#         # or to move from the tail
#         if index + 1 < self.size - index:
#             curr = self.head
#             for _ in range(index + 1):
#                 curr = curr.next
#         else:
#             curr = self.tail
#             for _ in range(self.size - index):
#                 curr = curr.prev
                
#         return curr.val
            

#     def addAtHead(self, val):
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         pred, succ = self.head, self.head.next
        
#         self.size += 1
#         to_add = ListNode(val)
#         to_add.prev = pred
#         to_add.next = succ
#         pred.next = to_add
#         succ.prev = to_add
        

#     def addAtTail(self, val):
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         succ, pred = self.tail, self.tail.prev
        
#         self.size += 1
#         to_add = ListNode(val)
#         to_add.prev = pred
#         to_add.next = succ
#         pred.next = to_add
#         succ.prev = to_add
        

#     def addAtIndex(self, index, val):
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         # If index is greater than the length, 
#         # the node will not be inserted.
#         if index > self.size:
#             return
        
#         # [so weird] If index is negative, 
#         # the node will be inserted at the head of the list.
#         if index < 0:
#             index = 0
        
#         # find predecessor and successor of the node to be added
#         if index < self.size - index:
#             pred = self.head
#             for _ in range(index):
#                 pred = pred.next
#             succ = pred.next
#         else:
#             succ = self.tail
#             for _ in range(self.size - index):
#                 succ = succ.prev
#             pred = succ.prev
        
#         # insertion itself
#         self.size += 1
#         to_add = ListNode(val)
#         to_add.prev = pred
#         to_add.next = succ
#         pred.next = to_add
#         succ.prev = to_add
        

#     def deleteAtIndex(self, index):
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         # if the index is invalid, do nothing
#         if index < 0 or index >= self.size:
#             return
        
#         # find predecessor and successor of the node to be deleted
#         if index < self.size - index:
#             pred = self.head
#             for _ in range(index):
#                 pred = pred.next
#             succ = pred.next.next
#         else:
#             succ = self.tail
#             for _ in range(self.size - index - 1):
#                 succ = succ.prev
#             pred = succ.prev.prev
            
#         # delete pred.next 
#         self.size -= 1
#         pred.next = succ
#         succ.prev = pred