class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recursion(i, n, memo):
            if i > n: return 0 # exceed
            if i == n: return 1 # base
            if memo[i] > 0: return memo[i] # memoization
            memo[i] = recursion(i+1, n, memo) + recursion(i+2, n, memo) # recursive recurrence
            return memo[i] # final answer
            
        memo = [0] * (n+1)
        return recursion(0, n, memo)
        