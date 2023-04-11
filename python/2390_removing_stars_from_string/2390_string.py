class Solution:
    def removeStars(self, s: str) -> str:

        n = len(s)-1
        skip = 0
        ans = ""

        while n >= 0:
            if s[n] == "*": skip += 1
            elif skip: skip -= 1
            else: ans += s[n]
            n -= 1

        return ans[::-1]
        