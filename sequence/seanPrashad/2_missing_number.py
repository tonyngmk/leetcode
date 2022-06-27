class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums)
        for i, j in enumerate(nums): ans ^= i ^ j
        return ans