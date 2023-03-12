class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = len(nums)
        
        for i, j in enumerate(nums):
            ans ^= i ^ j
            
        return ans