nums = [-1,0,3,5,9,12]; target = 9
ans = 4

# nums = [-1,0,3,5,9,12]; target = 2
# ans = -1

class Solution(object):
    def iterative_binary_search(self, A, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(A)
        i, j = 0, n-1
        while i <= j:
            mid = i + (j-i)//2
            if A[mid] == x:
                return mid
            elif x < A[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1

# def recursive_binary_search(A, i, j, x):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     while i <= j :
#         mid = i + (j-i)//2

#         if A[mid] == x:
#             return mid
#         elif x < A[mid]:
#             return recursive_binary_search(A, i, mid-1, x)
#         else:
#             return recursive_binary_search(A, mid+1, j, x)

#     return -1


solution = Solution()

print("Question: ", nums, target, ans)
print("Answer: ", solution.iterative_binary_search(nums, target))
# print("Answer: ", recursive_binary_search(nums, 0, len(nums), target))