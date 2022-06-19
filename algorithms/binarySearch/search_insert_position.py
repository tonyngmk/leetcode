# nums = [1,3,5,6]; target = 5
# ans = 2

nums = [1,3,5,6]; target = 2
ans = 1

# nums = [1,3,5,6]; target = 7
# ans = 4

class Solution(object):
    def searchInsert(self, A, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(A)
        i, j = 0, n-1
        
        while i <= j:
            mid = i + (j-i)//2
            if x == A[mid]:
                return mid
            elif x > A[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

solution = Solution()
print(nums, target, ans)
print(solution.searchInsert(nums, target))