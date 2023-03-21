class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        ans = 1
        
        for num in nums:
            if (num-1) not in nums and (num+1) in nums:
                curr_ans = 1
                curr_num = num+1
                while curr_num in nums:
                    curr_ans += 1
                    curr_num += 1
                ans = max(ans, curr_ans)
        
        return ans
