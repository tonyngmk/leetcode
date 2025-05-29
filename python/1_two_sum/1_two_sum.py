from typing import List
class Solution:
    def __init__(self):
        self.nums = [2,7,11,15]
        self.target = 9
        print(self.twoSum(self.nums, self.target))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {j:i for i, j in enumerate(nums)}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d and d[comp] != i: return [i, d[comp]]

sol = Solution()
