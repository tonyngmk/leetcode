class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        ans = [0] * (n+1)
        
        for i in range(1, n+1):
            ans[i] = ans[(i&(i-1))] + 1
            
        return ans
            