# # Example 1:
# arr = [2,1]
# ans = False

# # Example 2:
# arr = [3,5,5]
# ans = False

# # Example 3:
# arr = [0,3,2,1]
# ans = True

class Solution(object):
    def numPermsDISequence(self, A):
        """
        :type s: str
        :rtype: int
        """
        i, j, n = 0, len(A)-1, len(A)
        while i < n-1 and A[i] < A[i+1]:
            i+=1
        while j > 0 and A[j] < A[j-1]:
            j-=1

        return 0 < i == j < n-1

solution = Solution()
print("Question:", arr, ans)
print("Answer:", solution.numPermsDISequence(arr))