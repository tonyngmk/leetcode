class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        highest = 1
        
        for num in nums:
            if num-1 not in s and num+1 in s:
                curr_num = num
                curr_highest = 1
                
                while curr_num+1 in s:
                    curr_num += 1
                    curr_highest += 1
                highest = max(highest, curr_highest)
        
        return highest