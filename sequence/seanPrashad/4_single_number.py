nums = [2,2,1]; ans = 1
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums: ans ^= i
        return ans

solution = Solution()
print(solution.singleNumber(nums))