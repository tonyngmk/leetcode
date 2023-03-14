class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {j:i for i, j in enumerate(nums)}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d and d[comp] != i: return [i, d[comp]]
