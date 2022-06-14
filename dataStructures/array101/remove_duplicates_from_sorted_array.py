nums = [0,0,1,1,1,2,2,3,3,4]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        for i in range(1, length):

            # ### Aproach 1 ###
            # if nums[i] != nums[i-1]:
            #     nums[j] = nums[i]
            #     j+=1

            ### Aproach 2 ###
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[j] = nums[i]
                j+=1

        return j

print(solution.removeDuplicates(nums))
print(f"Input: {nums}")
print("Answer: 5, nums = [0,1,2,3,4,_,_,_,_,_]")