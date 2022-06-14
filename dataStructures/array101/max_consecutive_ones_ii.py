nums = [1,0,1,1,0]
ans = 4

class Solution(object):
    def findMaxConsecutiveOnes(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """

        # ### Elegant solution keeping previous and current length
        # a, b, mx = -1, 0, 0
        # for i in A:
        #     if i == 0:
        #         a, b = b, 0
        #     else:
        #         b += 1
        #         mx = max(mx, a+1+b)
        # return mx

        # Sliding window solution
        mx = 0 # longest sequence
        i, j = 0, 0 # left and right pointer
        k = 0 # number of zeroes
        n = len(A) # length

        while j < n: # alternative for traversing infinite input as compared to for-loop
            if A[j] == 0: # Valid window (right pointer encountering first zero)
                k += 1

            while k == 2: # Invalid window (move left pointer until k <= 1)
                if A[i] == 0: # Only reduce number of zeroes until left pointer touches a 0
                    k -= 1
                i += 1
            
            mx = max(mx, j - i + 1) # Update our longest sequence
            j += 1 # Traverse using while

        return mx 

solution = Solution()
print("Question: ", nums, ans)
print("Answer: ", solution.findMaxConsecutiveOnes(nums))