class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        
        def backtrack(combo=[], i=0):
            output.append(combo[:])
            
            for x in range(i, n):
                if x > i and nums[x]==nums[x-1]: continue
                combo.append(nums[x])
                backtrack(combo, x+1)
                combo.pop()
            
        backtrack()
        return output
        