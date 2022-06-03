nums = [-4,-1,0,3,10]

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        result = []

        while left != right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1
        
        result.append(nums[left]**2)

        return result[::-1]

solution = Solution()
print(solution.sortedSquares(nums))