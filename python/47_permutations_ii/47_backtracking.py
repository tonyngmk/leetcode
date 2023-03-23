class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)
        def backtrack(i=0):
            if i == n: output.add(tuple(nums[:]))
                
            for x in range(i, n):
                nums[x], nums[i] = nums[i], nums[x]
                backtrack(i+1)
                nums[i], nums[x] = nums[x], nums[i]
        
        backtrack()
        return output
    