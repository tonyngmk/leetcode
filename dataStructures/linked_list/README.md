# Linked List
> Part of W3 (2022-06-13 - 2022-06-19)
- Link: https://leetcode.com/explore/learn/card/linked-list/

### 1. Intro - Design Linked List
- File: `design_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
- Description: Implement class and methods for linked list.
- Pattern: NIL
- Difficulty: 5/10. Not easy to code from understanding, to revisit this.

### 2. Linked list cycle I 
- File: `linked_list_cycle.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
- Description: Use Floyd's Tortoise and Hare algorithm to determine if linked list is a cycle when both slow and fast pointer intersect.
- Pattern: Implement Floyd's Tortoise and Hare algorithm
- Difficulty: 3/10. 
- Time: O(n)
- Space: O(1)

### 3. Linked list cycle II 
- File: `linked_list_cycle_2.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
- Description: Use Floyd's Tortoise and Hare algorithm to determine if linked list is a cycle. If so, create 2 more pointers at head and intersection and traverse till both meets, that is guaranteed to be the entrance.
- Pattern: Implement Floyd's Tortoise and Hare algorithm
- Difficulty: 4/10, to revisit without help again. 
- Time: O(n)
- Space: O(1)


### 4. Intersection of Two Linked List
- File: `intersection_of_linked_list.py`
- Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
- Pattern: Using 2 pointers which is guaranteed to intersect if linked list intersects.
- Time: O(n+m), where n and m is the size of linked list for each linked list
- Space: O(1), no extra space created
- Difficulty: 4/10

### 5. Reverse Linked List 
- File: `reverse_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
- Description: Reversing linked list iteratively
- Pattern: Create 3 pointers: previous, current and next.
- Time: O(n)
- Space: O(1)
- Difficulty: 2/10

### 6. Reverse linked list
- File: `reverse_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
- Description: Return a linked list with its pointers reversed
- Pattern: Use the 3 pointer technique (prev, curr, next) to change the direction of the pointers.
- Time: O(n)
- Space: O(1)
- Difficulty: 1/10

### 7. Remove linked list elements
- File: `remove_linked_list_elements.py`
- Link: https://leetcode.com/problems/remove-linked-list-elements/
- Description: Remove linked list element if node has certain value.
- Pattern: Add Sentinel node to help return head value
- Difficulty: 1/10, but revisit without help again.
- Time: O(n)
- Space: O(1)

### 8. Odd even linked list
- File: `odd_even_linked_list.py`
- Link: https://leetcode.com/problems/odd-even-linked-list/
- Description: Group odd indices nodes, then even indices nodes, and return them in a linked-list inplace  
- Pattern: 
- Difficulty: 3/10, but revisit without help again.
- Time: O(n)
- Space: O(1)

### 9. Palindrome Linked List
- File: `palindrome_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
- Description: Find mid-way point, reverse linked list from mid-way point, compare linked-list from start and end of reversed ll.
- Pattern: Use slow-fast pointer, use reverse linked list, comparison of mid-way point
- Time: O(n)
- Space: O(1)
- Difficulty: 6/10, to redo without solution again

### 10. Merge Two Sorted Linked List
- File: `merge_two_sorted_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
- Description: Create new linked list and if pointer number of linked list is smaller
- Pattern: Create two pointers for each linked list and add to a new one, join longer end of remaining list if there is nothing else to compare to
- Time: O(n)
- Space: O(1)
- Difficulty: 3/10


### 11. Add two Numbers
- File: `add_two_numbers.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
- Description: Create new linked list and add values of both pointers in separate linked list  
- Pattern: To account for a carry number that brings value to next node of the linked list 
- Time: O(n)
- Space: O(n)
- Difficulty: 3/10

### 12. Flatten a multi-level doubly linked list
- File: `flatten_multi_level_doubly_linked_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
- Description: To do after trees 
- Pattern: To do after trees 
- Time: ?
- Space: ?
- Difficulty: Not done

### 13. Insert into a Cylic Sorted List
- File: `insert_into_cyclic_sorted_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1226/
- Description: To use two-pointer technique and account for all possible scenarios.
- Pattern: 
    - To iterate through 1 cycle of the linked list, looking for spots to insert where `insertVal` is between `prev.val` and `curr.val`.
    - Since `head` is not the lowest value, there may be chance where `insertVal` belongs to the "start" or "end" in terms of value wise of the LL, hence to account for this as well. - To account for empty linked list as well, which is to return linked list of 1 node by itself.
    - Even if linked list is not empty, if linked list is only of size 1, it should be just inserted as well.
- Time: O(n)
- Space: O(1)
- Difficulty: 6/10, need a lot of help and must be very sharp on all scenarios and edge cases

### 14. Copy list with a random pointer
- File: `.py`
- Link: 
- Description: Giddy after reading question, to attempt this at a later date.
- Pattern: 
- Time: 
- Space: 
- Difficulty: /10

### 15. Rotate List 
- File: `rotate_list.py`
- Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
- Description: To rotate list by using modulo operation, linking end of list to the start, and thereafter breaking link.
- Pattern: In general, require good visualisation and understanding of linked list traversal. The modulo operation as well!
- Time: O(n)
- Space: O(1)
- Difficulty: 4/10, to retry without help.

### Template
- File: `.py`
- Link: 
- Description: 
- Pattern: 
- Time: 
- Space: 
- Difficulty: /10

---
### Template
- File: `.py`
- Link: 
- Description: 
- Pattern: 
- Time: 
- Space: 
- Difficulty: /10
