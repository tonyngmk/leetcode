class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        ans = curr = 0
        A.sort()

        while A and (A[-1] + curr) > 0:
            curr += A.pop()
            ans += curr
        return ans
        