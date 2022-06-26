# Binary Search
> Part of learning algorithms after Array101

### 1. Intro - Max Consecutive Ones 
- File: `binary_search.py`
- Link: https://leetcode.com/problems/binary-search/
- Description: Return index using binary search if exists, else return -1
- Pattern: Implement binary search.
- Difficulty: 1/10

### 2. Guess Number Higher or Lower
- File: `guess_number_higher_or_lower.py`
- Link: https://leetcode.com/problems/guess-number-higher-or-lower/
- Description: Use binary search to interact with API.
- Pattern: Implement binary search.
- Difficulty: 1/10

### 3. Search Insert Position
- File: `search_insert_position.py`
- Link: https://leetcode.com/problems/search-insert-position/
- Description: Use binary search to return index of element in array. If element does not exist in array, return index that it should be inserted if it is sorted.
- Pattern: Implement binary search, but if nothing is found, return left pointer index.
- Difficulty: 2/10

### 4. Peak index in a mountain array
- File: `peak_index_in_mountain_array.py`
- Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
- Description: Use binary search
- Pattern: Implement binary search, but if nothing is found, return left pointer index.
- Difficulty: 2/10

### 5. Valid perfect square
- File: `valid_perfect_square.py`
- Link: https://leetcode.com/problems/valid-perfect-square/
- Description: Use binary search
- Pattern: Implement binary search, left pointer will be 2, right will be number//2. If value**2 = number, then return True, else return False.
- Difficulty: 2/10

### 6. Find the Distance Value Between Two Arrays
- File: `find_distance_between_two_arrays.py`
- Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
- Description: Use binary search
- Pattern: Sort 1 of the 2 arrays to use binary search. Use binary search to reduce amount of elements looked through in sorted array and prevent O(n^2).
- Difficulty: 2/10 (I don't fully get how binary search solves this problem?)
- Time complexity: O(n log n)
