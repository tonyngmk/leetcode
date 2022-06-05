nums = [0,0,1,1,1,2,2,3,3,4]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0 # pointer
        k = 0
        j = nums[0] # value of pointer
        l = len(nums)

        for i in range(l):
            if nums[i] == j:
                continue
            else:
                nums[m] = j
                k += 1

        return k, nums

solution = Solution()
print(solution.removeDuplicates(nums))
print("Answer: 5, nums = [0,1,2,3,4,_,_,_,_,_]")