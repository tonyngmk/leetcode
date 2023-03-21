class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        n = len(nums)

        def backtrack(combo=[], i=0):
            output.append(combo[:])
            
            for x in range(i, n):
                combo.append(nums[x])
                backtrack(combo, x+1)
                combo.pop()
            
        backtrack()
        return output
    