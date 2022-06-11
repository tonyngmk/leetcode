arr = [17,18,5,4,6,1]
ans = [18,6,6,6,1,-1]

class Solution(object):
    def replaceElements(self, A):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # arr[-2] = arr[-1]
        # arr[-1] = -1
        # for i in range(3, len(arr)+1):
        #     mx = max(arr[-i], arr[-i+1])
        #     arr[-i] = mx
        mx = -1
        for i in range(len(A)-1, -1, -1):
            ### My solution ###
            mx2 = mx # value for assignment (max(A[i], A[i+1]))
            mx = max(mx, A[i]) # calculate next value for A[i-1] before replacing A[i]
            A[i] = mx2
            
            ### Best solution ###
            # Calculate both RHS values before assigning to LHS, saving 1 initialisation of variable's memory
            # A[i], mx = mx, max(mx, A[i])

        return arr

solution = Solution()
print("Input: ", arr, ans)
print("Answer: ", solution.replaceElements(arr))