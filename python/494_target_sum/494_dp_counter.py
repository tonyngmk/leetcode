class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        c = collections.Counter({0:1})
        
        for num in nums:
            temp_c = collections.Counter()
            for k in c:
                temp_c[k+num] += c[k]
                temp_c[k-num] += c[k]
            c = temp_c
            
        return c[target]