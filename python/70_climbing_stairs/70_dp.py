class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        
        a = b = 1
        for i in range(n):
            a, b = b, a+b
            
        return a
        