class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]
        
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f: break
            
        a = nums[0]
        while a!=s:
            a = nums[a]
            s = nums[s]
        return a