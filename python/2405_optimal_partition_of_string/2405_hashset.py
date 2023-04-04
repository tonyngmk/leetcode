class Solution:
    def partitionString(self, s: str) -> int:

        S = set()
        ans = 0
        for c in s:
            if c in S:
                S = set()
                ans += 1
            S.add(c)
        return ans + 1
