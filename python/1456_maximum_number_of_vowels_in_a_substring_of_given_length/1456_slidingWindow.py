class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        count = 0
        vowels = set("aeiou")
        for i in range(k):
            count += int(s[i] in vowels)
        
        ans = count
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            ans = max(ans, count)
        return ans
