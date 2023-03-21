class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = subarray_length = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: subarray_length += 1
            if (nums[i] != 0 or i==(n-1)) and subarray_length:
                ans += int((subarray_length * (subarray_length+1))/2)
                subarray_length = 0
                
        return ans