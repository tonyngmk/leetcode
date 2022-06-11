nums = [0,1,0,3,12]
ans = [1,3,12,0,0]
class Solution(object):
    def moveZeroes(self, A):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # ### My solution (might 2 pass in worse-case scenario when all element is 0)
        # j = 0
        # n = len(A)
        # for i in range(n):
        #     if A[i] == 0:
        #         continue
        #     else:
        #         A[j] = A[i]
        #         j+=1

        # for i in range(j, n):
        #     A[i] = 0
        
        # return A


        ### Better solution
        j = 0
        n = len(A)
        for i in range(n):
            if A[i] != 0:
                A[j], A[i] = A[i], A[j]
                j+=1
            
        return A

solution = Solution()
print("Question: ", nums, ans)
print("Answer", solution.moveZeroes(nums))