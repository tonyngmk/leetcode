nums = [1,0,1,1,0,1]

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(list(map(len, "".join([str(i) for i in nums]).split("0"))))

solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))