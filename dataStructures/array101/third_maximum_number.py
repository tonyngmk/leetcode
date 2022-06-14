# nums = [3,2,1]
# ans = 1

# nums = [2,1]
# ans = 1

# nums = [1]
# ans = 1

nums = [2,2,3,1]
ans = 1

# nums = [1,2]
# ans = 1

class Solution(object):
    def thirdMax(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Set method
        S = set(A) # time: O(n), space: O(n)
        if len(S) <= 2: return max(S) # time: O(n) 
        else:
            S.remove(max(S)); S.remove(max(S)) # time: O(n), 2 pass
            return max(S)  # time: O(n)

        # Best case: 
        #   Time: O(n), 2 pass, space O(n)
        # Worse case: 
        #   Time: O(n), 4 pass, space O(n)
            

        # ### Oh no they did not want to sort array
        # a, b, c = 0, 0, 0 
        # for i in nums:
        #     ### Missing slots (we need this as all numbers will tend to move to start)
        #     if a == 0: 
        #         if b == 0 and c == 0: c = i # All missing, just slot i into c
        #         elif b == 0: # if first 2 missing
        #             if i > c: b = i 
        #             else: b, c = c, i
        #         else: # if only first missing
        #             if i > b: a = i
        #             elif b > i > c: a, b, c = b, i, c
        #             elif b > c > i: a, b, c = b, c, i

        #     ### Fully occupied
        #     if i > c: c = i # enter values
        #     if c > b: b, c = c, b # swap b and c
        #     if b > a: a, b = b, a # swap a and b

        #     # Ensure distinct (push back)
        #     if a==b: a = 0
        #     if b==c: a, b, c = 0, a, b
        # return a, b, c

solution = Solution()
print("Question: ", nums, ans)
print("Answer: ", solution.thirdMax(nums))