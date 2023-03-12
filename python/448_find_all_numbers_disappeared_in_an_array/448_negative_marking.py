class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num)-1
            if nums[i] > 0: nums[i] *= -1
                
        return [i+1 for i, j in enumerate(nums) if j > 0]