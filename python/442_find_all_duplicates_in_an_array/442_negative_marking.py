class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = []
        n = len(nums)
        for i in range(n):
            index = abs(nums[i])-1
            if nums[index] > 0: nums[index] *= -1
            else: ans.append(index+1)
                
        return ans
        