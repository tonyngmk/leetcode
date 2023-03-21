class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 2: return 0
        
        ans = 0
        curr_ans = 0 
        diff = nums[1]-nums[0]
        
        for i in range(2, n):
            curr_diff = nums[i]-nums[i-1]
            if curr_diff==diff: curr_ans += 1
            else:
                curr_ans = 0
                diff = curr_diff
            ans += curr_ans
            
        return ans
            