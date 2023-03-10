from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return True
        return False


assert(Solution().containsDuplicate([1,2,3,1])==True)
assert(Solution().containsDuplicate([1,2,3])==False)
