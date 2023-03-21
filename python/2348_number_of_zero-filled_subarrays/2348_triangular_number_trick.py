class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = subarray_length = 0
        for num in nums:
            if num == 0: subarray_length += 1
            else: subarray_length = 0
            ans += subarray_length
                
        return ans