# Array101
> Part of W1 (2022-05-30 - 2022-06-05)

### 1. Intro - Max Consecutive Ones 
- File: `max_consecutive_ones.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
- Description: Find longest consecutive element in array
- Pattern: Convert to string, split by undesired element, map to get list of length, find max of length in array
- Difficulty: 1/10

### 2. Find Numbers with Even Number of Digits
- File: `find_numbers_with_even_digits.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
- Description: Find how many numbers in array has even length (or digits)
- Pattern: Convert int to str, if length of string is even, reflect as 1 in tuple. Finally, sum the tuple.
- Difficulty: 1/10

### 3. Squares of a Sorted Array
- File: `squares_of_sorted_array.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
- Description: Given ascending array with negative, return sorted array with elements squared
- Pattern: Use double pointer (left and right), square only the abs(left / right) of which is greater, place this in the last element of array (or otherwise flip it later)
- Difficulty: 2/10

### 4. Duplicate Zeros
- File: `duplicate_zeros.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
- Description: Duplicate zeros in array, shifting non-zero elements to the right.
- Pattern: To use break to maintain array length. To have 2 pointers for writing and referencing value.
- Edge case: If the shifted array last element is 0, do not count that as `possible_dup`, go directly to array and hard code 0 and shift to previous index.
- Time: O(2n)
- Space: O(1)
- Difficulty: 3/10

### 5. Merge Sorted Array
- File: `merge_sorted_array.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
- Description: Two arrays sorted in ascending, modify first array in place by combining second array into first.
- Pattern: 2 pointers to point to the tail of 2 array, 1 pointer for writing.
- Edge case: Since we are slotting 2nd array to 1st, if all of 1st array has been used while 2nd array is not, we would have to dump array 2 into array 1 (starting from the back).
- Time: O(n)
- Space: O(1) 
- Difficulty: 3/10

### 6. Remove elements
- File: `remove_elements.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
- Description: Remove element in array, pushing forward all unremoved elements to the start of array.
- Pattern: 2 pointers, 1 reader going through the array, 1 writer to write only if element is not val. To call .pop() array the amount of times val has occurred thereafter.
- Edge case: NIL
- Time: O(2n)
- Space: O(1) 
- Difficulty: 2/10

### 7. Remove duplicates from Sorted Array
- File: `remove_duplicates_from_sorted_array.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
- Description: To remove duplicates of a sorted array, pushing forward unremoved elements to the start of array.
- Pattern: 2 pointers, 1 reader going through the array, 1 writer to write only if element is not equal to nums[j-1]. Final writer index would also be the total amount of distinct elements. 
- Edge case: NIL
- Time: O(n)
- Space: O(1)
- Difficulty: 2/10

### 8. Check if N and its double exists
- File: `check_if_n_and_its_double_exists.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
- Description: Check if both N and 2N exists in an array. 
- Pattern: Loop through array. Create a new hash map to store elements that you have "seen". If current iteration's value divided by 2 or multiplication of 2 value exists in "seen" map, returns True. Else, store current iteration value into hash map.
- Edge case: NIL
- Time: O(n), 1 pass
- Space: O(n), new hash map
- Difficulty: 1/10

### 9. Valid Mountain Array
- File: `valid_mountain_array.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
- Description: A valid mountain array is one where array starts from 0, continues to a peak without duplicates, and goes down to 0 without duplicates.
- Pattern: Create 2 pointers. Left and right pointers can only move towards their opposite directions if the next element is greater than their current position. Both will end at the same peak (index) if array is a valid mountain.
- Edge case: NIL
- Time: O(n)
- Space: O(1)
- Difficulty: 2/10


---
### Template
- File: `.py`
- Link: 
- Description: 
- Pattern: 
- Edge case: 
- Time: 
- Space: 
- Difficulty: /10
