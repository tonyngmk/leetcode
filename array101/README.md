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
- Edge case: If the shifted array last element is 0, do not count that as `possible_dup`.
- Difficulty: 4/10

### 5. Merge Sorted Array
- File: `merge_sorted_array.py`
- Link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
- Description: Two arrays sorted in ascending, modify first array in place by combining second array into first.
- Pattern: 2 pointers to point to the tail of 2 array, 1 pointer for writing.
- Edge case: Since we are slotting 2nd array to 1st, if all of 1st array has been used while 2nd array is not, we would have to dump array 2 into array 1 (starting from the back).
- Time: O(N)
- Space: O(1) 
- Difficulty: 5/10 