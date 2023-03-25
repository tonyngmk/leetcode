class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = ans = nums[0]
        
        for num in nums[1:]:
            curr = max(num, curr+num) # only activated if current num flips all cumulative to negative
            ans = max(curr, ans)
            
        return ans
            
