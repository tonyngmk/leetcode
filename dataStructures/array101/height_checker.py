# heights = [1,1,4,2,1,3]
# ans = 3

heights = [5,1,2,3,4]
ans = 5

# heights = [1,2,3,4,5]
# ans = 0

class Solution(object):
    def heightChecker(self, A):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Create count-sort array
        n = len(A)
        A2 = [0 for i in range(101)]
        for i in range(n):
            A2[A[i]] += 1

        # Use count-sort array to find differencce
        j = 0
        ans = 0
        for i in range(n):
            if A2[j] == 0:
                j += 1
            
            if j != A[i]:
                ans +=1

            A2[j] -= 1

        return ans

solution = Solution()
print("Question: ", heights, ans)
print("Answer: ", solution.heightChecker(heights))
