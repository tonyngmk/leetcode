from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 1
        
        while head:
            head = head.next
            self.n += 1
            
    def getRandom(self) -> int:
        
        curr = self.head
        for _ in range(1, random.randint(1, self.n-1)):
            curr = curr.next
            
        return curr.val

# example1 = [1,2,3]
# sentinel = ListNode(None)
# head = sentinel
# for i in range(len(example1)):
#     head.next = ListNode(example1[i])
#     head = head.next
# head = sentinel.next

# print(Solution(example1).getRandom())


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()