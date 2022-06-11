nums = [3,1,2,4]
ans = [2,4,3,1]

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = 0
        n = len(A)
        for i in range(n):
            if A[i] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j+=1
        return A

solution = Solution()
print("Question: ", nums, ans)
print("Answer: ", solution.sortArrayByParity(nums))