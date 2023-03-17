class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        i, j = 0, len(nums)
        
        while i < j:
            mid = i + (j-i)//2
            
            if nums[mid] < target: i = mid + 1
            else: j = mid
                
        return i
