class Solution:
    def house_robbers_i(self, nums):
        a = b = 0
        
        for num in nums:
            a, b = b, max(b, a+num)
        return b
        
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        return max(self.house_robbers_i(nums[1:]), self.house_robbers_i(nums[:-1]))