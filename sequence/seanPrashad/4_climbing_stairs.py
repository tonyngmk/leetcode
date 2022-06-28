class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
#         # Approach 1: Dynamic programming: Recursion with Memoisation
#         def climb_Stairs(i, n, memo):
#             if (i > n):
#                 return 0

#             elif i == n:
#                 return 1
            
#             elif memo[i] != 0:
#                 return memo[i]
            
#             memo[i] = climb_Stairs(i+1, n, memo) + climb_Stairs(i+2, n, memo)
#             return memo[i]
        
#         memo = [0 for i in range(n)]
#         return climb_Stairs(0, n, memo)

        
        # Approach 2: Dynamic programming: Bottom-up approach 
        A = [0 for i in range (n+1)]
        if n >= 1: A[1] = 1
        if n >= 2: A[2] = 2
        if n >= 3:
            for i in range(3, n+1):
                A[i] = A[i-1] + A[i-2]
        
        return A[n]

    
