nums = [555,901,482,1771]

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return len([i for i in map(len, map(str, nums)) if i%2==0])
        return sum(1 for i in nums if len(str(i)) %2 == 0)

solution = Solution()
print(solution.findNumbers(nums))