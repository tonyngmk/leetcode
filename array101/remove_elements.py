nums = [3,2,2,3]; val = 3

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        j = 0
        ignored = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                ignored += 1
                continue
            else:
                nums[j] = nums[i]
                j += 1
        for i in range(ignored):
            nums.pop()
        return nums

solution = Solution()
print(solution.removeElement(nums, val))