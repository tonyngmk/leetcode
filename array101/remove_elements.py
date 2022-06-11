nums = [3,2,2,3]; val = 3

class Solution(object):
    def removeElement(self, A, x):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        j = 0
        n = len(A)
        for i in range(n):
            if A[i] != x:
                A[i], A[j] = A[j], A[i]
                j += 1
            print(i, j, A)
        
        A = A[:j]
        return j

solution = Solution()
print(solution.removeElement(nums, val))