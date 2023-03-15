class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]
        x = 1
        n = len(nums)
        for num in nums[:-1]:
            x *= num
            ans.append(x)
            
        x = 1
        for i in range(n-2, -1, -1):
            x *= nums[i+1]
            ans[i] *= x
            
        return ans